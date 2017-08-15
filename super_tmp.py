#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: super_tmp.py
@time: 2017/8/15 9:48
"""

"""
 super(type[, object-or-type])
  Return the superclass of type. If the second argument is omitted the super object
  returned is unbound. If the second argument is an object, isinstance(obj, type)
  must be true. If the second argument is a type, issubclass(type2, type) must be
  true. super() only works for new-style classes.
  A typical use for calling a cooperative superclass method is:
   class C(B):
       def meth(self, arg):
           super(C, self).meth(arg)

    super 只能用于2之后， 2之后3之前，必须是新式类调用 （需要显示继承object类），
    3之后， 便不用显示继承object类， 会自动继承object类
"""

class A(object):
    def __init__(self):
        print 'this is parent A'

    def test(self):
        print 'test A'

    def test_a(self):
        print 'test_a A'

class B(A):
    def __init__(self):
        print 'this is child B'
        super(B, self).__init__()

    def test(self):
        print 'test B'

b = B()
b.test()
b.test_a()