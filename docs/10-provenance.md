# Provenance, choix et limites

## Filiation du kit

Textility prolonge le kit *Gouvernance documentaire humain–agent*, snapshot 1.0.0 du 4 novembre 2026. Sa licence MIT est conservée. Les textes, modèles, procédures et scripts sont rédigés pour le kit ; les données, dates, rôles et approbations des exemples sont fictifs.

Les prescriptions de gouvernance sont des choix proposés, pas des obligations imposées par Hermes ou Obsidian. Les références techniques officielles ont été consultées lors de la préparation du snapshot, le 4 novembre 2026.[1][2][3] La page « Creating Skills » a été relue le 16 novembre 2026 pour la structure des nouvelles procédures. Ces lectures ne constituent pas une vérification permanente de toutes les versions des outils.

## Portée des prolongements méthodologiques

- Les [registres](04-registres.md) proposent une démarche, des modèles et un [exemple fictif](../examples/REGISTRES.md). Leurs tables et leurs identifiants ne font pas l'objet de contrôles automatiques dédiés.
- Le [design commun](05-design-commun.md) explique les choix partagés et leur adaptation par support. Son [illustration](../examples/DESIGN-COMMUN.md) ne fournit ni identité visuelle prête à appliquer ni rendu testé.
- Le [classeur maître](06-classeur-maitre.md) distingue autorité des données, changement et projection. Le [module optionnel](../modules/classeur-maitre/README.md) fournit un XLSX de trois prêts inventés, une projection et des scripts bornés. Seul cet outillage optionnel utilise `openpyxl`.
- Le [chapitre HTML](07-html-pour-comprendre.md) traite des tâches de lecture, des relations et de la fraîcheur. Le [cas fictif du festival](../examples/HTML-MAITRE-DENSE.md) et le [complément d'édition](../modules/html-edition/README.md) proposent des exercices documentaires. Ils ne livrent ni application HTML, ni éditeur, ni serveur.

Le [scénario](../examples/SCENARIO.md) relie ces démarches à des consignes, des sorties attendues et des décisions humaines. Les productions d'essai restent dans `atelier/` d'une copie indépendante ; les approbations de la fiction ne les autorisent pas.

Les procédures `gd-tenir-registre`, `gd-construire-design-commun` et `gd-capitaliser-lecon` sont des ébauches documentaires 0.1.0. La capitalisation complète les formes documentaires et la carte des workflows : observation étayée, règle candidate, destination et vérification d'intégration, sans extension du schéma du mini-vault. La page « Creating Skills » a été relue le 17 novembre 2026 pour ce complément. La présence et les métadonnées des procédures ne démontrent ni installation native ni comportement conforme d'un agent. Le journal du XLSX reste vide : aucune validation réelle n'y est présumée.

## Inspiration du nom

Le nom s'inspire du concept de *textility* chez Tim Ingold, notamment dans *The textility of making*, **Cambridge Journal of Economics**, 34 (2010), 91–102, DOI [10.1093/cje/bep042](https://doi.org/10.1093/cje/bep042). La référence bibliographique est notamment confirmée par une [bibliographie publiée chez Oxford University Press](https://academic.oup.com/edited-volume/38642/chapter/335375893).

L'article primaire n'a pas été lu pour cette adaptation. Cette inspiration ne revendique ni application intégrale de la théorie ni approbation du projet par son auteur.

## Choix assumés

- Responsabilités et échanges explicites, plutôt qu'une séparation physique humain/agent.
- Références communes, sans copie officielle propre à chaque lecteur.
- Markdown pour la lecture et la réutilisation ; aucun service imposé.
- Métadonnées limitées au démonstrateur et adoption progressive.
- Skills courts et autonomes, sans droits supplémentaires.
- Inconnues et réserves visibles, même dans les exemples.

## Ce qui n'est pas démontré par ce dépôt

- La qualité d'un modèle ou sa conformité systématique aux instructions.
- Une protection technique contre les écritures hors mandat.
- Le chargement automatique des règles et skills dans toutes les versions de Hermes.
- Le rendu et le comportement de chaque version d'Obsidian ou de tableur.
- L'absence absolue de données sensibles ou de risques de redistribution.
- L'efficacité des vues HTML ou de l'édition guidée, sans application livrée et essayée.
- Un bénéfice chiffré de productivité.

Les tests du kit portent sur des contrôles statiques et sur son outillage d'exemple. Une recette humaine dans l'environnement destinataire complète ces preuves ; la démarche n'est pas présentée comme universellement éprouvée.

## Références techniques

[1] https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files

[2] https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills

[3] https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions
