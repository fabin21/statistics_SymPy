# ----------------------------------------------------------------------------------------------- #
# External Modules Import
import sympy as sp
import pandas as pd

# Internal Scripts Import
from SymPy_DLC_Functions import vectorsPower
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
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
        self.ProbabilitysMatrice = sp.matrices.Matrix(
            [1 - sp.Symbol(name= "p"), sp.Symbol(name= "p")]
        )


def momentum(variable, momentums_order: int):
    x = variable.ValuesMatrice
    n = sp.Integer(momentums_order)
    x_n = vectorsPower(x, n)

    p = variable.ProbabilitysMatrice
    return x_n.dot(p)


def recursiveformula_for_momentum(current_momentum, previous_momentum, current_momentum_order):
    principalfactor_current_momentum = current_momentum / previous_momentum
    if current_momentum_order > 2:
        M_n = sp.Symbol(f"CM[{current_momentum_order - 1}]")
        return M_n * sp.simplify(principalfactor_current_momentum)
    else:
        return current_momentum


def Bernoulli_Momentus_Analysis_exe():
    X = BernoulliVariable()
    Bernoulli_Momentus_Analysis = pd.DataFrame(
        columns = [
            "Distribution",
            "Order (n)",
            "Momentum (M[n])",
            "Recursive Formula for Momentum (M[n])"
        ]
    )

    for i in range(1, 100, 1):
        print(f"Momentus: {i}")
        data_dict = dict()
        data_dict["Distribution"] = X.DistributionsName
        data_dict["Order (n)"] = i
        data_dict["Momentum (M[n])"] = momentum(X, i)
        if i > 1:
            data_dict["Recursive Formula for Momentum (M[n])"] = recursiveformula_for_momentum(
                current_momentum = data_dict["Momentum (M[n])"],
                previous_momentum = Bernoulli_Momentus_Analysis.loc[i - 1, "Momentum (M[n])"],
                current_momentum_order = i)
        else:
            data_dict["Recursive Formula for Momentum (M[n])"] = data_dict["Momentum (M[n])"]
        Bernoulli_Momentus_Analysis.loc[i] = data_dict
    return Bernoulli_Momentus_Analysis

