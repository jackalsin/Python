class A(object):
    # @staticmethod
    def f(x):
        return 10*x

print(A.f(42)) # 420 (called A.f without creating an instance of A)
