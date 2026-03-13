# semaine-01/complexite.py
#Question 1 du quiz : quelle est la complexite de ce code?

# CODE ORIGINAL DU QUIZ
# for i in range(n):
#     for j in range(n):
#         print(i, j)


# MON ANALYSE:
# Pour  n = 3: le print s'execute 3 x 3 = 9 fois
# Pour  n = 4: le print s'execute 4 x 4 = 16 fois
# Pour  n = 5: le print s'execute 5 x 5 = 25 fois
# Formule generale: n x n = n2
#Complexite : O(n^2)

def compter_operations(n):
    compteur = 0
    for i in range(n):
        for j in range(n):
           compteur += 1

    return compteur


# Verification experimentale
for n in [3, 4, 5, 10, 100]:
    print(f"n={n} → {compter_operations(n)} operations (attendu : {n**2})")