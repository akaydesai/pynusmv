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
        mname = '.'.join((pkg, '_type_checking')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_type_checking')
    _type_checking = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_type_checking', [dirname(__file__)])
        except ImportError:
            import _type_checking
            return _type_checking
        if fp is not None:
            try:
                _mod = imp.load_module('_type_checking', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _type_checking = swig_import_helper()
    del swig_import_helper
else:
    import _type_checking
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

PRIuPTR = _type_checking.PRIuPTR
PRIdPTR = _type_checking.PRIdPTR
LLU = _type_checking.LLU
LLO = _type_checking.LLO
LLX = _type_checking.LLX
false = _type_checking.false
true = _type_checking.true
OUTCOME_GENERIC_ERROR = _type_checking.OUTCOME_GENERIC_ERROR
OUTCOME_PARSER_ERROR = _type_checking.OUTCOME_PARSER_ERROR
OUTCOME_SYNTAX_ERROR = _type_checking.OUTCOME_SYNTAX_ERROR
OUTCOME_FILE_ERROR = _type_checking.OUTCOME_FILE_ERROR
OUTCOME_SUCCESS_REQUIRED_HELP = _type_checking.OUTCOME_SUCCESS_REQUIRED_HELP
OUTCOME_SUCCESS = _type_checking.OUTCOME_SUCCESS

def TypeChecker_create(symbolTable: 'struct SymbTable_TAG *') -> "TypeChecker_ptr":
    """TypeChecker_create(struct SymbTable_TAG * symbolTable) -> TypeChecker_ptr"""
    return _type_checking.TypeChecker_create(symbolTable)

def TypeChecker_create_with_default_checkers(symbolTable: 'struct SymbTable_TAG *') -> "TypeChecker_ptr":
    """TypeChecker_create_with_default_checkers(struct SymbTable_TAG * symbolTable) -> TypeChecker_ptr"""
    return _type_checking.TypeChecker_create_with_default_checkers(symbolTable)

def TypeChecker_destroy(arg1: 'TypeChecker_ptr') -> "void":
    """TypeChecker_destroy(TypeChecker_ptr arg1)"""
    return _type_checking.TypeChecker_destroy(arg1)

def TypeChecker_get_symb_table(arg1: 'TypeChecker_ptr') -> "struct SymbTable_TAG *":
    """TypeChecker_get_symb_table(TypeChecker_ptr arg1) -> struct SymbTable_TAG *"""
    return _type_checking.TypeChecker_get_symb_table(arg1)

def TypeChecker_check_layer(arg1: 'TypeChecker_ptr', layer: 'SymbLayer_ptr') -> "boolean":
    """TypeChecker_check_layer(TypeChecker_ptr arg1, SymbLayer_ptr layer) -> boolean"""
    return _type_checking.TypeChecker_check_layer(arg1, layer)

def TypeChecker_check_constrains(arg1: 'TypeChecker_ptr', init: 'node_ptr', trans: 'node_ptr', invar: 'node_ptr', assign: 'node_ptr', justice: 'node_ptr', compassion: 'node_ptr') -> "boolean":
    """TypeChecker_check_constrains(TypeChecker_ptr arg1, node_ptr init, node_ptr trans, node_ptr invar, node_ptr assign, node_ptr justice, node_ptr compassion) -> boolean"""
    return _type_checking.TypeChecker_check_constrains(arg1, init, trans, invar, assign, justice, compassion)

def TypeChecker_check_property(arg1: 'TypeChecker_ptr', property: 'struct Prop_TAG *') -> "boolean":
    """TypeChecker_check_property(TypeChecker_ptr arg1, struct Prop_TAG * property) -> boolean"""
    return _type_checking.TypeChecker_check_property(arg1, property)

def TypeChecker_is_expression_wellformed(arg1: 'TypeChecker_ptr', expression: 'node_ptr', context: 'node_ptr') -> "boolean":
    """TypeChecker_is_expression_wellformed(TypeChecker_ptr arg1, node_ptr expression, node_ptr context) -> boolean"""
    return _type_checking.TypeChecker_is_expression_wellformed(arg1, expression, context)

def TypeChecker_is_specification_wellformed(arg1: 'TypeChecker_ptr', expression: 'node_ptr') -> "boolean":
    """TypeChecker_is_specification_wellformed(TypeChecker_ptr arg1, node_ptr expression) -> boolean"""
    return _type_checking.TypeChecker_is_specification_wellformed(arg1, expression)

def TypeChecker_is_type_wellformed(arg1: 'TypeChecker_ptr', type: 'SymbType_ptr', varName: 'node_ptr') -> "boolean":
    """TypeChecker_is_type_wellformed(TypeChecker_ptr arg1, SymbType_ptr type, node_ptr varName) -> boolean"""
    return _type_checking.TypeChecker_is_type_wellformed(arg1, type, varName)

def TypeChecker_get_expression_type(arg1: 'TypeChecker_ptr', expression: 'node_ptr', context: 'node_ptr') -> "SymbType_ptr":
    """TypeChecker_get_expression_type(TypeChecker_ptr arg1, node_ptr expression, node_ptr context) -> SymbType_ptr"""
    return _type_checking.TypeChecker_get_expression_type(arg1, expression, context)

def TypeChecker_is_expression_type_checked(arg1: 'TypeChecker_ptr', expression: 'node_ptr', context: 'node_ptr') -> "boolean":
    """TypeChecker_is_expression_type_checked(TypeChecker_ptr arg1, node_ptr expression, node_ptr context) -> boolean"""
    return _type_checking.TypeChecker_is_expression_type_checked(arg1, expression, context)
# This file is compatible with both classic and new-style classes.


