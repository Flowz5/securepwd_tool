
# SecurePwd Generator 🔐

Un outil léger en ligne de commande (CLI) écrit en Python pour générer des mots de passe robustes et évaluer leur sécurité réelle.

## 📌 Présentation

La sécurité d'un mot de passe ne dépend pas seulement de sa longueur, mais de son **entropie** (le niveau d'incertitude). Cet outil permet de :
1. Générer des mots de passe incluant majuscules, minuscules, chiffres et symboles.
2. Calculer l'entropie en bits selon les critères de l'ANSSI.
3. Afficher un indicateur visuel de force (Faible, Moyen, Fort).

## 🛠️ Fonctionnement technique

Le script repose sur des modules sécurisés :
- **`secrets`** : Pour une génération de caractères cryptographiquement sûre (supérieure au module `random` classique).
- **Algorithme d'entropie** : Calcule le nombre de bits de sécurité selon la formule $L \times \log_2(R)$ où $L$ est la longueur et $R$ la taille du jeu de caractères utilisé.

## 🚀 Utilisation

### Prérequis
- Python 3.6 ou supérieur installé.

### Lancement
1. Clonez le dépôt :
   ```bash
   git clone [https://github.com/Flowz5/SecurePwd.git](https://github.com/Flowz5/SecurePwd.git)

    ```

2. Accédez au dossier :
    ```bash
    cd SecurePwd

    ```


3. Lancez le script :
    ```bash
    python main.py

    ```

## 💡 Pourquoi ce projet ?

Développé dans le cadre de mon **BTS SIO SLAM**, ce projet démontre ma compréhension des enjeux de la cybersécurité et ma capacité à implémenter des concepts mathématiques (entropie) dans un utilitaire fonctionnel.

## ⚖️ Licence

Ce projet est sous licence MIT - libre d'utilisation et de modification.
