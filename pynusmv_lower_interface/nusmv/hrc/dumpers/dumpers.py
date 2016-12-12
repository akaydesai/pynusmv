# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_dumpers')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_dumpers')
    _dumpers = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_dumpers', [dirname(__file__)])
        except ImportError:
            import _dumpers
            return _dumpers
        if fp is not None:
            try:
                _mod = imp.load_module('_dumpers', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _dumpers = swig_import_helper()
    del swig_import_helper
else:
    import _dumpers
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

PRIuPTR = _dumpers.PRIuPTR
PRIdPTR = _dumpers.PRIdPTR
LLU = _dumpers.LLU
LLO = _dumpers.LLO
LLX = _dumpers.LLX
false = _dumpers.false
true = _dumpers.true
OUTCOME_GENERIC_ERROR = _dumpers.OUTCOME_GENERIC_ERROR
OUTCOME_PARSER_ERROR = _dumpers.OUTCOME_PARSER_ERROR
OUTCOME_SYNTAX_ERROR = _dumpers.OUTCOME_SYNTAX_ERROR
OUTCOME_FILE_ERROR = _dumpers.OUTCOME_FILE_ERROR
OUTCOME_SUCCESS_REQUIRED_HELP = _dumpers.OUTCOME_SUCCESS_REQUIRED_HELP
OUTCOME_SUCCESS = _dumpers.OUTCOME_SUCCESS

def Object_destroy(arg1: 'Object_ptr', arg: 'void *') -> "void":
    """Object_destroy(Object_ptr arg1, void * arg)"""
    return _dumpers.Object_destroy(arg1, arg)

def Object_copy(arg1: 'Object_ptr const') -> "Object_ptr":
    """Object_copy(Object_ptr const arg1) -> Object_ptr"""
    return _dumpers.Object_copy(arg1)
HDS_HRC_TOP = _dumpers.HDS_HRC_TOP
HDS_LIST_MODS = _dumpers.HDS_LIST_MODS
HDS_MOD = _dumpers.HDS_MOD
HDS_MOD_NAME = _dumpers.HDS_MOD_NAME
HDS_LIST_MOD_FORMAL_PARAMS = _dumpers.HDS_LIST_MOD_FORMAL_PARAMS
HDS_MOD_FORMAL_PARAM = _dumpers.HDS_MOD_FORMAL_PARAM
HDS_LIST_MOD_INSTANCES = _dumpers.HDS_LIST_MOD_INSTANCES
HDS_MOD_INSTANCE = _dumpers.HDS_MOD_INSTANCE
HDS_MOD_INSTANCE_VARNAME = _dumpers.HDS_MOD_INSTANCE_VARNAME
HDS_MOD_INSTANCE_MODNAME = _dumpers.HDS_MOD_INSTANCE_MODNAME
HDS_LIST_MOD_INSTANCE_ACTUAL_PARAMS = _dumpers.HDS_LIST_MOD_INSTANCE_ACTUAL_PARAMS
HDS_MOD_INSTANCE_ACTUAL_PARAM = _dumpers.HDS_MOD_INSTANCE_ACTUAL_PARAM
HDS_LIST_SYMBOLS = _dumpers.HDS_LIST_SYMBOLS
HDS_SYMBOL = _dumpers.HDS_SYMBOL
HDS_LIST_ASSIGNS = _dumpers.HDS_LIST_ASSIGNS
HDS_ASSIGN_INIT = _dumpers.HDS_ASSIGN_INIT
HDS_ASSIGN_INVAR = _dumpers.HDS_ASSIGN_INVAR
HDS_ASSIGN_NEXT = _dumpers.HDS_ASSIGN_NEXT
HDS_LIST_CONSTRAINTS = _dumpers.HDS_LIST_CONSTRAINTS
HDS_CONSTRAINT_INIT = _dumpers.HDS_CONSTRAINT_INIT
HDS_CONSTRAINT_INVAR = _dumpers.HDS_CONSTRAINT_INVAR
HDS_CONSTRAINT_TRANS = _dumpers.HDS_CONSTRAINT_TRANS
HDS_LIST_FAIRNESS = _dumpers.HDS_LIST_FAIRNESS
HDS_JUSTICE = _dumpers.HDS_JUSTICE
HDS_COMPASSION = _dumpers.HDS_COMPASSION
HDS_LIST_SPECS = _dumpers.HDS_LIST_SPECS
HDS_SPEC = _dumpers.HDS_SPEC
HDS_LIST_COMPILER_INFO = _dumpers.HDS_LIST_COMPILER_INFO
HDS_LIST_SYNTAX_ERRORS = _dumpers.HDS_LIST_SYNTAX_ERRORS
HDS_ERROR = _dumpers.HDS_ERROR
class HrcDumperInfo(_object):
    """Proxy of C HrcDumperInfo_TAG struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HrcDumperInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HrcDumperInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["stage"] = _dumpers.HrcDumperInfo_stage_set
    __swig_getmethods__["stage"] = _dumpers.HrcDumperInfo_stage_get
    if _newclass:
        stage = _swig_property(_dumpers.HrcDumperInfo_stage_get, _dumpers.HrcDumperInfo_stage_set)
    __swig_getmethods__["n1"] = _dumpers.HrcDumperInfo_n1_get
    if _newclass:
        n1 = _swig_property(_dumpers.HrcDumperInfo_n1_get)
    __swig_getmethods__["n2"] = _dumpers.HrcDumperInfo_n2_get
    if _newclass:
        n2 = _swig_property(_dumpers.HrcDumperInfo_n2_get)
    __swig_getmethods__["error"] = _dumpers.HrcDumperInfo_error_get
    if _newclass:
        error = _swig_property(_dumpers.HrcDumperInfo_error_get)
    __swig_setmethods__["symb_cat"] = _dumpers.HrcDumperInfo_symb_cat_set
    __swig_getmethods__["symb_cat"] = _dumpers.HrcDumperInfo_symb_cat_get
    if _newclass:
        symb_cat = _swig_property(_dumpers.HrcDumperInfo_symb_cat_get, _dumpers.HrcDumperInfo_symb_cat_set)
    __swig_setmethods__["spec_type"] = _dumpers.HrcDumperInfo_spec_type_set
    __swig_getmethods__["spec_type"] = _dumpers.HrcDumperInfo_spec_type_get
    if _newclass:
        spec_type = _swig_property(_dumpers.HrcDumperInfo_spec_type_get, _dumpers.HrcDumperInfo_spec_type_set)
    __swig_setmethods__["last_in_list"] = _dumpers.HrcDumperInfo_last_in_list_set
    __swig_getmethods__["last_in_list"] = _dumpers.HrcDumperInfo_last_in_list_get
    if _newclass:
        last_in_list = _swig_property(_dumpers.HrcDumperInfo_last_in_list_get, _dumpers.HrcDumperInfo_last_in_list_set)
    __swig_setmethods__["list_is_empty"] = _dumpers.HrcDumperInfo_list_is_empty_set
    __swig_getmethods__["list_is_empty"] = _dumpers.HrcDumperInfo_list_is_empty_get
    if _newclass:
        list_is_empty = _swig_property(_dumpers.HrcDumperInfo_list_is_empty_get, _dumpers.HrcDumperInfo_list_is_empty_set)
    __swig_setmethods__["hrcNode"] = _dumpers.HrcDumperInfo_hrcNode_set
    __swig_getmethods__["hrcNode"] = _dumpers.HrcDumperInfo_hrcNode_get
    if _newclass:
        hrcNode = _swig_property(_dumpers.HrcDumperInfo_hrcNode_get, _dumpers.HrcDumperInfo_hrcNode_set)
    __swig_setmethods__["user"] = _dumpers.HrcDumperInfo_user_set
    __swig_getmethods__["user"] = _dumpers.HrcDumperInfo_user_get
    if _newclass:
        user = _swig_property(_dumpers.HrcDumperInfo_user_get, _dumpers.HrcDumperInfo_user_set)

    def __init__(self):
        """__init__(HrcDumperInfo_TAG self) -> HrcDumperInfo"""
        this = _dumpers.new_HrcDumperInfo()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _dumpers.delete_HrcDumperInfo
    __del__ = lambda self: None
HrcDumperInfo_swigregister = _dumpers.HrcDumperInfo_swigregister
HrcDumperInfo_swigregister(HrcDumperInfo)
HRC_STAGE_BEGIN = _dumpers.HRC_STAGE_BEGIN
HRC_STAGE_END = _dumpers.HRC_STAGE_END
HRC_STAGE_BEGIN_END = _dumpers.HRC_STAGE_BEGIN_END

class HrcDumperInfo_TAG_error(_object):
    """Proxy of C HrcDumperInfo_TAG_error struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HrcDumperInfo_TAG_error, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HrcDumperInfo_TAG_error, name)
    __repr__ = _swig_repr
    __swig_setmethods__["lineno"] = _dumpers.HrcDumperInfo_TAG_error_lineno_set
    __swig_getmethods__["lineno"] = _dumpers.HrcDumperInfo_TAG_error_lineno_get
    if _newclass:
        lineno = _swig_property(_dumpers.HrcDumperInfo_TAG_error_lineno_get, _dumpers.HrcDumperInfo_TAG_error_lineno_set)
    __swig_setmethods__["filename"] = _dumpers.HrcDumperInfo_TAG_error_filename_set
    __swig_getmethods__["filename"] = _dumpers.HrcDumperInfo_TAG_error_filename_get
    if _newclass:
        filename = _swig_property(_dumpers.HrcDumperInfo_TAG_error_filename_get, _dumpers.HrcDumperInfo_TAG_error_filename_set)
    __swig_setmethods__["message"] = _dumpers.HrcDumperInfo_TAG_error_message_set
    __swig_getmethods__["message"] = _dumpers.HrcDumperInfo_TAG_error_message_get
    if _newclass:
        message = _swig_property(_dumpers.HrcDumperInfo_TAG_error_message_get, _dumpers.HrcDumperInfo_TAG_error_message_set)
    __swig_setmethods__["token"] = _dumpers.HrcDumperInfo_TAG_error_token_set
    __swig_getmethods__["token"] = _dumpers.HrcDumperInfo_TAG_error_token_get
    if _newclass:
        token = _swig_property(_dumpers.HrcDumperInfo_TAG_error_token_get, _dumpers.HrcDumperInfo_TAG_error_token_set)

    def __init__(self):
        """__init__(HrcDumperInfo_TAG_error self) -> HrcDumperInfo_TAG_error"""
        this = _dumpers.new_HrcDumperInfo_TAG_error()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _dumpers.delete_HrcDumperInfo_TAG_error
    __del__ = lambda self: None
HrcDumperInfo_TAG_error_swigregister = _dumpers.HrcDumperInfo_TAG_error_swigregister
HrcDumperInfo_TAG_error_swigregister(HrcDumperInfo_TAG_error)

class HrcDumperInfo_TAG_n2(_object):
    """Proxy of C HrcDumperInfo_TAG_n2 struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HrcDumperInfo_TAG_n2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HrcDumperInfo_TAG_n2, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _dumpers.HrcDumperInfo_TAG_n2_type_set
    __swig_getmethods__["type"] = _dumpers.HrcDumperInfo_TAG_n2_type_get
    if _newclass:
        type = _swig_property(_dumpers.HrcDumperInfo_TAG_n2_type_get, _dumpers.HrcDumperInfo_TAG_n2_type_set)
    __swig_setmethods__["body"] = _dumpers.HrcDumperInfo_TAG_n2_body_set
    __swig_getmethods__["body"] = _dumpers.HrcDumperInfo_TAG_n2_body_get
    if _newclass:
        body = _swig_property(_dumpers.HrcDumperInfo_TAG_n2_body_get, _dumpers.HrcDumperInfo_TAG_n2_body_set)
    __swig_setmethods__["expr"] = _dumpers.HrcDumperInfo_TAG_n2_expr_set
    __swig_getmethods__["expr"] = _dumpers.HrcDumperInfo_TAG_n2_expr_get
    if _newclass:
        expr = _swig_property(_dumpers.HrcDumperInfo_TAG_n2_expr_get, _dumpers.HrcDumperInfo_TAG_n2_expr_set)
    __swig_setmethods__["lineno"] = _dumpers.HrcDumperInfo_TAG_n2_lineno_set
    __swig_getmethods__["lineno"] = _dumpers.HrcDumperInfo_TAG_n2_lineno_get
    if _newclass:
        lineno = _swig_property(_dumpers.HrcDumperInfo_TAG_n2_lineno_get, _dumpers.HrcDumperInfo_TAG_n2_lineno_set)

    def __init__(self):
        """__init__(HrcDumperInfo_TAG_n2 self) -> HrcDumperInfo_TAG_n2"""
        this = _dumpers.new_HrcDumperInfo_TAG_n2()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _dumpers.delete_HrcDumperInfo_TAG_n2
    __del__ = lambda self: None
HrcDumperInfo_TAG_n2_swigregister = _dumpers.HrcDumperInfo_TAG_n2_swigregister
HrcDumperInfo_TAG_n2_swigregister(HrcDumperInfo_TAG_n2)

class HrcDumperInfo_TAG_n1(_object):
    """Proxy of C HrcDumperInfo_TAG_n1 struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HrcDumperInfo_TAG_n1, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HrcDumperInfo_TAG_n1, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _dumpers.HrcDumperInfo_TAG_n1_name_set
    __swig_getmethods__["name"] = _dumpers.HrcDumperInfo_TAG_n1_name_get
    if _newclass:
        name = _swig_property(_dumpers.HrcDumperInfo_TAG_n1_name_get, _dumpers.HrcDumperInfo_TAG_n1_name_set)
    __swig_setmethods__["value"] = _dumpers.HrcDumperInfo_TAG_n1_value_set
    __swig_getmethods__["value"] = _dumpers.HrcDumperInfo_TAG_n1_value_get
    if _newclass:
        value = _swig_property(_dumpers.HrcDumperInfo_TAG_n1_value_get, _dumpers.HrcDumperInfo_TAG_n1_value_set)
    __swig_setmethods__["expr"] = _dumpers.HrcDumperInfo_TAG_n1_expr_set
    __swig_getmethods__["expr"] = _dumpers.HrcDumperInfo_TAG_n1_expr_get
    if _newclass:
        expr = _swig_property(_dumpers.HrcDumperInfo_TAG_n1_expr_get, _dumpers.HrcDumperInfo_TAG_n1_expr_set)

    def __init__(self):
        """__init__(HrcDumperInfo_TAG_n1 self) -> HrcDumperInfo_TAG_n1"""
        this = _dumpers.new_HrcDumperInfo_TAG_n1()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _dumpers.delete_HrcDumperInfo_TAG_n1
    __del__ = lambda self: None
HrcDumperInfo_TAG_n1_swigregister = _dumpers.HrcDumperInfo_TAG_n1_swigregister
HrcDumperInfo_TAG_n1_swigregister(HrcDumperInfo_TAG_n1)


def HrcDumper_create(fout: 'FILE *') -> "HrcDumper_ptr":
    """HrcDumper_create(FILE * fout) -> HrcDumper_ptr"""
    return _dumpers.HrcDumper_create(fout)

def HrcDumper_destroy(arg1: 'HrcDumper_ptr') -> "void":
    """HrcDumper_destroy(HrcDumper_ptr arg1)"""
    return _dumpers.HrcDumper_destroy(arg1)

def HrcDumper_dump_snippet(arg1: 'HrcDumper_ptr', snippet: 'HrcDumperSnippet', info: 'HrcDumperInfo') -> "void":
    """HrcDumper_dump_snippet(HrcDumper_ptr arg1, HrcDumperSnippet snippet, HrcDumperInfo info)"""
    return _dumpers.HrcDumper_dump_snippet(arg1, snippet, info)

def HrcDumper_enable_indentation(arg1: 'HrcDumper_ptr', flag: 'boolean') -> "void":
    """HrcDumper_enable_indentation(HrcDumper_ptr arg1, boolean flag)"""
    return _dumpers.HrcDumper_enable_indentation(arg1, flag)

def HrcDumper_inc_indent(arg1: 'HrcDumper_ptr') -> "void":
    """HrcDumper_inc_indent(HrcDumper_ptr arg1)"""
    return _dumpers.HrcDumper_inc_indent(arg1)

def HrcDumper_dec_indent(arg1: 'HrcDumper_ptr') -> "void":
    """HrcDumper_dec_indent(HrcDumper_ptr arg1)"""
    return _dumpers.HrcDumper_dec_indent(arg1)

def HrcDumper_enable_mod_suffix(arg1: 'HrcDumper_ptr', flag: 'boolean') -> "void":
    """HrcDumper_enable_mod_suffix(HrcDumper_ptr arg1, boolean flag)"""
    return _dumpers.HrcDumper_enable_mod_suffix(arg1, flag)

def HrcDumperDebug_create(fout: 'FILE *') -> "HrcDumperDebug_ptr":
    """HrcDumperDebug_create(FILE * fout) -> HrcDumperDebug_ptr"""
    return _dumpers.HrcDumperDebug_create(fout)

def HrcDumperSmv_create(fout: 'FILE *') -> "HrcDumperSmv_ptr":
    """HrcDumperSmv_create(FILE * fout) -> HrcDumperSmv_ptr"""
    return _dumpers.HrcDumperSmv_create(fout)

def HrcDumperXml_create(fout: 'FILE *') -> "HrcDumperXml_ptr":
    """HrcDumperXml_create(FILE * fout) -> HrcDumperXml_ptr"""
    return _dumpers.HrcDumperXml_create(fout)
# This file is compatible with both classic and new-style classes.


