# Historique des versions

## Unreleased — Textility

Préparation de la présentation sous le nom Textility, à partir du snapshot 1.0.0. Cette entrée ne désigne pas une nouvelle version publiée.

### Guides et exemples

- Catalogue des formes documentaires, distinct des fonctions du champ `type` : analyses, synthèses, procédures, glossaires, index, leçons, registres et projections. Aucun ajout de valeur au schéma du démonstrateur.
- Carte des workflows reliant besoins, entrées, sorties, contrôle humain, guides et skills ; démarche de capitalisation détaillée, sans dupliquer les guides spécialisés.
- Trois espaces fonctionnels : agent (cadre et préparation), commun (matière partagée), humain (compréhension et intervention), avec schéma relationnel et exemple de registre ; schéma de métadonnées, modèles et vérificateur inchangés.
- Démarches génériques sur les registres, le design commun, le classeur maître et les vues HTML. Exemples fictifs, sans récit d'un environnement de travail particulier.
- Trois modèles de registres : sources, questions et décisions, sans nouveau schéma de frontmatter imposé.
- Module XLSX optionnel : quatre informations de prêt, trois opérations inventées, mode d'emploi, journal vide et projection Markdown liée à l'empreinte de sa source.
- Générateur d'exemple, exporteur en lecture seule et neuf tests propres au module ; dépendance `openpyxl` distincte du socle. Refus des destinations occupées, pas d'éditeur de maître ni de synchronisation inverse.
- HTML : intérêt général, conception des vues par tâches et fraîcheur. Exercice documentaire sur un festival fictif, séparé du mini-vault de prêts.
- Complément documentaire d'édition guidée : droits, changement confirmé, base, conflits, sauvegarde et relecture. Aucun éditeur ou serveur livré.

### Procédures et parcours

- Trois ébauches autonomes 0.1.0 : `gd-tenir-registre`, `gd-construire-design-commun` et `gd-capitaliser-lecon`, sans script ni installation implicite.
- Capitalisation reliée au scénario : preuve observée, règle déjà présente à rechercher, destination et delta proposés, refus attendu d'un faux succès ou d'une écriture hors mandat.
- Scénario progressif reliant reprise, registres, design, essai optionnel du maître, conception HTML, cadrage de l'édition, révision et capitalisation.
- Essai minimal en lecture seule ou parcours complet dans `atelier/` d'une copie indépendante. Les huit notes gouvernées du mini-vault restent inchangées.
- Chapitres ordonnés selon le parcours : principes, conventions, workflows, registres, design, maître, HTML, adoption, maintenance et provenance.
- Installation native des skills, essais comportementaux et acceptation humaine non déduits des tests statiques.

### Présentation

- Accueil en français avec le descripteur anglais, le public visé et la boucle « cadrer → explorer → arbitrer → capitaliser → réviser ».
- Schémas du passage des sources à la référence, de la reprise, de la révision, du maître et de ses vues, puis de la boucle de capitalisation.
- Filiation du snapshot, inspiration du nom chez Tim Ingold et licence MIT conservées.
- Navigation, limites des contrôles et recette locale explicites.

### Vérificateur

- Rejet des wikilinks explicites qui sortent du mini-vault, y compris par chemin absolu, sans résolution de secours trompeuse.
- Diagnostics pour une liste `audience` contenant des objets, listes ou nombres, au lieu d'une exception non gérée.
- Sept tests de non-régression, en préservant les liens locaux valides et la validation stricte des valeurs permises.

Le vérificateur n'est ni un contrôle du comportement de l'agent, ni un parseur YAML général, ni une garantie de confidentialité. La [notice](scripts/README.md) précise son périmètre ; la structure et les identifiants des tables de registres restent à contrôler séparément.

## 1.0.0 — 2026-11-04

Première édition : zones de responsabilités et d'échanges, conventions documentaires, workflows, six modèles, mini-vault fictif, quatre skills et contrôles locaux. Aucun déploiement, profil ou service activé.
