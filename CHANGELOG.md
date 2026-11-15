# Historique des versions

## Unreleased — Textility

Préparation de la présentation du dépôt sous le nom Textility, à partir du snapshot 1.0.0. Cette entrée ne désigne pas une nouvelle version publiée.

### Présentation préparée

- Accueil en français avec le descripteur anglais retenu, le public visé et la boucle « cadrer → explorer → arbitrer → capitaliser → réviser ».
- Parcours de lecture, démarrage en lecture seule sur copie isolée et distinction entre capitalisation et stockage exhaustif.
- Première série de visuels retirée après relecture.
- Schéma source → référence revu, retenu et intégré au README.
- Deux déclinaisons du même langage illustrent la reprise et la révision dans le guide des workflows.
- Provenance précisant la filiation du snapshot et l’inspiration du nom chez Tim Ingold, sans revendication d’approbation.
- Licence MIT existante conservée ; limites des contrôles statiques et recette locale rendues explicites.

### Vérificateur — corrections ciblées

- Rejeter les wikilinks explicites qui sortent du périmètre du mini-vault, y compris par chemin absolu, sans masquer cette sortie par une résolution de secours.
- Renvoyer des diagnostics pour une liste `audience` contenant des objets, listes ou nombres, au lieu de provoquer une exception non gérée.
- Ajouter les tests de non-régression correspondants, en préservant les liens locaux valides et la validation stricte des valeurs permises.

Ces corrections sont intégrées à la préparation locale : les deux défauts ont été reproduits sur le vérificateur d’origine, puis les sept tests passent sur la version corrigée. Le vérificateur ne signale pas d’écart couvert dans le paquet.

Ces corrections ne transforment pas le vérificateur en contrôle du comportement de l’agent, en parseur YAML général ou en garantie de confidentialité. La notice des contrôles décrit le périmètre effectivement testé.

## 1.0.0 — 2026-11-04

Première édition : zones de responsabilités et d’échanges, conventions documentaires, workflows, six modèles, mini-vault fictif, quatre skills et contrôles locaux. Aucun déploiement, profil ou service activé.
