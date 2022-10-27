import scipy.optimize as minimize


def f(x):
    return (x - 3) ** 2


res = minimize(f, 2)

print(res)
print(res.x)
print(res.x[0])

f = lambda x: (x[0] - 1) ** 2 + (x[1] - 2.5) ** 2

cons = (
    {"type": "ineq", "fun": lambda x: x[0] - 2 * x[1] + 2},
    {"type": "ineq", "fun": lambda x: -x[0] - 2 * x[1] + 6},
    {"type": "ineq", "fun": lambda x: -x[0] + 2 * x[1] + 2},
)

bnds = ((0, None), (0, None))
res = minimize(f, (2, 0), bounds=bnds, constrains=cons)
print(res)
