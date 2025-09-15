# Analyse de Sentiment des Annonces de la FED

Une application web professionnelle pour analyser le sentiment des communiqués de presse et des annonces de la Réserve Fédérale (FED). Cette application offre une
interface conviviale pour exécuter trois algorithmes d'analyse de sentiment distincts sur n'importe quelle URL d'annonce de la FED.

## Fonctionnalités

- **Interface Web Intuitive** : Une interface utilisateur claire et simple, construite avec Flask et Bootstrap.
- **Modèles d'Analyse Multiples** : Choisissez parmi trois indicateurs d'analyse de sentiment :
    - **Indicateur v1** : Utilise NLTK VADER, un modèle basé sur un lexique robuste et optimisé pour le sentiment.
    - **Indicateur v2** : Emploie TextBlob pour un calcul rapide de la polarité et de la subjectivité du texte entier.
    - **Indicateur v3** : Une approche plus fine qui calcule le sentiment moyen de chaque phrase individuelle avec TextBlob.
- **Résultats Détaillés** : Visualisez les scores de sentiment directement dans l'interface web.
- **Déploiement Simple** : Fonctionne localement comme une application Flask standard.

## Installation

Suivez ces étapes pour configurer et lancer le projet sur votre machine.

### 1. Prérequis

- Python 3.7+
- Gestionnaire de paquets `pip`

### 2. Cloner le Dépôt

Clonez ce dépôt sur votre machine locale :

```bash
git clone <url_du_depot>
cd <repertoire_du_projet>
````

### 3. Créer un Environnement Virtuel (Recommandé)

Pour une gestion propre des dépendances, créez et activez un environnement virtuel.

- **macOS / Linux :**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **Windows :**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

### 4. Installer les Dépendances

Installez les paquets Python requis à partir du fichier `requirements.txt`.

```bash
pip install -r requirements.txt
```

Lors du premier lancement, l'application téléchargera également automatiquement les données NLTK nécessaires (`vader_lexicon` et `punkt`).

## Utilisation

### 1. Démarrer le Serveur Flask

Exécutez le fichier `app.py` pour lancer le serveur web local.

```bash
python app.py
```

Le terminal indiquera que le serveur est en cours d'exécution, généralement sur `http://127.0.0.1:5000`.

### 2. Accéder à l'Interface Web

Ouvrez votre navigateur web et accédez à l'adresse suivante :
[**http://127.0.0.1:5000**](https://www.google.com/url?sa=E&source=gmail&q=http://127.0.0.1:5000)

### 3. Effectuer une Analyse

1. **Choisir un Indicateur** : Sélectionnez l'onglet "Indicateur v1", "v2" ou "v3".
2. **Saisir une URL** : Trouvez une URL de communiqué de presse sur le [site de la Réserve Fédérale]
3. (https://www.federalreserve.gov/newsevents/pressreleases.htm) et collez-la dans le champ de saisie.
    - *Exemple d'URL :* `https://www.federalreserve.gov/newsevents/pressreleases/monetary20230503a.htm`
4. **Analyser** : Cliquez sur le bouton "Analyser le Sentiment".
5. **Consulter les Résultats** : La page se rechargera pour afficher les résultats détaillés de l'analyse.

