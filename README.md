# COMMENT INSTALLER UN ENVIRONNEMENT VIRTUEL

##

### etape 1: avoir python3 d'installé, sinon se référer a la doc officielle de python pour l'installer

### etape 2: taper la commande suivante pour le creer:

```bash
python3 -m venv venv
```

un dossier nommé "venv devrait apparaitre

### etape 3: taper la commande suivante pour l'activer

```bash
source venv/bin/activate
```

si l'operation a été un succès, vos ligne de terminal doivent commencer par (.venv) ou (venv)

pour le desactiver, taper sous venv:

```bash
deactivate
```

### etape 4: installer les dépendances

sous venv, taper la commande suivante:
```bash
pip install -r requirements.txt
```

voila ! vous avez tous les prérequis nécessaires pour débuter le workshop. en cas de souci hésiter pas a m'interroger (je mords pas xd)

bon courage !