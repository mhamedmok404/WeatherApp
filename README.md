# 🌤️ Weather App (Tkinter)

## 🧾 Description

Application Python avec interface graphique permettant d'afficher la météo en temps réel d'une ville ou de votre position actuelle.

Les données sont récupérées via l’API OpenWeatherMap et incluent :

* 🌡️ Température
* 🌬️ Vent
* 💧 Humidité
* 📊 Pression
* 📝 Description
* 🕒 Heure locale

---

## 🚀 Fonctionnalités

* Recherche météo par ville
* Détection automatique de la localisation
* Affichage du fuseau horaire local
* Interface graphique intuitive

---

## 🛠️ Technologies utilisées

* Python
* Tkinter
* Geopy
* TimezoneFinder
* Requests
* Pytz
* Geocoder

---

## ⚙️ Installation

### 1. Cloner le projet

```bash id="n6k9c3"
git clone https://github.com/username/weather-app.git
cd weather-app
```

### 2. Créer un environnement virtuel (recommandé)

```bash id="lj2r7m"
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Installer les dépendances

```bash id="7z0z9g"
pip install -r requirements.txt
```

---

## 🔑 Configuration

Ajoutez votre clé API OpenWeatherMap dans le code :

```python id="7i5h5s"
appid=YOUR_API_KEY
```

👉 Obtenir une clé gratuite : https://openweathermap.org/api

---

## ▶️ Exécution

```bash id="zgh1zq"
python main.py
```

---

## 📡 Utilisation

* Entrez une ville puis cliquez sur 🔍
* Ou utilisez 📍 pour votre position actuelle

---

## 📁 Structure du projet

```id="mjkg3l"
weather-app/
│── main.py
│── requirements.txt
│── assets/
│    ├── search.png
│    ├── search_icon.png
│    ├── location.png
│    ├── logo.png
│    └── box.png
```

---

## ⚠️ Remarques

* Nécessite une connexion Internet
* Une clé API valide est obligatoire
* Vérifiez les chemins des images

---

## 🔧 Améliorations futures

* Prévisions météo sur plusieurs jours
* Interface plus moderne
* Sécurisation de la clé API (.env)
* Version web (Flask / React)

---

## 📜 Licence

Projet open-source.
