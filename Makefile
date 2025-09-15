# Makefile pour le projet d'analyse de sentiment de la FED

# --- Variables de configuration ---
PYTHON ?= python3
# Le nom du répertoire venv est maintenant .venv pour correspondre au projet
VENV_DIR = .venv
VENV_PYTHON = $(VENV_DIR)/bin/python
VENV_PIP = $(VENV_DIR)/bin/pip

# --- Cibles principales ---
.PHONY: help install install-dev run clean lint
.DEFAULT_GOAL := help

help:
	@echo "-----------------------------------------------------------"
	@echo " Makefile pour le Projet d'Analyse de Sentiment de la FED"
	@echo "-----------------------------------------------------------"
	@echo "Cibles disponibles :"
	@echo "  make install      -> Crée l'env. virtuel (.venv) et installe les dépendances."
	@echo "  make install-dev  -> Installe les dépendances de développement."
	@echo "  make run          -> Démarre le serveur de développement Flask."
	@echo "  make clean        -> Supprime l'environnement virtuel et les fichiers cache."
	@echo "  make lint         -> Lance le linter flake8 pour vérifier la qualité du code."
	@echo "  make help         -> Affiche ce message d'aide."
	@echo "-----------------------------------------------------------"

# ... le reste du fichier reste identique ...

$(VENV_DIR)/bin/activate:
	@echo "🚀 Création de l'environnement virtuel dans $(VENV_DIR)..."
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_PIP) install --upgrade pip

install: $(VENV_DIR)/bin/activate
	@echo "📦 Installation des dépendances depuis requirements.txt..."
	$(VENV_PIP) install -r requirements.txt
	@echo "✅ Dépendances de base installées avec succès."

install-dev: install
	@echo "🛠️ Installation des dépendances de développement depuis requirements-dev.txt..."
	$(VENV_PIP) install -r requirements-dev.txt
	@echo "✅ Dépendances de développement installées."

run: install
	@echo "🔥 Démarrage du serveur Flask sur http://127.0.0.1:5000..."
	@echo "   (Pressez CTRL+C pour arrêter)"
	$(VENV_PYTHON) app.py

clean:
	@echo "🧹 Nettoyage du projet..."
	@rm -rf $(VENV_DIR)
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.pyc' -delete`
	@echo "🗑️ Environnement virtuel et fichiers cache supprimés."

lint:
	@echo "🎨 Lancement de l'analyse du code avec flake8 (en ignorant le dossier .venv)..."
	@$(VENV_PIP) show flake8 > /dev/null 2>&1 || \
		(echo "⚠️ flake8 n'est pas installé. Lancez 'make install-dev' pour l'ajouter." && exit 1)

	$(VENV_DIR)/bin/flake8 .

	@echo "✅ Analyse du code terminée."