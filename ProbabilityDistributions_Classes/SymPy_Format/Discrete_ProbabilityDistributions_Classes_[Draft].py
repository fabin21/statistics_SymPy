import sympy as sp

class BernoulliVariable:
    def __init__(self):
        self.DistributionsName = "Bernoulli"
        self.ValuesMatrice = sp.matrices.Matrix([0, 1])
        self.ProbabilitysMatrice = sp.matrices.Matrix(
            [1 - sp.Symbol(name= "p"), sp.Symbol(name= "p")]
        )
