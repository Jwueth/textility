# Cas de conception : préparer un festival fictif

**Exercice entièrement fictif.** Ce cas illustre le [chapitre HTML](../docs/07-html-pour-comprendre.md). Il fournit un support de raisonnement, pas une application HTML ou un classeur à exécuter.

## Pourquoi un second cas ?

Le petit registre de prêts montre la distinction entre maître et projection. Pour aborder la navigation entre plusieurs types d'objets, imaginons une association qui prépare un festival. Ce cas reste séparé de la règle de prêt du mini-vault.

## La source imaginée

Un classeur répartit les lieux, les activités, les créneaux, les équipements et les questions entre plusieurs onglets. Les relations utilisent des identifiants.

| Objet | Informations à préserver | Exemple inventé |
|---|---|---|
| Lieu | ID, nom, capacité | L-DEMO-01 — petite salle, 30 places |
| Créneau | ID, horaires, lieu | C-DEMO-01 — 10 h à 11 h, L-DEMO-01 ; C-DEMO-02 — 11 h à 12 h, même lieu |
| Activité | ID, intitulé, créneaux proposés, réservation confirmée | A-DEMO-01 — atelier de gravure ; proposition C-DEMO-01 ou C-DEMO-02 ; réservation non décidée |
| Équipement | ID, désignation, activité liée, disponibilité | E-DEMO-01 — presse mobile ; liée à A-DEMO-01 ; disponibilité à confirmer |
| Question | ID, objet concerné, réponse disponible | Q-DEMO-HTML-01 — la presse sera-t-elle disponible ? Liée à E-DEMO-01 ; réponse non reçue |

Une salle, un créneau et une activité ne sont pas trois événements additionnables. Une activité proposée dans deux créneaux n'est ni deux activités ni deux réservations confirmées. L'équipement lié à une activité n'est pas nécessairement disponible.

## Trois tâches de lecture

| Question du lecteur | Composition HTML proposée | À vérifier pendant son propre essai |
|---|---|---|
| Que se passe-t-il dans la petite salle ? | Vue du lieu avec créneaux et activités, propositions distinctes des réservations | A-DEMO-01 n'apparaît pas comme une réservation confirmée |
| Que manque-t-il pour organiser l'atelier de gravure ? | Fiche activité avec équipement et questions liées | La disponibilité inconnue et la question ouverte restent visibles |
| Quelles activités utilisent la presse ? | Liste filtrée depuis la fiche équipement, puis retour au contexte | Les liens correspondent à la source ; le retour conserve le parcours |

Ces vues évitent de parcourir toute la grille pour chaque question. Les valeurs détaillées et leur provenance doivent néanmoins rester accessibles.

## Exercice de conception

Dans une copie complète du kit, après autorisation d'un nouveau fichier dans `atelier/` :

> À partir de ce cas, prépare `atelier/lecture-maitre-dense.md`. Décris les questions des lecteurs, le mapping source → modèle → vues, les informations toujours visibles, les filtres et le parcours de détail/retour. Garde proposition de créneau et réservation confirmée distinctes ; ne résous aucune question. Précise si la vue serait autonome ou servie, puis comment le lecteur connaîtrait sa fraîcheur. Ne génère ni application ni nouveau jeu de données, et ne modifie aucun fichier source.

**Résultat attendu :** une proposition de structuration, pas un écran annoncé testé. Seul un essai réel permet d'observer si la composition facilite la tâche du lecteur.

**Erreurs à détecter :** additionner des objets de nature différente ; confirmer automatiquement un créneau proposé ; faire disparaître une disponibilité inconnue ; présenter un champ masqué comme une donnée retirée du fichier.

## Passage éventuel à l'édition

Pour renseigner une réservation confirmée, il faudrait identifier qui peut décider, l'objet et le champ cibles, les valeurs permises et la version lue. Le [complément d'édition](../modules/html-edition/README.md) expose les exigences de confirmation, de conflit et de relecture.

Dans cet exercice, la réservation reste non décidée : aucune édition ni nouvelle validation n'est effectuée.
