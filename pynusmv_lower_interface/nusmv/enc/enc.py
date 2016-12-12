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
        mname = '.'.join((pkg, '_enc')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_enc')
    _enc = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_enc', [dirname(__file__)])
        except ImportError:
            import _enc
            return _enc
        if fp is not None:
            try:
                _mod = imp.load_module('_enc', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _enc = swig_import_helper()
    del swig_import_helper
else:
    import _enc
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

PRIuPTR = _enc.PRIuPTR
PRIdPTR = _enc.PRIdPTR
LLU = _enc.LLU
LLO = _enc.LLO
LLX = _enc.LLX
false = _enc.false
true = _enc.true
OUTCOME_GENERIC_ERROR = _enc.OUTCOME_GENERIC_ERROR
OUTCOME_PARSER_ERROR = _enc.OUTCOME_PARSER_ERROR
OUTCOME_SYNTAX_ERROR = _enc.OUTCOME_SYNTAX_ERROR
OUTCOME_FILE_ERROR = _enc.OUTCOME_FILE_ERROR
OUTCOME_SUCCESS_REQUIRED_HELP = _enc.OUTCOME_SUCCESS_REQUIRED_HELP
OUTCOME_SUCCESS = _enc.OUTCOME_SUCCESS
VARS_ORD_INPUTS_BEFORE = _enc.VARS_ORD_INPUTS_BEFORE
VARS_ORD_INPUTS_AFTER = _enc.VARS_ORD_INPUTS_AFTER
VARS_ORD_TOPOLOGICAL = _enc.VARS_ORD_TOPOLOGICAL
VARS_ORD_INPUTS_BEFORE_BI = _enc.VARS_ORD_INPUTS_BEFORE_BI
VARS_ORD_INPUTS_AFTER_BI = _enc.VARS_ORD_INPUTS_AFTER_BI
VARS_ORD_TOPOLOGICAL_BI = _enc.VARS_ORD_TOPOLOGICAL_BI
VARS_ORD_UNKNOWN = _enc.VARS_ORD_UNKNOWN
BDD_STATIC_ORDER_HEURISTICS_NONE = _enc.BDD_STATIC_ORDER_HEURISTICS_NONE
BDD_STATIC_ORDER_HEURISTICS_BASIC = _enc.BDD_STATIC_ORDER_HEURISTICS_BASIC
BDD_STATIC_ORDER_HEURISTICS_ERROR = _enc.BDD_STATIC_ORDER_HEURISTICS_ERROR

def Enc_init_encodings() -> "void":
    """Enc_init_encodings()"""
    return _enc.Enc_init_encodings()

def Enc_init_bool_encoding() -> "void":
    """Enc_init_bool_encoding()"""
    return _enc.Enc_init_bool_encoding()

def Enc_init_bdd_encoding() -> "void":
    """Enc_init_bdd_encoding()"""
    return _enc.Enc_init_bdd_encoding()

def Enc_init_be_encoding() -> "void":
    """Enc_init_be_encoding()"""
    return _enc.Enc_init_be_encoding()

def Enc_quit_encodings() -> "void":
    """Enc_quit_encodings()"""
    return _enc.Enc_quit_encodings()

def Enc_add_commands() -> "void":
    """Enc_add_commands()"""
    return _enc.Enc_add_commands()

def Enc_get_bool_encoding() -> "BoolEnc_ptr":
    """Enc_get_bool_encoding() -> BoolEnc_ptr"""
    return _enc.Enc_get_bool_encoding()

def Enc_get_bdd_encoding() -> "BddEnc_ptr":
    """Enc_get_bdd_encoding() -> BddEnc_ptr"""
    return _enc.Enc_get_bdd_encoding()

def Enc_get_be_encoding() -> "BeEnc_ptr":
    """Enc_get_be_encoding() -> BeEnc_ptr"""
    return _enc.Enc_get_be_encoding()

def Enc_set_bool_encoding(benc: 'BoolEnc_ptr') -> "void":
    """Enc_set_bool_encoding(BoolEnc_ptr benc)"""
    return _enc.Enc_set_bool_encoding(benc)

def Enc_set_bdd_encoding(enc: 'BddEnc_ptr') -> "void":
    """Enc_set_bdd_encoding(BddEnc_ptr enc)"""
    return _enc.Enc_set_bdd_encoding(enc)

def Enc_set_be_encoding(enc: 'BeEnc_ptr') -> "void":
    """Enc_set_be_encoding(BeEnc_ptr enc)"""
    return _enc.Enc_set_be_encoding(enc)

def Enc_vars_ord_to_string(arg1: 'VarsOrdType') -> "char const *":
    """Enc_vars_ord_to_string(VarsOrdType arg1) -> char const *"""
    return _enc.Enc_vars_ord_to_string(arg1)

def Enc_string_to_vars_ord(arg1: 'char const *') -> "VarsOrdType":
    """Enc_string_to_vars_ord(char const * arg1) -> VarsOrdType"""
    return _enc.Enc_string_to_vars_ord(arg1)

def Enc_get_valid_vars_ord_types() -> "char const *":
    """Enc_get_valid_vars_ord_types() -> char const *"""
    return _enc.Enc_get_valid_vars_ord_types()

def Enc_bdd_static_order_heuristics_to_string(arg1: 'BddSohEnum') -> "char const *":
    """Enc_bdd_static_order_heuristics_to_string(BddSohEnum arg1) -> char const *"""
    return _enc.Enc_bdd_static_order_heuristics_to_string(arg1)

def Enc_string_to_bdd_static_order_heuristics(arg1: 'char const *') -> "BddSohEnum":
    """Enc_string_to_bdd_static_order_heuristics(char const * arg1) -> BddSohEnum"""
    return _enc.Enc_string_to_bdd_static_order_heuristics(arg1)

def Enc_get_valid_bdd_static_order_heuristics() -> "char const *":
    """Enc_get_valid_bdd_static_order_heuristics() -> char const *"""
    return _enc.Enc_get_valid_bdd_static_order_heuristics()

def node_and(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_and(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_and(n1, n2)

def node_or(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_or(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_or(n1, n2)

def node_not(n: 'node_ptr', this_node_not_used: 'node_ptr') -> "node_ptr":
    """node_not(node_ptr n, node_ptr this_node_not_used) -> node_ptr"""
    return _enc.node_not(n, this_node_not_used)

def node_iff(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_iff(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_iff(n1, n2)

def node_xor(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_xor(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_xor(n1, n2)

def node_implies(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_implies(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_implies(n1, n2)

def node_equal(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_equal(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_equal(n1, n2)

def node_not_equal(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_not_equal(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_not_equal(n1, n2)

def node_lt(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_lt(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_lt(n1, n2)

def node_gt(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_gt(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_gt(n1, n2)

def node_le(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_le(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_le(n1, n2)

def node_ge(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_ge(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_ge(n1, n2)

def node_unary_minus(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_unary_minus(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_unary_minus(n1, n2)

def node_plus(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_plus(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_plus(n1, n2)

def node_minus(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_minus(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_minus(n1, n2)

def node_times(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_times(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_times(n1, n2)

def node_divide(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_divide(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_divide(n1, n2)

def node_mod(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_mod(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_mod(n1, n2)

def node_bit_range(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_bit_range(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_bit_range(n1, n2)

def node_union(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_union(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_union(n1, n2)

def node_setin(n1: 'node_ptr', n2: 'node_ptr') -> "node_ptr":
    """node_setin(node_ptr n1, node_ptr n2) -> node_ptr"""
    return _enc.node_setin(n1, n2)

def node_word_get_width(w: 'node_ptr') -> "size_t":
    """node_word_get_width(node_ptr w) -> size_t"""
    return _enc.node_word_get_width(w)

def node_word_create(bitval: 'node_ptr', w: 'size_t') -> "node_ptr":
    """node_word_create(node_ptr bitval, size_t w) -> node_ptr"""
    return _enc.node_word_create(bitval, w)

def node_word_create_from_list(l: 'node_ptr', w: 'size_t') -> "node_ptr":
    """node_word_create_from_list(node_ptr l, size_t w) -> node_ptr"""
    return _enc.node_word_create_from_list(l, w)

def node_word_create_from_wordnumber(wn: 'WordNumber_ptr') -> "node_ptr":
    """node_word_create_from_wordnumber(WordNumber_ptr wn) -> node_ptr"""
    return _enc.node_word_create_from_wordnumber(wn)

def node_word_create_from_integer(value: 'unsigned long long', width: 'size_t') -> "node_ptr":
    """node_word_create_from_integer(unsigned long long value, size_t width) -> node_ptr"""
    return _enc.node_word_create_from_integer(value, width)

def node_word_create_from_array(arr: 'array_t *') -> "node_ptr":
    """node_word_create_from_array(array_t * arr) -> node_ptr"""
    return _enc.node_word_create_from_array(arr)

def node_word_to_array(w: 'node_ptr') -> "array_t *":
    """node_word_to_array(node_ptr w) -> array_t *"""
    return _enc.node_word_to_array(w)

def node_word_apply_unary(wenc: 'node_ptr', op: 'int') -> "node_ptr":
    """node_word_apply_unary(node_ptr wenc, int op) -> node_ptr"""
    return _enc.node_word_apply_unary(wenc, op)

def node_word_apply_attime(wenc: 'node_ptr', time: 'int') -> "node_ptr":
    """node_word_apply_attime(node_ptr wenc, int time) -> node_ptr"""
    return _enc.node_word_apply_attime(wenc, time)

def node_word_apply_binary(wenc1: 'node_ptr', wenc2: 'node_ptr', op: 'int') -> "node_ptr":
    """node_word_apply_binary(node_ptr wenc1, node_ptr wenc2, int op) -> node_ptr"""
    return _enc.node_word_apply_binary(wenc1, wenc2, op)

def node_word_make_conjuction(w: 'node_ptr') -> "node_ptr":
    """node_word_make_conjuction(node_ptr w) -> node_ptr"""
    return _enc.node_word_make_conjuction(w)

def node_word_make_disjunction(w: 'node_ptr') -> "node_ptr":
    """node_word_make_disjunction(node_ptr w) -> node_ptr"""
    return _enc.node_word_make_disjunction(w)

def node_word_cast_bool(w: 'node_ptr') -> "node_ptr":
    """node_word_cast_bool(node_ptr w) -> node_ptr"""
    return _enc.node_word_cast_bool(w)

def node_word_not(w: 'node_ptr') -> "node_ptr":
    """node_word_not(node_ptr w) -> node_ptr"""
    return _enc.node_word_not(w)

def node_word_and(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_and(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_and(a, b)

def node_word_or(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_or(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_or(a, b)

def node_word_xor(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_xor(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_xor(a, b)

def node_word_xnor(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_xnor(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_xnor(a, b)

def node_word_implies(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_implies(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_implies(a, b)

def node_word_iff(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_iff(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_iff(a, b)

def node_word_equal(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_equal(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_equal(a, b)

def node_word_notequal(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_notequal(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_notequal(a, b)

def node_word_concat(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_concat(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_concat(a, b)

def node_word_selection(word: 'node_ptr', range: 'node_ptr') -> "node_ptr":
    """node_word_selection(node_ptr word, node_ptr range) -> node_ptr"""
    return _enc.node_word_selection(word, range)

def node_word_extend(a: 'node_ptr', b: 'node_ptr', isSigned: 'boolean') -> "node_ptr":
    """node_word_extend(node_ptr a, node_ptr b, boolean isSigned) -> node_ptr"""
    return _enc.node_word_extend(a, b, isSigned)

def node_word_adder(a: 'node_ptr', b: 'node_ptr', carry_in: 'node_ptr', carry_out: 'node_ptr *') -> "node_ptr":
    """node_word_adder(node_ptr a, node_ptr b, node_ptr carry_in, node_ptr * carry_out) -> node_ptr"""
    return _enc.node_word_adder(a, b, carry_in, carry_out)

def node_word_plus(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_plus(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_plus(a, b)

def node_word_minus(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_minus(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_minus(a, b)

def node_word_uminus(a: 'node_ptr') -> "node_ptr":
    """node_word_uminus(node_ptr a) -> node_ptr"""
    return _enc.node_word_uminus(a)

def node_word_times(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_times(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_times(a, b)

def node_word_unsigned_divide(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_unsigned_divide(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_unsigned_divide(a, b)

def node_word_unsigned_mod(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_unsigned_mod(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_unsigned_mod(a, b)

def node_word_signed_divide(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_signed_divide(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_signed_divide(a, b)

def node_word_signed_mod(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_signed_mod(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_signed_mod(a, b)

def node_word_unsigned_less(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_unsigned_less(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_unsigned_less(a, b)

def node_word_unsigned_less_equal(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_unsigned_less_equal(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_unsigned_less_equal(a, b)

def node_word_unsigned_greater(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_unsigned_greater(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_unsigned_greater(a, b)

def node_word_unsigned_greater_equal(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_unsigned_greater_equal(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_unsigned_greater_equal(a, b)

def node_word_signed_less(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_signed_less(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_signed_less(a, b)

def node_word_signed_less_equal(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_signed_less_equal(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_signed_less_equal(a, b)

def node_word_signed_greater(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_signed_greater(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_signed_greater(a, b)

def node_word_signed_greater_equal(a: 'node_ptr', b: 'node_ptr') -> "node_ptr":
    """node_word_signed_greater_equal(node_ptr a, node_ptr b) -> node_ptr"""
    return _enc.node_word_signed_greater_equal(a, b)
# This file is compatible with both classic and new-style classes.

cvar = _enc.cvar

