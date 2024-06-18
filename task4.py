class A:
    def introduce(self):
        return 'Я клас А'

class B(A):
    def introduce(self):
        return 'Я клас B'

class C(A):
    def introduce(self):
        return 'Я клас C'

class D(B, C):
    pass


a_instance = A()
b_instance = B()
c_instance = C()
d_instance = D()       

print(a_instance.introduce())
print(b_instance.introduce())
print(c_instance.introduce())
print(d_instance.introduce())
print('MRO для D:', D.mro())


class B(A):
    pass

class D(B, C):
    pass


d_instance = D()
print(d_instance.introduce())
print('MRO для після зміни В:', D.mro())


class C(A):
    pass

class D(B, C):
    pass


d_instance = D()
print(d_instance.introduce())
print('MRO для D після зміни С:', D.mro())
