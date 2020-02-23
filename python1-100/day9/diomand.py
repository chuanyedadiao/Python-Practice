class A(object):

    def foo(self):
        print('foo of A')


class B(A):
    
    def foo(self):
        print('foo fo B')


class C(B):

    def foo(self):
        print('foo fo C')

class D(C):
    def foo(self):
        print('foo fo D')


class E(D):

    def foo(self):
        #print('foo in E')
        #super().foo()
        #super(B, self).foo()
        super(C, self).foo()


if __name__ == '__main__':
    #d = D()
    #d.foo()
    e = E()
    e.foo()
