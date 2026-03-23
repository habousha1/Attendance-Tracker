# Cloud Attendance Tracker ☁️🎓

Bienvenue dans le dépôt du projet **Cloud Attendance Tracker** ! 

Il s'agit d'une application web simple conçue pour aider les professeurs ou les écoles à suivre la présence de leurs étudiants. Elle permet d'ajouter des étudiants, de marquer leur statut de présence (Présent/Absent) au jour le jour, et de visualiser rapidement les statistiques globales.

## 🚀 Fonctionnalités
- **Page d'accueil simple** : Visualisation en un coup d'œil de tous les étudiants enregistrés.
- **Ajout d'étudiants** : Formulaire rapide pour ajouter le nom et le prénom de l'étudiant.
- **Gestion des présences** : Boutons "Présent" (Vert) ou "Absent" (Rouge) pour chaque étudiant.
- **Statistiques en temps réel** : Compteur automatique du nombre d'absences et de présences.
- **Design moderne & responsive** : Interface centrée, propre et intuitive (CSS Vanilla).

## 🛠️ Technologies Utilisées
- **Backend :** Python, Flask
- **Frontend :** HTML, CSS (100% sans JavaScript)
- **Base de données :** SQLite (embarquée)

---

## 💻 Comment lancer le projet localement ?

Si vous souhaitez tester l'application sur votre propre ordinateur avant de la déployer :

**1. Clonez ce dépôt ou téléchargez les fichiers**
```bash
git clone https://github.com/VOTRE_NOM_UTILISATEUR/Cloud_Attendance_Tracker.git
cd Cloud_Attendance_Tracker
```

**2. Créez un environnement virtuel (Recommandé)**
```bash
python -m venv venv
# Sur Windows :
.\venv\Scripts\activate
# Sur Mac/Linux :
source venv/bin/activate
```

**3. Installez les dépendances**
```bash
pip install -r requirements.txt
```

**4. Lancez le serveur Flask**
```bash
python app.py
```

**5. Ouvrez votre navigateur**
Allez sur `http://localhost:10000` et profitez !

---

## ☁️ Déploiement Cloud (sur Render)

Cette application a été spécialement configurée pour être déployée facilement et gratuitement sur **Render**.

1. Créez un compte gratuit sur [Render.com](https://render.com/).
2. Cliquez sur **"New Web Service"**.
3. Connectez votre compte GitHub et sélectionnez ce dépôt (`Cloud_Attendance_Tracker`).
4. Dans la configuration, utilisez ces paramètres :
   - **Environment :** Python
   - **Build Command :** `pip install -r requirements.txt`
   - **Start Command :** `python app.py` (ou `gunicorn app:app`)
5. Cliquez sur **"Create Web Service"**.

Patientez quelques minutes, et Render vous fournira une URL publique accessible depuis n'importe quel ordinateur ou téléphone ! 🌍
