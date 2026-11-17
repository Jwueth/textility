# Tenir des registres que l'humain et l'agent peuvent partager

Une question posée dans une séance réapparaît dans une synthèse, puis dans un échange avec l'agent. Une décision est citée sans sa réserve. Un document attendu finit par être traité comme s'il avait été lu. Les registres servent à retrouver ces objets et leur état sans relire toutes les conversations.

Ce chapitre propose une démarche de tenue des registres, avec ses limites. Les modèles en fin de page sont des supports à adapter, pas une structure à imposer à tous les projets.

## Partir de l'information qui doit faire foi

Avant de créer une table, convenir de ce qu'elle porte et de ce qui reste ailleurs.

| Information | Où elle fait foi | Ce que le registre apporte |
|---|---|---|
| Contenu et version d'une source | Dans le document identifié | Provenance, disponibilité, périmètre de lecture et limites |
| Arbitrage | Dans un acte identifiable, ou dans une ligne assez complète pour en conserver la teneur et la preuve | Décideur, date, portée, réserves et lien vers l'application |
| Question | Dans l'entrée suivie, reliée aux échanges utiles | Formulation, destinataire, réponse reçue, inconnue restante |
| Application d'une décision | Dans le résultat effectivement contrôlé | Renvoi vers ce contrôle, distinct de l'approbation |

Une seule source de vérité signifie un propriétaire par information, pas nécessairement un fichier unique. Si la décision complète vit dans une note, le registre l'indexe sans en maintenir une seconde version. Si une ligne porte elle-même l'arbitrage, les synthèses renvoient à cette ligne.

Un classeur peut porter les données structurées et une vue HTML en faciliter la lecture. Le registre Markdown décrit alors les décisions et questions utiles sans recopier toutes les données du classeur. Un export HTML est un instantané ; une interface de saisie exige en plus un mécanisme d'écriture, des contrôles et des permissions. Ce kit n'en fournit pas.

## Choisir des outils simples

Un éditeur Markdown suffit pour les modèles du kit. Un outil de notes liées peut faciliter la navigation ; un agent mandaté peut rechercher une entrée, préparer un ajout et comparer les changements. Aucun ne remplace l'autorité qui décide.

Conserver un historique récupérable, par versionnement ou copies datées. Un changement enregistré prouve une modification, pas une approbation. Les besoins de droits d'accès et de suivi simultané déterminent si une simple table reste adaptée.

## Construire le registre en travaillant

1. **Choisir un besoin précis.** « Quelles questions attendent une réponse ? » justifie une table ; « centraliser toute la connaissance » ne fixe pas de limite exploitable. Nommer le responsable du registre et les écritures que l'agent peut effectuer.
2. **Chercher avant d'ajouter.** Comparer sens, périmètre et source avec les entrées existantes. Une reformulation ou une réponse partielle ne crée pas nécessairement un nouvel objet.
3. **Attribuer un identifiant stable.** Dans les exemples, les préfixes sont `SRC-DEMO`, `Q-DEMO` et `DEC-DEMO`, suivis d'un numéro. Conserver l'ID lors d'une correction et ne pas recycler ceux des entrées retirées. Préserver tels quels les numéros d'une source externe.
4. **Qualifier l'entrée.** Séparer le propos de la source, l'interprétation de l'agent et la proposition soumise. Pour une décision, distinguer celui qui arbitre dans son mandat de celui dont la confirmation est encore nécessaire.
5. **Appliquer le changement autorisé.** Relire le fichier courant juste avant d'écrire. En présence d'une modification concurrente inexpliquée, suspendre l'écriture plutôt qu'écraser. Comparer ensuite les seules lignes et colonnes attendues.
6. **Fermer la boucle.** Une réponse partielle laisse la question ouverte sur ce qui manque. Une décision acceptée n'est « appliquée » qu'après contrôle de son effet. Actualiser les renvois concernés sans recopier l'historique dans chaque note.

Une ligne doit pouvoir être vérifiée et faire évoluer son état indépendamment. Si elle contient deux questions adressées à des personnes différentes, ou un choix accepté et un choix encore ouvert, la scinder ou expliciter les sous-parties.

## Répartir les responsabilités

| Acte | Humain responsable | Agent mandaté |
|---|---|---|
| Définir le registre | Fixe usage, périmètre, règles et responsable | Propose la structure et les points ambigus |
| Alimenter | Apporte ou confirme les sources et le sens des échanges | Recherche les doublons, prépare les lignes et les liens |
| Arbitrer | Décide dans son mandat ; identifie l'autorité supplémentaire si nécessaire | Sépare recommandation, décision rapportée et preuve disponible |
| Mettre à jour | Autorise un lot ou une maintenance routinière bornée | Applique, compare et signale ce qui reste inconnu |
| Clore ou remplacer | Confirme le traitement et les conséquences | Préserve l'identifiant, le motif et les renvois historiques |

Dans un travail à plusieurs agents, un dépôt d'extraction reste une entrée à contrôler. Le rôle qui consolide vérifie fidélité et doublons ; une revue indépendante peut examiner un risque précis. Ni la fin d'une tâche ni le verdict technique d'un reviewer ne valent décision humaine. Prévoir un seul rédacteur par fichier à un instant donné ; une instruction seule ne verrouille pas le fichier.

## Distinguer l'état du fichier de celui des lignes

Un registre peut être actif et contenir des questions ouvertes, des décisions confirmées et des propositions refusées. Une approbation de sa structure ne valide pas chaque ligne, ni les ajouts futurs.

Les trois modèles de registres n'ont volontairement pas de frontmatter : ils ne créent pas un nouveau vocabulaire dans le schéma du mini-vault. À l'adoption, leur attribuer les métadonnées locales et préciser leur portée. Ne pas appliquer `authority: reference` et `validation_status: approved` à tout le tableau pour éviter de qualifier ses lignes.

Convenir de statuts simples selon l'objet :

- source : disponible et lue, lue partiellement, disponible non lue, attendue ; une synthèse dérivée reste distincte de son original ;
- question : ouverte, réponse partielle, close ou abandonnée avec motif ; « close » ne signifie pas forcément « exigence approuvée » ;
- décision : attendue, arbitrage local à confirmer, confirmée dans son périmètre, refusée ou remplacée. L'application se suit séparément.

Ces libellés sont des propositions pour les modèles, pas de nouveaux états de frontmatter.

## Points de vigilance

Les registres longs deviennent difficiles à lire. Des compteurs saisis à la main se désynchronisent. Une ligne fermée trop vite peut masquer la moitié non répondue d'une question. Une mention « validé » copiée depuis une source peut perdre son acteur ou sa portée.

Avant une remise, vérifier les IDs uniques, les liens utiles, la cohérence entre statut et preuve, le décideur et la date des décisions confirmées. Relire la source pour toute assertion qui commande l'action suivante. Si les tables deviennent trop larges, conserver l'index court et déplacer le détail dans des notes liées ; ne pas créer une copie officielle pour chaque lecteur.

Le [vérificateur du kit](../scripts/README.md) contrôle certains liens, pas la structure des tables, l'unicité de leurs IDs ou la vérité de leurs lignes. Les contrôles ci-dessus restent une recette à réaliser, non une capacité automatique livrée. Les permissions et la gestion des accès relèvent de l'environnement choisi.

## Essayer sans réorganiser son environnement

Lire l'[exemple fictif](../examples/REGISTRES.md), puis choisir au besoin un seul des modèles : [sources](../templates/Registre-sources.md), [questions](../templates/Registre-questions.md) ou [décisions](../templates/Registre-decisions.md). Sur une copie non sensible, préparer un ajout et une réponse partielle. Vérifier que l'agent réutilise l'entrée existante, laisse les inconnues ouvertes et ne présente aucune recommandation comme un accord.

Conserver le registre seulement s'il évite une recherche, une contradiction ou une perte de suivi réelle. Une note de décision bien liée peut suffire pour un sujet court.

L’ébauche [gd-tenir-registre](../skills/gd-tenir-registre/SKILL.md) traduit la démarche en procédure pour l’agent. L’étape 2 du [scénario](../examples/SCENARIO.md) l’exerce sur les mêmes sources, avec une réponse partielle à traiter sans fermer la question. Il s’agit d’une recette à réaliser, pas d’un résultat déjà obtenu.

Suite : [construire un design commun](05-design-commun.md).
