Pr�sentation projet bibliographie : 

Une base de donn�e : Livres (situ� dans biblio/models.py)

Deux pages html situ� dans le dossier templates :

accueil.html :
 
Ou se trouve 3 images (static/biblio) en static.
Chaque image amene a la deuxiemme page "description.html"
	

description.html :

Ou se trouve les donn�es qu'on recupere grace a l'id pr�sent dans l'url.
On recupere aussi grace a cette ID, les diff�rentes donn�es pr�sent dans la base de donn�e pour le livre choisi
Affiche donc le titre, l'annee, l'auteur ainsi que l'image choisi dans accueil.html

 