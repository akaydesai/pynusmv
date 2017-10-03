import unittest

from pynusmv_lower_interface.nusmv.cmd import cmd
from pynusmv_lower_interface.nusmv.prop import prop as nsprop
from pynusmv_lower_interface.nusmv.mc import mc as nsmc

from pynusmv.init import init_nusmv, deinit_nusmv
from pynusmv import mc
from pynusmv import glob
from pynusmv import prop
from pynusmv import parser


class TestMC(unittest.TestCase):
    
    def setUp(self):
        init_nusmv()
        
    def tearDown(self):
        deinit_nusmv()
    
    
    def test_nsmc(self):
        # Initialize the model
        ret = cmd.Cmd_SecureCommandExecute("read_model -i"
                                           " tests/pynusmv/models/admin.smv")
        self.assertEqual(ret, 0)
        ret = cmd.Cmd_SecureCommandExecute("go")
        self.assertEqual(ret, 0)
        
        # Check CTL specs
        propDb = nsprop.PropPkg_get_prop_database()
        for i in range(nsprop.PropDb_get_size(propDb)):
            p = nsprop.PropDb_get_prop_at_index(propDb, i)
            if nsprop.Prop_get_type(p) == nsprop.Prop_Ctl:
                nsmc.Mc_CheckCTLSpec(p)
    
    def test_mc(self):
        # Initialize the model
        ret = cmd.Cmd_SecureCommandExecute("read_model -i"
                                           " tests/pynusmv/models/admin.smv")
        self.assertEqual(ret, 0)
        ret = cmd.Cmd_SecureCommandExecute("go")
        self.assertEqual(ret, 0)
        
        ret = {"(EF admin = alice -> AG (admin != none -> admin = alice))":
               False,
               "(EF admin = alice & EF admin = bob)": True}
        
        propDb = glob.prop_database()
        fsm = propDb.master.bddFsm
        
        for p in propDb:
            if p.type == prop.propTypes["CTL"]:
                spec = p.expr
                self.assertEqual(mc.check_ctl_spec(fsm, spec), ret[str(spec)])
    
    def test_mc_ltl_true(self):
        # Initialize the model
        glob.load("tests/pynusmv/models/admin.smv")
        glob.compute_model()
        fsm = glob.prop_database().master.bddFsm
        
        spec = prop.Spec(parser.parse_ltl_spec("G admin = none"))
        self.assertEqual(mc.check_ltl_spec(spec), False)
    
    def test_mc_ltl_false(self):
        # Initialize the model
        glob.load("tests/pynusmv/models/admin.smv")
        glob.compute_model()
        fsm = glob.prop_database().master.bddFsm
        
        spec = prop.Spec(parser.parse_ltl_spec(
                         "(F admin = alice) | (F admin = bob)"))
        self.assertEqual(mc.check_ltl_spec(spec), True)
    
    def test_mc_explain_ltl_true(self):
        # Initialize the model
        glob.load("tests/pynusmv/models/admin.smv")
        glob.compute_model()
        
        spec = prop.Spec(parser.parse_ltl_spec(
                            "(F admin = alice) | (F admin = bob)"))
        
        result, explanation = mc.check_explain_ltl_spec(spec)
        self.assertTrue(result)
        self.assertIsNone(explanation)
    
    def test_mc_explain_ltl_false(self):
        # Initialize the model
        glob.load("tests/pynusmv/models/admin.smv")
        glob.compute_model()
        
        spec = prop.Spec(parser.parse_ltl_spec("G admin = none"))
        
        result, explanation = mc.check_explain_ltl_spec(spec)
        self.assertFalse(result)
        self.assertIsNotNone(explanation)
        
        #print(explanation[0])
        #for inputs, state in zip(explanation[1::2], explanation[2::2]):
        #    print(inputs)
        #    print(state)
        self.assertTrue(any(state["admin"] != "none"
                            for state in explanation[::2]))