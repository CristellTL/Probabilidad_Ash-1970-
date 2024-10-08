# -*- coding: utf-8 -*-
"""Regla_suma.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UzJkFRaJqbjRZ7Pt1i623FmdWGgmCtgw

## **Regla de la suma**

***Presenta: Vanessa Cristell Torres López***
"""

# Definimos el espacio muestral
Omega = {1, 2, 3, 4, 5, 6}

# Definimos una función de probabilidad P para eventos en el espacio muestral
def P(event):
    probabilities = {
        frozenset(): 0,               # P(conjunto vacío) = 0
        frozenset({1}): 1/6,          # P({1}) = 1/6
        frozenset({2}): 1/6,          # P({2}) = 1/6
        frozenset({3}): 1/6,          # P({3}) = 1/6
        frozenset({4}): 1/6,          # P({4}) = 1/6
        frozenset({5}): 1/6,          # P({5}) = 1/6
        frozenset({6}): 1/6,          # P({6}) = 1/6
        frozenset({1, 2}): 1/3,      # P({1, 2}) = 1/3 (ejemplo)
        frozenset({3, 4}): 1/3,      # P({3, 4}) = 1/3 (ejemplo)
        frozenset({5, 6}): 1/3,      # P({5, 6}) = 1/3 (ejemplo)
        frozenset(Omega): 1          # P(Omega) = 1
    }
    return probabilities.get(frozenset(event), 0)

# Define los eventos
A = {1, 2}
B = {2, 4}

# Calculamos las probabilidades
P_A = P(A)
P_B = P(B)
P_A_inter_B = P(A.intersection(B))

# Aplicamos la regla de la suma
P_A_union_B = P_A + P_B - P_A_inter_B

# Resultados
print(f"P(A) = {P_A}")
print(f"P(B) = {P_B}")
print(f"P(A ∩ B) = {P_A_inter_B}")
print(f"P(A ∪ B) (calculado usando la regla de la suma) = {P_A_union_B}")