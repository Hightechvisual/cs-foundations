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