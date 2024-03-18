# Sujet 4 : floutage automatique de visages

## Sujet :

Sujet 4 : floutage de visages en temps-réel
L’objectif de ce mini-projet est de suivre automatiquement un ou plusieurs visages qui se déplacent devant une webcam. Le suivi doit se faire en temps réel (c’est-à-dire au moins 5 fois/seconde pour être fluide). On veut flouter les visages pour « anonymiser » le flux vidéo.

Étapes :

  1. améliorer la qualité de l’image

  2. appliquer la méthode de Viola et Jones pour détecter le visage

  3. flouter automatiquement le(s) visage(s)

  4. bonus, si vous avez le temps: utiliser une heuristique pour stabiliser le tracking quand on passe d’une image à l’autre

## Orga :

### Captation du flux vidéo

- Récupération du flux vidéo d'une webcam : mauvaise fréquence d'image (risque faible), peu de stabilité de la récupération d'image (risque moyen), problèmes de drivers (risque faibles)
- Extraction des images et gestion d'envoie pour le traitement de celles-ci : l'extraction prend du temps et du processus (risque moyen), risque de traitement parallèle des images en fonction du temps de traitement (risque est fort)

### Traitement des Images

- Amélioration de la qualité de l'image : les images sont trop sombres ou trop lumineuses (risque moyen), bruit thermique (risque élevé), bruit poivre/sel (risque faible), les images ne sont pas nettes (risque fort)
- Identification des visages : l'image n'a pas de visage (risque fort), l'amélioration de la qualité n'a pas correctement fonctionnée (risque faible), la détection échoue (risque faible)
- Floutage des visages : le flou ne s'applique pas à un visage (risque faible)

### Retranscription des images

- Réception des images traitées : la réception échoue (risque faible)
- retranscription de la vidéo à partir des images traitées, l'affichage des images prend trop de temps par rapport au traitement (risque faible)


## Méthode

La méthode appliquée dite Viola et Jones permet de trouver les visages dans une image. En la testant, nous nous sommes rendus compte qu'elle s'avère très performante mais couteuse en temps de calcul. Afin de réduire ce temps nécessaire, nous avons pris différents décisions:

### Amélioration de l'image
Nous avons choisi d'améliorer les capacités de détection et augmentant le contraste de l'image par la méthode d'égalisation de l'histogramme d'intensités, et de la convolution d'image afin de faire ressortir les plus hautes fréquence. Nous avons également essayé différents algorithmes de filtration du bruit (variation totale, bilateral) sans obtenir de résultats concluant sur le temps de calcul économisé, il s'est également avéré inutile d'appliquer un algorithme d'amélioration de la netteté. "L'amélioration" de l'image se résume donc à améliorer le contrast afin d'améliorer la stabilité de la détection et d'économiser du temps de calcul.

### Optimisation 
Nous nous sommes rendus compte que la plupart des images détectées sur une webcam se situent vers le centre de l'image, afin d'améliorer le temps de calcul, nous avons décidé d'appliqué la méthode sur 85% de l'écran en partant du centre afin de ne pas calculer inutilement les bords de l'écran où le visage ne se trouve que très occasionellement.

## Affichage du visage flouté

Afin de retranscrire la vidéo modifiée, nous avons utilisé le mode interactif du module pyplot, cela permet de mettre à jour une figure pendant l'exécution du programme.

## Captation de la vidéo
Opencv permet de récupérer des images issues d'un flux vidéo capté par une caméra sans devoir passer par de l'asynchrone ou du threading. Cela permet d'éxécuter notre code sans avoir à gérer le framerate.

## Retour d'expérience

Grâce à l'efficacité de la méthode de Viola et Jones, beaucoup des risques identifiés n'ont pas de difficultés à réaliser ce projet, le temps pris à l'affichage et la captation de la vidéo est négligeable par rapport au temps de traitement
