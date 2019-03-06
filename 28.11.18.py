from timeit import timeit
import numpy as np


def kwadrat():
    N = 1000
    wynik = [i**2 for i in range(1, N+1)]
    return wynik


def kwadrat1():
    N = 10000
    wynik = []
    for i in range(1, N+1):
        wynik.append(i**2)
    return wynik


np.sin(0.25 * np.pi)**2
tab1 = np.array([1/2.1/3, 1])
tab2 = np.array([1, 2, 3], dtype=float)
print(tab2.dtype)
tab3 = np.array([[1, 2, 3, 45],
                [3, 4, 345, 456],
                 [234, 456, 567, 456]])

print(tab3.shape)
print(tab3[1, 2])
print(tab3[:, 0:2])
dzielenie = tab3 % 3 == 0
print(dzielenie.dtype)
print(dzielenie)
tab3[tab3 % 3 == 0] = 100
print(tab3)
np.zeros((10, 5, 3))
tab4 = np.ones((4, 3, 5))
print(tab4)
tab5 = np.arange(0.5, 10.0, 0.5)
print(tab5)
tab6 = np.linspace(0., 2., 11)
print(tab6)
tab7 = 2 * np.random.rand(5, 5) - 1
print(tab7)
tab7 * np.eye(5)
m1 = np.matrix(tab7)
m2 = np.matrix(np.eye(5))
print(m1*m2)
m1**(-1)

A = np.matrix([[1,2],
               [4,3]])
B = np.array([9,8])
print(np.linalg.solve(A,B))