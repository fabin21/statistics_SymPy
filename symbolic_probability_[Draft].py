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


def recursiveformula_for_momentum(current_momentum, previous_momentum, current_momentum_order):
    principalfactor_current_momentum = current_momentum / previous_momentum
    if current_momentum_order > 2:
        M_n = sp.Symbol(f"CM[{current_momentum_order - 1}]")
        return M_n * sp.simplify(principalfactor_current_momentum)
    else:
        return current_momentum


def recursiveformula_for_central_momentum(current_central_momentum, previous_central_momentum, current_central_momentum_order):
    principalfactor_current_central_momentum = current_central_momentum / previous_central_momentum
    if current_central_momentum_order > 2:
        CM_n = sp.Symbol(f"M[{current_central_momentum_order - 1}]")
        return CM_n * sp.simplify(principalfactor_current_central_momentum)
    else :
        return current_central_momentum


X = BernoulliVariable()
descriptive_statistics_dataframe = pd.DataFrame(columns = ["Distribution", "Order (n)", "Momentum (M[n])", "Recursive Formula for Momentum (M[n])", "Central Momentum (CM[n])", "Recursive Formula for Central Momentum CM[n])"])

for i in range(1, 100, 1):
    data_dict = dict()
    data_dict["Distribution"] = X.DistributionsName
    data_dict["Order (n)"] = i
    data_dict["Momentum (M[n])"] = momentum(X, i)
    data_dict["Central Momentum (CM[n])"] = central_momentum(X, i)
    if i > 1:
        data_dict["Recursive Formula for Momentum (M[n])"] = recursiveformula_for_momentum(
            current_momentum = data_dict["Momentum (M[n])"],
            previous_momentum = descriptive_statistics_dataframe.loc[i - 1, "Momentum (M[n])"],
            current_momentum_order = i)
        data_dict["Recursive Formula for Central Momentum CM[n])"] = recursiveformula_for_central_momentum(
            current_central_momentum = data_dict["Central Momentum (CM[n])"],
            previous_central_momentum = descriptive_statistics_dataframe.loc[i - 1, "Central Momentum (CM[n])"],
            current_central_momentum_order = i)
    else:
        data_dict["Recursive Formula for Momentum (M[n])"] = data_dict["Momentum (M[n])"]
        data_dict["Recursive Formula for Central Momentum CM[n])"] = data_dict["Central Momentum (CM[n])"]
    descriptive_statistics_dataframe.loc[i] = data_dict

# Defining the Output PathDir
folder_dir = "descriptive_statistics_dataframe_directory/"
archive_name = "descriptive_statistics_dataframe"
archive_extension = ".csv"

# Write the New CSV Archive
descriptive_statistics_dataframe.to_csv(
    path_or_buf = f"{folder_dir}{archive_name}{archive_extension}",
    header = True)
