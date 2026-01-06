
# SecurePwd Pro 🔐

Un utilitaire Python avancé pour la génération, l'analyse d'entropie et l'audit de sécurité des mots de passe via API.

## 📌 Présentation

La sécurité d'un mot de passe ne dépend pas seulement de sa longueur, mais de sa résistance aux attaques. **SecurePwd Pro** va plus loin que la simple génération en proposant :
1. **Génération robuste** : Utilise des méthodes cryptographiquement sûres.
2. **Calcul d'entropie** : Mesure mathématique de la force du mot de passe selon les critères de l'ANSSI.
3. **Audit de fuite (API)** : Vérifie en temps réel si le mot de passe a été exposé dans des brèches de données mondiales.
4. **Interface élégante** : Rendu visuel riche et coloré directement dans le terminal.

## 🛠️ Fonctionnement technique

Le script met en œuvre des concepts de sécurité et de développement avancés :
- **Bibliothèque `secrets`** : Pour une génération de caractères supérieure au module `random` classique.
- **API HaveIBeenPwned (K-Anonymity)** : Pour garantir la confidentialité, le mot de passe est haché en **SHA-1**. Seuls les 5 premiers caractères du hash sont envoyés à l'API ; la comparaison finale se fait localement.
- **Formule d'entropie** : Calcule le niveau de sécurité en bits : $L \times \log_2(R)$ (où $L$=longueur et $R$=taille du jeu de caractères).
- **Rich UI** : Utilisation de tableaux et de panneaux pour une expérience utilisateur (UX) professionnelle en ligne de commande.

## 🚀 Utilisation

### Prérequis
- Python 3.8 ou supérieur.
- Une connexion internet (pour la vérification d'API).

### Installation et Lancement
1. **Clonez le dépôt** :
```bash
git clone [https://github.com/Flowz5/SecurePwd.git](https://github.com/Flowz5/SecurePwd.git)
cd SecurePwd

```

2. **Installez les dépendances** :
```bash
pip install -r requirements.txt

```


3. **Lancez l'outil** :
```bash
python main.py

```



## 💡 Pourquoi ce projet ?

Développé dans le cadre de mon **BTS SIO SLAM**, ce projet démontre ma capacité à :

* Consommer des **API REST** de manière sécurisée.
* Manipuler des concepts de **hachage cryptographique**.
* Créer des outils "Developer Friendly" avec une interface soignée.
* Appliquer des notions mathématiques à la cybersécurité.

## ⚖️ Licence

Ce projet est sous licence MIT - libre d'utilisation et de modification.
