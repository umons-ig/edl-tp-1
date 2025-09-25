# Exercice 1 : Fondamentaux des Tests Unitaires

## Objectif

Cet exercice a pour but de vous familiariser avec les tests unitaires et le cycle de développement piloté par les tests (TDD). Votre tâche consiste à corriger les fonctions défectueuses dans `calculator.py` afin que tous les tests unitaires définis dans `test_calculator.py` passent avec succès.

## Configuration de l'environnement

1.  **Changer de branche pour l'exercice 1 :**
    ```bash
    git checkout exercice-1-test-unitaire
    ```

## Utilisation

### Exécuter les tests

Pour exécuter les tests unitaires et vérifier votre progression, utilisez la commande suivante :

```bash
uv run pytest test_calculator.py
```

Au début de l'exercice, vous devriez observer plusieurs échecs de tests. Votre objectif est de modifier `calculator.py` jusqu'à ce que tous les tests passent.

### Fichiers à modifier

*   `calculator.py` : Contient les fonctions à corriger.
*   `test_calculator.py` : Contient les tests unitaires. Vous pouvez également ajouter vos propres tests si vous le jugez nécessaire pour couvrir des cas non testés.

## Fonctions à corriger

Les fonctions suivantes dans `calculator.py` contiennent des bogues :

*   `divide(a, b)` : Doit gérer la division par zéro en levant une `ZeroDivisionError`.
*   `power(base, exponent)` : Doit gérer correctement les exposants négatifs et le cas où l'exposant est zéro.
*   `factorial(n)` : Doit calculer la factorielle pour les nombres non négatifs (0! = 1, 1! = 1) et lever une `ValueError` pour les nombres négatifs.
*   `average(numbers)` : Doit gérer le cas d'une liste vide en levant une `ValueError`.

## Résultat attendu

Lorsque toutes les corrections auront été appliquées et que les tests seront exécutés, la sortie de la commande `uv run pytest test_calculator.py` devra indiquer que **tous les tests ont réussi** (par exemple, "15 passed in X.XXs").
