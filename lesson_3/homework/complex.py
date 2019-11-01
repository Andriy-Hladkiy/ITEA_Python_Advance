class ComplexInt():
    def __init__(self, n):
        self.n = n

    def __add__(self, cInt):
        return ComplexInt(self.n + cInt.n)

    def __sub__(self, cInt):
        return ComplexInt(self.n - cInt.n)

    def __mul__(self, cInt):
        return ComplexInt(self.n * cInt.n)

    def __truediv__(self, cInt):
        return ComplexInt(self.n / cInt.n)

    def __abs__(self):
        return ComplexInt(abs(self.n))

    def __pow__(self, y):
        return ComplexInt(self.n ** y)

    def __str__(self):
        return str(self.n)


A = []
C = []

for i in range(1, 10):
    obj = ComplexInt(i + i * 1j)
    new_element = obj.n
    A.append(new_element)
print(A)

for i in range(len(A)):
    if i == 0:
        C.append(abs(A[i + 1]))
    elif i == (len(A) - 1):
        C.append(abs(A[i - 1]))
    else:
        C.append(abs(A[i - 1] + A[i + 1]))

print(C)
