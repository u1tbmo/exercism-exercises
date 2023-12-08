from math import e, sin, cos, sqrt


class ComplexNumber:
    def __init__(self, real: int | float, imaginary: int | float):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        complex_other = (
            other if isinstance(other, ComplexNumber) else ComplexNumber(other, 0)
        )
        return ComplexNumber(
            self.real + complex_other.real, self.imaginary + complex_other.imaginary
        )

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        complex_other = (
            other if isinstance(other, ComplexNumber) else ComplexNumber(other, 0)
        )
        return ComplexNumber(
            self.real * complex_other.real - self.imaginary * complex_other.imaginary,
            self.real * complex_other.imaginary + self.imaginary * complex_other.real,
        )

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        complex_other = (
            other if isinstance(other, ComplexNumber) else ComplexNumber(other, 0)
        )
        return ComplexNumber(
            self.real - complex_other.real, self.imaginary - complex_other.imaginary
        )

    def __rsub__(self, other):
        complex_other = (
            other if isinstance(other, ComplexNumber) else ComplexNumber(other, 0)
        )
        return ComplexNumber(
            complex_other.real - self.real, complex_other.imaginary - self.imaginary
        )

    def __truediv__(self, other):
        complex_other = (
            other if isinstance(other, ComplexNumber) else ComplexNumber(other, 0)
        )
        denominator = complex_other.real**2 + complex_other.imaginary**2
        return ComplexNumber(
            (self.real * complex_other.real + self.imaginary * complex_other.imaginary)
            / denominator,
            (self.imaginary * complex_other.real - self.real * complex_other.imaginary)
            / denominator,
        )

    def __rtruediv__(self, other):
        complex_other = (
            other if isinstance(other, ComplexNumber) else ComplexNumber(other, 0)
        )
        denominator = self.real**2 + self.imaginary**2
        return ComplexNumber(
            (complex_other.real * self.real + complex_other.imaginary * self.imaginary)
            / denominator,
            (complex_other.imaginary * self.real - complex_other.real * self.imaginary)
            / denominator,
        )

    def __abs__(self):
        return sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(e**self.real, 0) * ComplexNumber(
            cos(self.imaginary), sin(self.imaginary)
        )
