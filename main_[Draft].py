import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt


def main():
    pass


def plot_graphics(f_prime):
    x = sp.symbols('x')
    xs = range(100)
    ys = []
    for i in xs:
        f_prime_at_3 = f_prime.subs(x, i)

        value_at_3 = f_prime_at_3.evalf()
        ys.append(value_at_3)
        # print(value_at_3)

    plt.plot(xs, ys)

    plt.title(f_prime)
    plt.xlabel("Delay")
    plt.ylabel("Subject Value")

    plt.show()


if __name__ == '__main__':
    main()

