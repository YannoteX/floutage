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
