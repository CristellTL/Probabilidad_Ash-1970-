# -*- coding: utf-8 -*-
"""Regla_Bayes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Uyumaznc2AqtBX2jeCcrOSvkKAAjm89j

## **Verificar a través de un ejemplo la regla de Bayes**

## P(A/B) = $\frac{P(B/A) P(A)}{\sum_{i=1}^n P(B_{i}/A) P(A)}$
**Presenta: Vanessa Cristell Torres López**

P(A/B), representa la probabilidad de que ocurra el evento A dado que ha ocurrido el evento B.
Se conoce también como la probabilidad posterior de A.

**Ejemplo**
La probabilidad de que un alumno repruebe un examen es del 20%.

Reprobar un examen está relacionado con: haber estudiado poco, no haber descansado lo suficiente y tener mala salud; cada una con probabilidades de 60%, 30% y 10% respectivamente.

La probabilidad de que ocurra cada uno de los tres eventos sin que esté relacionado con reprobar el examen es de:  Estudiar poco = 5%, no descansar lo suficiente = 70% y tener mala salud = 25%.

A fin de aplicar la regla de Bayes, calculemos la probabilidad de que el alumno repruebe un examen dado que no descansó lo suficiente.  


*Definiendo eventos*

P(A) = Probabilidad de reprobar un examen = 0.2

P(B_1)  = Probabilidad de que el alumno haya estudiado poco = 0.05

P(B_2) = Probabilidad de que el alumno no haya descansado bien = 0.7

P(B_3) = Probabilidad de que el alumno se enferme = 0.25

P(B1/A) = Probabilidad de que el alumno haya estudiado poco dado que reprobó el examen =0.6

P(B2/A) = Probabilidad de que alumno ho haya descansado correctamnte dado que reprobó el examen = 0.3

P(B3/A) = Probabilidad de que alumno se encuentre enfermo dado que reprobó el examen = 0.1
"""

# Probabilidad de fallar el examen
P_A = 0.2

# Probabilidades condicionales de los indicadores dado que falla el examen
P_B1_given_A = 0.6  # P(B1|A)
P_B2_given_A = 0.3  # P(B2|A)
P_B3_given_A = 0.1  # P(B3|A)

# Probabilidad total de cada indicador
P_B1 = 0.05  # P(B1)
P_B2 = 0.7   # P(B2)
P_B3 = 0.25  # P(B3)

# Probabilidad total de B dado que falla el examen
P_B_total = P_B1_given_A * P_A + P_B2_given_A * P_A + P_B3_given_A * P_A

# Aplicando la regla de Bayes para encontrar P(A|B1)
P_A_given_B1 = (P_B1_given_A * P_A) / P_B_total

# Imprimir el resultado
print(f"La probabilidad de fallar el examen dado que estudió poco es: {P_A_given_B1:.4f}")