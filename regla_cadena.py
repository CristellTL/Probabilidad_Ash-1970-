# -*- coding: utf-8 -*-
"""Regla_cadena.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pELS-YdS98dHPhd_pD9MQQLGCDMYqsH-

## **Regla de la cadena**

***Presenta: Vanessa Cristell Torres López***
"""

# Definimos las probabilidades de eventos y eventos condicionales
def P(event):
    # Definimos un diccionario con las probabilidades
    probabilities = {
        'A1': 0.4,                # P(A1)
        'A2_given_A1': 0.6,       # P(A2 | A1)
        'A3_given_A1_and_A2': 0.5 # P(A3 | A1 ∩ A2)
    }
    return probabilities.get(event, 0)

# Calcula la probabilidad conjunta usando la regla de la cadena
def joint_probability():
    P_A1 = P('A1')
    P_A2_given_A1 = P('A2_given_A1')
    P_A3_given_A1_and_A2 = P('A3_given_A1_and_A2')

    P_A1_and_A2_and_A3 = P_A1 * P_A2_given_A1 * P_A3_given_A1_and_A2

    return P_A1_and_A2_and_A3

# Ejecutar el cálculo
probabilidad_conjunta = joint_probability()

# Resultados
print(f"P(A1) = {P('A1')}")
print(f"P(A2 | A1) = {P('A2_given_A1')}")
print(f"P(A3 | A1 ∩ A2) = {P('A3_given_A1_and_A2')}")
print(f"P(A1 ∩ A2 ∩ A3) (calculado usando la regla de la cadena) = {probabilidad_conjunta}")