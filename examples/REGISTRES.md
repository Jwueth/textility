# Registres du Collectif Démo

**Exemple entièrement fictif.** Les personnes, dates, décisions et états ci-dessous appartiennent au [scénario de prêt](SCENARIO.md). Ces tables sont des exemples de tenue documentaire, pas des comptes rendus d'exécution ni des validations réelles.

Le « registre commun » prévu par la règle de prêt contient les prêts. Les registres présentés ici ont une autre fonction : retrouver les sources, questions et décisions qui expliquent cette règle. Ils ne contiennent ni emprunteurs ni historique de prêts.

## Répartition fictive

La responsable fictive du collectif décide de la règle. L'agent fictif prépare les entrées et vérifie leurs renvois ; il n'accorde pas d'approbation. Les notes du mini-vault portent les textes complets. Les tables suivantes les indexent sans constituer une seconde version de la règle.

## Sources

| ID | Document | Nature | Version/date | Disponibilité et lecture dans le scénario | Usage et limite |
|---|---|---|---|---|---|
| SRC-DEMO-001 | [Besoin](vault/10_References/Source%20-%20besoin.md) | Entrée locale fictive | État livré avec le scénario | Document disponible ; lecture décrite par le scénario | Exprime le besoin, pas une approbation de solution |
| SRC-DEMO-002 | [Décision du registre unique](vault/10_References/Decision%20-%20registre%20unique.md) | Acte d'arbitrage fictif | 2026-01-15, dans la fiction | Document disponible | Établit le choix et laisse la conservation ouverte |
| SRC-DEMO-003 | [Référence de prêt](vault/10_References/Reference%20-%20pret%20de%20materiel.md) | Référence fictive dérivée de la décision | 2026-01-15, dans la fiction | Document disponible | Formulation d'usage de la règle ; ne fixe aucune conservation |

« Disponible » décrit ici le paquet. Il ne signifie pas qu'un agent vient de relire ces documents dans une nouvelle session.

## Question à suivre

| ID | Question et enjeu | Origine | Destinataire | État | Réponse établie dans la fiction | Suite |
|---|---|---|---|---|---|---|
| Q-DEMO-001 | Quelle conservation pour les données du registre des prêts ? | [Question de conservation](vault/00_Inbox/Question%20-%20conservation.md) | Responsable fictive | Ouverte | Aucune durée approuvée ; douze mois ne constitue pas une règle | Préciser les contraintes avant de décider ; ne rien supprimer sur cette seule hypothèse |

La simple répétition de « douze mois » dans un brouillon ne permet pas de remplir la colonne Réponse comme si le choix était acquis.

## Décisions et portée

| ID | Choix indexé | État dans la fiction | Décideur et date fictifs | Preuve | Portée et confirmation restante |
|---|---|---|---|---|---|
| DEC-DEMO-001 | Registre commun avec quatre informations ; pas de copie personnelle officielle | Confirmée dans le scénario | Responsable fictive du collectif, 2026-01-15 | [Acte complet](vault/10_References/Decision%20-%20registre%20unique.md) | Règle du collectif fictif seulement ; la conservation reste hors de cet accord |
| DEC-DEMO-002 | Retenir douze mois comme durée de conservation | Non approuvée ; question ouverte | Absence d'approbation constatée dans l'acte fictif du 2026-01-15 | [Même acte](vault/10_References/Decision%20-%20registre%20unique.md) | Aucun autre délai n'en découle ; voir Q-DEMO-001 |

Ces IDs sont propres à cet exemple ; ils ne remplacent pas les titres ni les actes du mini-vault. La séparation des deux lignes empêche de traiter une approbation partielle comme un accord sur l'ensemble.

## Application distincte

| Décision | Effet documentaire décrit | Preuve du scénario | Limite |
|---|---|---|---|
| DEC-DEMO-001 | Règle intégrée dans la référence de prêt | [Référence](vault/10_References/Reference%20-%20pret%20de%20materiel.md) | Aucun registre de prêts réellement déployé ni traitement de données attesté |
| DEC-DEMO-002 | Pas de durée intégrée comme règle | [Question maintenue ouverte](vault/00_Inbox/Question%20-%20conservation.md) | Aucune suppression autorisée |

## Place dans le scénario

Cette table sert de support à l’étape 2 du [parcours progressif](SCENARIO.md). La procédure proposée est [gd-tenir-registre](../skills/gd-tenir-registre/SKILL.md) ; les nouvelles productions restent dans `atelier/` de la copie complète, jamais dans les notes sources. L’étape suivante prépare le design de ces mêmes tables.

## Exercice sur copie

Demander à l'agent, en lecture seule : « Une réponse indique que la durée sera précisée plus tard. Quelle entrée faut-il actualiser et que faut-il garder ouvert ? »

La réponse attendue réutilise Q-DEMO-001 et n'invente ni délai, ni approbation, ni preuve d'application. Pour essayer une écriture, l'autoriser ensuite sur une copie, comparer la ligne touchée et vérifier que les autres objets restent inchangés. Ce parcours est une recette proposée, pas un test comportemental déjà réussi.

Les [modèles](../templates/README.md) et le [guide des registres](../docs/04-registres.md) permettent d'adapter ces tables sans reprendre les approbations fictives.
