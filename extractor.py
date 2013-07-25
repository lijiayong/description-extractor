# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_extractor', [dirname(__file__)])
        except ImportError:
            import _extractor
            return _extractor
        if fp is not None:
            try:
                _mod = imp.load_module('_extractor', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _extractor = swig_import_helper()
    del swig_import_helper
else:
    import _extractor
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _extractor.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _extractor.SwigPyIterator_value(self)
    def incr(self, n = 1): return _extractor.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _extractor.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _extractor.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _extractor.SwigPyIterator_equal(self, *args)
    def copy(self): return _extractor.SwigPyIterator_copy(self)
    def next(self): return _extractor.SwigPyIterator_next(self)
    def __next__(self): return _extractor.SwigPyIterator___next__(self)
    def previous(self): return _extractor.SwigPyIterator_previous(self)
    def advance(self, *args): return _extractor.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _extractor.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _extractor.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _extractor.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _extractor.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _extractor.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _extractor.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _extractor.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class VariantVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VariantVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VariantVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _extractor.VariantVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _extractor.VariantVector___nonzero__(self)
    def __bool__(self): return _extractor.VariantVector___bool__(self)
    def __len__(self): return _extractor.VariantVector___len__(self)
    def pop(self): return _extractor.VariantVector_pop(self)
    def __getslice__(self, *args): return _extractor.VariantVector___getslice__(self, *args)
    def __setslice__(self, *args): return _extractor.VariantVector___setslice__(self, *args)
    def __delslice__(self, *args): return _extractor.VariantVector___delslice__(self, *args)
    def __delitem__(self, *args): return _extractor.VariantVector___delitem__(self, *args)
    def __getitem__(self, *args): return _extractor.VariantVector___getitem__(self, *args)
    def __setitem__(self, *args): return _extractor.VariantVector___setitem__(self, *args)
    def append(self, *args): return _extractor.VariantVector_append(self, *args)
    def empty(self): return _extractor.VariantVector_empty(self)
    def size(self): return _extractor.VariantVector_size(self)
    def clear(self): return _extractor.VariantVector_clear(self)
    def swap(self, *args): return _extractor.VariantVector_swap(self, *args)
    def get_allocator(self): return _extractor.VariantVector_get_allocator(self)
    def begin(self): return _extractor.VariantVector_begin(self)
    def end(self): return _extractor.VariantVector_end(self)
    def rbegin(self): return _extractor.VariantVector_rbegin(self)
    def rend(self): return _extractor.VariantVector_rend(self)
    def pop_back(self): return _extractor.VariantVector_pop_back(self)
    def erase(self, *args): return _extractor.VariantVector_erase(self, *args)
    def __init__(self, *args): 
        this = _extractor.new_VariantVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _extractor.VariantVector_push_back(self, *args)
    def front(self): return _extractor.VariantVector_front(self)
    def back(self): return _extractor.VariantVector_back(self)
    def assign(self, *args): return _extractor.VariantVector_assign(self, *args)
    def resize(self, *args): return _extractor.VariantVector_resize(self, *args)
    def insert(self, *args): return _extractor.VariantVector_insert(self, *args)
    def reserve(self, *args): return _extractor.VariantVector_reserve(self, *args)
    def capacity(self): return _extractor.VariantVector_capacity(self)
    __swig_destroy__ = _extractor.delete_VariantVector
    __del__ = lambda self : None;
VariantVector_swigregister = _extractor.VariantVector_swigregister
VariantVector_swigregister(VariantVector)

class SubstringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SubstringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SubstringVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _extractor.SubstringVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _extractor.SubstringVector___nonzero__(self)
    def __bool__(self): return _extractor.SubstringVector___bool__(self)
    def __len__(self): return _extractor.SubstringVector___len__(self)
    def pop(self): return _extractor.SubstringVector_pop(self)
    def __getslice__(self, *args): return _extractor.SubstringVector___getslice__(self, *args)
    def __setslice__(self, *args): return _extractor.SubstringVector___setslice__(self, *args)
    def __delslice__(self, *args): return _extractor.SubstringVector___delslice__(self, *args)
    def __delitem__(self, *args): return _extractor.SubstringVector___delitem__(self, *args)
    def __getitem__(self, *args): return _extractor.SubstringVector___getitem__(self, *args)
    def __setitem__(self, *args): return _extractor.SubstringVector___setitem__(self, *args)
    def append(self, *args): return _extractor.SubstringVector_append(self, *args)
    def empty(self): return _extractor.SubstringVector_empty(self)
    def size(self): return _extractor.SubstringVector_size(self)
    def clear(self): return _extractor.SubstringVector_clear(self)
    def swap(self, *args): return _extractor.SubstringVector_swap(self, *args)
    def get_allocator(self): return _extractor.SubstringVector_get_allocator(self)
    def begin(self): return _extractor.SubstringVector_begin(self)
    def end(self): return _extractor.SubstringVector_end(self)
    def rbegin(self): return _extractor.SubstringVector_rbegin(self)
    def rend(self): return _extractor.SubstringVector_rend(self)
    def pop_back(self): return _extractor.SubstringVector_pop_back(self)
    def erase(self, *args): return _extractor.SubstringVector_erase(self, *args)
    def __init__(self, *args): 
        this = _extractor.new_SubstringVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _extractor.SubstringVector_push_back(self, *args)
    def front(self): return _extractor.SubstringVector_front(self)
    def back(self): return _extractor.SubstringVector_back(self)
    def assign(self, *args): return _extractor.SubstringVector_assign(self, *args)
    def resize(self, *args): return _extractor.SubstringVector_resize(self, *args)
    def insert(self, *args): return _extractor.SubstringVector_insert(self, *args)
    def reserve(self, *args): return _extractor.SubstringVector_reserve(self, *args)
    def capacity(self): return _extractor.SubstringVector_capacity(self)
    __swig_destroy__ = _extractor.delete_SubstringVector
    __del__ = lambda self : None;
SubstringVector_swigregister = _extractor.SubstringVector_swigregister
SubstringVector_swigregister(SubstringVector)

class Variant(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Variant, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Variant, name)
    __repr__ = _swig_repr
    __swig_setmethods__["reference_start"] = _extractor.Variant_reference_start_set
    __swig_getmethods__["reference_start"] = _extractor.Variant_reference_start_get
    if _newclass:reference_start = _swig_property(_extractor.Variant_reference_start_get, _extractor.Variant_reference_start_set)
    __swig_setmethods__["reference_end"] = _extractor.Variant_reference_end_set
    __swig_getmethods__["reference_end"] = _extractor.Variant_reference_end_get
    if _newclass:reference_end = _swig_property(_extractor.Variant_reference_end_get, _extractor.Variant_reference_end_set)
    __swig_setmethods__["sample_start"] = _extractor.Variant_sample_start_set
    __swig_getmethods__["sample_start"] = _extractor.Variant_sample_start_get
    if _newclass:sample_start = _swig_property(_extractor.Variant_sample_start_get, _extractor.Variant_sample_start_set)
    __swig_setmethods__["sample_end"] = _extractor.Variant_sample_end_set
    __swig_getmethods__["sample_end"] = _extractor.Variant_sample_end_get
    if _newclass:sample_end = _swig_property(_extractor.Variant_sample_end_get, _extractor.Variant_sample_end_set)
    __swig_setmethods__["reverse_complement"] = _extractor.Variant_reverse_complement_set
    __swig_getmethods__["reverse_complement"] = _extractor.Variant_reverse_complement_get
    if _newclass:reverse_complement = _swig_property(_extractor.Variant_reverse_complement_get, _extractor.Variant_reverse_complement_set)
    def __init__(self): 
        this = _extractor.new_Variant()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _extractor.delete_Variant
    __del__ = lambda self : None;
Variant_swigregister = _extractor.Variant_swigregister
Variant_swigregister(Variant)


def extractor(*args):
  return _extractor.extractor(*args)
extractor = _extractor.extractor
class Substring(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Substring, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Substring, name)
    __repr__ = _swig_repr
    __swig_setmethods__["reference_index"] = _extractor.Substring_reference_index_set
    __swig_getmethods__["reference_index"] = _extractor.Substring_reference_index_get
    if _newclass:reference_index = _swig_property(_extractor.Substring_reference_index_get, _extractor.Substring_reference_index_set)
    __swig_setmethods__["sample_index"] = _extractor.Substring_sample_index_set
    __swig_getmethods__["sample_index"] = _extractor.Substring_sample_index_get
    if _newclass:sample_index = _swig_property(_extractor.Substring_sample_index_get, _extractor.Substring_sample_index_set)
    __swig_setmethods__["length"] = _extractor.Substring_length_set
    __swig_getmethods__["length"] = _extractor.Substring_length_get
    if _newclass:length = _swig_property(_extractor.Substring_length_get, _extractor.Substring_length_set)
    __swig_setmethods__["reverse_complement"] = _extractor.Substring_reverse_complement_set
    __swig_getmethods__["reverse_complement"] = _extractor.Substring_reverse_complement_get
    if _newclass:reverse_complement = _swig_property(_extractor.Substring_reverse_complement_get, _extractor.Substring_reverse_complement_set)
    def __init__(self): 
        this = _extractor.new_Substring()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _extractor.delete_Substring
    __del__ = lambda self : None;
Substring_swigregister = _extractor.Substring_swigregister
Substring_swigregister(Substring)

def extract(*args):
  return _extractor.extract(*args)
extract = _extractor.extract


def LCS_1(*args):
  return _extractor.LCS_1(*args)
LCS_1 = _extractor.LCS_1

def LCS_k(*args):
  return _extractor.LCS_k(*args)
LCS_k = _extractor.LCS_k

def LCS(*args):
  return _extractor.LCS(*args)
LCS = _extractor.LCS


def IUPAC_complement(*args):
  return _extractor.IUPAC_complement(*args)
IUPAC_complement = _extractor.IUPAC_complement

