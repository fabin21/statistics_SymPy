import sympy as sp


def adding(x: sp.Symbol, y: sp.Symbol):
    return sp.srepr(x + y)


def subtracting(x: sp.Symbol, y: sp.Symbol):
    return sp.srepr(x - y)


def power_operating(x: sp.Symbol, n: sp.Symbol):
    return sp.Pow(x, n)


def adding_Value_from_vector(x: sp.Matrix, value: sp.Symbol):
    y = list()
    for xi in x:
        y.append(xi + value)
    y = sp.Matrix(y)
    return y

def subtracting_Value_from_vector(x: sp.Matrix, value: sp.Symbol):
    y = list()
    for xi in x:
        y.append(xi - value)
    y = sp.Matrix(y)
    return y

def vectorsPower(x: sp.matrices.Matrix, n: sp.Symbol):
    y = list()
    for xi in x:
        print(xi)
        y.append(power_operating(xi, n))
    y = sp.Matrix(y)
    return y

