Présentation projet bibliographie : 

Une base de donnée : Livres (situé dans biblio/models.py)

Deux pages html situé dans le dossier templates :

accueil.html :
 
Ou se trouve 3 images (static/biblio) en static.
Chaque image amene a la deuxiemme page "description.html"
	

description.html :

Ou se trouve les données qu'on recupere grace a l'id présent dans l'url.
On recupere aussi grace a cette ID, les différentes données présent dans la base de donnée pour le livre choisi
Affiche donc le titre, l'annee, l'auteur ainsi que l'image choisi dans accueil.html

 