# Semaine 01 — Complexité algorithmique

## Ce que j'ai appris
La complexité temporelle mesure combien d'opérations
fait un algorithme en fonction de la taille n des données.

## Question 1 du quiz
Deux boucles for imbriquées → O(n²)
Pourquoi : la boucle externe tourne n fois,
pour CHAQUE iteration elle relance la boucle interne n fois.
Total : n × n = n² opérations.

## Tableau de mes mesures
| n   | opérations réelles | n²    |
|-----|-------------------|-------|
| 3   | 9                 | 9     |
| 10  | 100               | 100   |
| 100 | 10 000            | 10 000|

1. **C'est quoi la complexité temporelle ?**

   La complexité temporelle est le temps que met un algorithme à afficher un résultat.
   Elle mesure le nombre d'opérations qu'un algorithme effectue en fonction de la taille **n** des données en entrée.

2. **Pourquoi deux boucles imbriquées donnent O(n²) ?**

   Une boucle est de complexité **n**. Deux boucles imbriquées sont de complexité **n × n = n²**.
   Donc 2 boucles imbriquées donnent **O(n²)**.

3. **Exemple concret de code O(n) et O(n²) :**

   **O(n) :**
```python
   for i in range(n):
       print(i)
```

   **O(n²) :**
```python
   for i in range(n):
       for j in range(n):
           print(i, j)
```