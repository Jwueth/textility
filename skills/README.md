# Procédures proposées à l'agent

Les quatre procédures du socle sont complétées par **trois ébauches 0.1.0** pour les registres, le design commun et la capitalisation. Elles sont rédigées pour ce kit.

Ces sept skills sont des procédures, pas des droits supplémentaires. Leur présence dans le dépôt ne les installe pas. Aucun n'embarque de script ou de dépendance réseau ; ils ne requièrent pas les autres dossiers du kit pour comprendre leurs étapes essentielles.

## Choisir selon le travail à faire

| Skill | Quand l'utiliser | Résultat | Dans le scénario |
|---|---|---|---|
| [gd-cadrer-echange](gd-cadrer-echange/SKILL.md) | Le mandat ou l'échange est ambigu | Résultat, responsabilités et limites explicites | Cadrer l'essai avant toute écriture |
| [gd-curer-document](gd-curer-document/SKILL.md) | Une source ou un brouillon doit devenir exploitable | Proposition sourcée, sans validation implicite | Rédiger la candidate après analyse des impacts |
| [gd-reprendre-contexte](gd-reprendre-contexte/SKILL.md) | Reprendre un sujet ou actualiser un checkpoint | État vérifié dans son périmètre et cache dérivé | Expliquer la règle puis reprendre l'essai |
| [gd-reviser-reference](gd-reviser-reference/SKILL.md) | Une référence ou convention doit évoluer | Candidate, impacts, décision et contrôle | Instruire l'ajout d'un champ d'état au retour du matériel |
| [gd-tenir-registre](gd-tenir-registre/SKILL.md) — ébauche | Suivre sources, questions ou décisions dans le temps | Delta borné, IDs stables, preuves et inconnues | Tenir les registres et traiter une réponse partielle |
| [gd-construire-design-commun](gd-construire-design-commun/SKILL.md) — ébauche | Préparer une cohérence entre plusieurs supports | Démarche, outils, responsabilités et recette de pilote | Préparer le design des mêmes notes et tables |
| [gd-capitaliser-lecon](gd-capitaliser-lecon/SKILL.md) — ébauche | Un résultat observé peut améliorer une pratique réutilisable | Règle candidate, destination, delta et preuve d'intégration selon le mandat | Distinguer bilan et leçon ; ne pas inventer un essai réussi |

Les trois ébauches spécialisent le socle ; elles ne le remplacent pas. Tenir un registre n'exige pas de réviser une référence à chaque ajout. Préparer le design d'une table n'autorise pas à modifier son contenu. Reprendre le résultat ne suffit pas à intégrer une leçon dans la procédure qui doit la porter.

La [carte des workflows](../docs/03-workflows.md) indique aussi les démarches sans skill dédiée : revue du corpus, partage et prolongements maître/HTML. Ce choix n'enlève ni leurs contrôles ni les autorisations nécessaires ; toutes les démarches n'exigent pas une nouvelle procédure installable.

## Essayer sans installer

Dans une copie isolée du kit, demander explicitement à l'agent de lire le `SKILL.md` voulu, puis lui donner la consigne du [scénario](../examples/SCENARIO.md). Cette lecture permet un essai guidé ; elle ne démontre pas l'installation native, la découverte automatique ni la conformité systématique d'un agent.

Pour une adoption dans Hermes, lire les procédures avant installation et suivre le [guide d'adoption](../docs/08-adoption.md) ainsi que la documentation officielle de sa version. Ne remplacer ni un homonyme, ni l'identité ou les conventions existantes. Les chemins de données et les permissions se résolvent dans le workspace réel.

## Preuves encore à obtenir

Les trois ébauches ont des métadonnées et une structure examinables, mais n'ont pas fait l'objet d'une installation native ou d'une recette comportementale. Le scénario décrit les sorties et refus attendus pour les éprouver. Pour la capitalisation, vérifier aussi le refus de transformer un essai prévu en résultat acquis, le réemploi d'une règle existante et l'absence d'écriture sans mandat. Noter version de Hermes, procédure lue, mandat, résultat observé et limites au lieu de conclure « skill validé » depuis la seule présence du fichier.
