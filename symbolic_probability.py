import numpy as np
import sympy as sp
import pandas as pd

from SymPy_DLC_Functions import adding
from SymPy_DLC_Functions import subtracting
from SymPy_DLC_Functions import subtracting_Value_from_vector
from SymPy_DLC_Functions import adding_Value_from_vector
from SymPy_DLC_Functions import vectorsPower


def SymPy_Apply(x: sp.matrices.Matrix, f):
    xn = list()
    for xi in x:
        xn.append(f(xi))
    xn = sp.matrices.Matrix(xn)
    return xn

class BernoulliVariable:
    def __init__(self):
        self.DistributionsName = "Bernoulli"
        self.ValuesMatrice = sp.matrices.Matrix([0, 1])
        self.ProbabilitysMatrice = sp.matrices.Matrix([1 - sp.Symbol(name= "p"),sp.Symbol(name= "p")])


def momentum(variable, momentums_order: int):
    x = variable.ValuesMatrice
    n = sp.Integer(momentums_order)
    x_n = vectorsPower(x, n)

    p = variable.ProbabilitysMatrice
    return x_n.dot(p)


def central_momentum(variable, centralmomentums_order):
    x = variable.ValuesMatrice
    Ex = momentum(variable = variable, momentums_order = 1)

    def subtracting_Ex(number):
        return number - Ex

    dx = SymPy_Apply(x, subtracting_Ex)

    n = sp.Integer(centralmomentums_order)
    p = variable.ProbabilitysMatrice
    dx_n = vectorsPower(dx, n)

    E_dx2 = dx_n.dot(p)
    E_dx2 = sp.simplify(E_dx2)

    return E_dx2


X = BernoulliVariable()
descriptive_statistics_dataframe = pd.DataFrame(columns = ["Distribution", "Order", "Momentum", "Central-Momentum"])

for i in range(1, 100, 1):
    data_dict = dict()
    data_dict["Distribution"] = X.DistributionsName
    data_dict["Order"] = i
    data_dict["Momentum"] = momentum(X, i)
    data_dict["Central-Momentum"] = central_momentum(X, i)
    descriptive_statistics_dataframe.loc[i] = data_dict
    print(descriptive_statistics_dataframe)

print(descriptive_statistics_dataframe)
descriptive_statistics_dataframe.to_csv(path_or_buf = "descriptive_statistics_dataframe_directory/descriptive_statistics_dataframe.csv", header = True)
