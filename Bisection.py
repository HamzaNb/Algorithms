def func(x):
    return x ** 2 + 1 - x


def bisection(a, b, eps):
    a_k = a
    b_k = b

    for i in range(10):
        Lambda = (a_k + b_k) / 2 - eps
        mu = (a_k + b_k) / 2 + eps
        print("Lambda ==>", Lambda)
        print("mu ==>", mu)

        if func(Lambda) <= func(mu):
            b_k = mu

        if func(Lambda) > func(mu):
            a_k = Lambda

        if (b_k - a_k) <= 0.1:
            break

    return a_k, b_k

#  [a,b]
a = -4
b = 7
a, b = bisection(a, b, 0.01)
print("Alpha star", a + (b - a) / 2)
