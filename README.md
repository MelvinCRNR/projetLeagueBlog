# README Projet LeagueBlog

# Introduction

Ce projet consiste au développement d’un Blog portant sur le sujet de League Of Legends.

Afin de mettre en place ce projet, nous allons utiliser les technologies suivantes :

- Python avec comme Framework, Flask.
- HTML, CSS, Bootstrap.
- Base de données MySQL.
- Docker.

# Base de données

Notre base de données se compose de la sorte : 

![BDDLeagueBlog.png](README%20Projet%20LeagueBlog%207bb1f483e52f440c9870ef7bf12dc7eb/BDDLeagueBlog.png)

Nous possédons une base contenant 2 tables.

La table user qui contient les informations sur les utilisateurs du blog.

La table post qui contient les posts postés sur le site.

Ces deux tables sont liés par [user.id](http://user.id) et post.user_id qui permettent d’indiquer à qui appartient le post.

# Architecture des fichiers

Voici les fichiers que nous retrouvons à la base du fichier.

![Untitled](README%20Projet%20LeagueBlog%207bb1f483e52f440c9870ef7bf12dc7eb/Untitled.png)

Comme éléments importants ici, nous retrouvons le dossier [app.py](http://app.py) contenant le code de notre site. 

Le fichier [config.py](http://config.py) contient des informations utiles pour se connecter à a base de données.

Le fichier [tests.py](http://tests.py) contient 2 tests de l’application.

Le dossier sql contient les le Dockerfile pour la base de données et le fichiers lolbase.sql qui contient les requêtes sql à exécuter pour créer la base de données utilisée dans le projet.

## app.py

![Untitled](README%20Projet%20LeagueBlog%207bb1f483e52f440c9870ef7bf12dc7eb/Untitled%201.png)

Le fichier __init_.py est le main fichier de l’application.

[forms.py](http://forms.py) contient les formulaires utilisés dans l’application.

[models.py](http://models.py) contient les modèles des tables qui seront importés dans la base de données de manière automatique grâce à quelques commande de la bibliothèque flask-db.

[routes.py](http://routes.py) contient les routes utilisées dans notre blog.

## templates

Le dossier templates contient les éléments de frontend.

![Untitled](README%20Projet%20LeagueBlog%207bb1f483e52f440c9870ef7bf12dc7eb/Untitled%202.png)

# Routes utilisées

| Route | Correspondance |
| --- | --- |
| /index et / | Accueil |
| /login | Page de connexion |
| /logout | Déconnexion |
| /register | Page d’inscription |
| /user/<username> | Page de profil d’<username> |
| /edit_profile | Modification de profil |
| /follow/<username> | Route pour suivre <username> |
| /unfollow/<username> | Route pour ne plus suivre <username> |
|  |  |

# Déploiement de l’application en local

Afin de déployer l’application en local.

1. Installez l’image Docker ‘mysql’
2. Paramètrez mysql avec comme user : root et mot de passe : Mysql2022
3. Créez la database : LolBase
4. Téléchargez le contenu du git
5. Mettez vous à la racine du projet
6. Lancez l’environnement virtuel avec la commande suivante : **python3 -m venv env** && **source env/bin/activate**
7. Lancez la commande suivante pour installer les bibliothèques nécessaires au bon fonctionnement de l’application : **python3 -m pip install -r requirements.txt**
8. Remplacer ‘db’ par 127.0.0.1 dans le fichier [config.py](http://config.py), ligne 6 : `SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Mysql2022@127.0.0.1/LolBase'`
9. Lancez les commandes suivantes : flask db init && flask db migrate && flask db migrate

# Lancement de l’application avec Docker

Lancez la commande suivante après avoir télécharger les fichiers Docker fournis avec le code.

Vous pouvez aussi retrouver les images docker sur le docker hub.

[https://hub.docker.com/repository/docker/melvinks/mysql](https://hub.docker.com/repository/docker/melvinks/mysql)

[https://hub.docker.com/repository/docker/melvinks/projetleagueblog_app](https://hub.docker.com/repository/docker/melvinks/projetleagueblog_app)

Lancez la commande suivante : 

```java
docker-compose up --build
```

Allez ensuite sur l’adresse suivante :

http://0.0.0.0:5000/

# Problème rencontré

Utilisant flask-db et flask-migrate, il s’avère que mes modèles ne créaient pas mes tables déclarées dans mon fichier models.py. L’application plante donc à chaque moment ou on appel la base de données.
