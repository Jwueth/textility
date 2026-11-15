# Adopter le kit sans perturber son environnement

## Deux parcours

### Découvrir dans un vault de démonstration

Copier `examples/vault/` dans un dossier indépendant. L’ouvrir comme vault Obsidian, lire `Accueil.md` et tester d’abord en lecture seule. Le mini-vault ne requiert pas de plugin communautaire. Obsidian peut créer sa propre configuration locale à l’ouverture ; ne pas la republier avec les notes.

Ouvrir le vault de démonstration seul pour vérifier que les liens ne sont pas résolus accidentellement par des notes du vault de travail. Le contenu doit rester compréhensible en Markdown, même sans Obsidian ; les liens wiki sont utilisés seulement dans le mini-vault.

### Adopter dans un vault existant

1. Inventorier les conventions, instructions, templates, droits et mécanismes de validation déjà en place.
2. Établir une petite table : concept du kit → équivalent local → écart → décision. Conserver les conventions utiles plutôt que tout renommer.
3. Choisir un sujet pilote non sensible : une proposition, une décision et une référence.
4. Valider les responsabilités et la limite d’intervention avant toute écriture.
5. Tester la reprise et la révision sur copies. Contrôler liens, historique et absence d’écriture hors mandat.
6. Étendre seulement si le pilote facilite réellement le travail.

Les modèles ont des champs volontairement vides. Les remplir n’est pas une approbation automatique. Les métadonnées du kit ne doivent pas remplacer celles qu’un plugin gère pour son propre fonctionnement.

## Utiliser avec Hermes

Les rôles généraux des fichiers de contexte et des skills sont décrits dans la documentation officielle ; leur découverte dépend du contexte de lancement et de la version.[1][2]

- **Identité du profil** : conserver son identité existante. Aucun `SOUL.md`, mémoire personnelle, modèle LLM ou paramètre d’authentification n’est fourni par ce kit.
- **Contrat du workspace** : `examples/vault/AGENTS.md` est un exemple à examiner, pas un fichier à copier par-dessus un contrat existant. Au premier essai, demander explicitement à l’agent de lire ce fichier ; ne pas supposer qu’il a été chargé automatiquement.
- **Skills** : les quatre dossiers `skills/gd-*` contiennent des procédures autonomes au format `SKILL.md`.[2] Les lire avant installation et suivre le mécanisme de sa version de Hermes. Une méthode prudente consiste à demander à son propre agent de les examiner puis de proposer leur installation dans un profil de test, sans modifier les skills homonymes.
- **Racine de travail** : confirmer le dossier réellement accessible par les outils. Un chemin hôte et un chemin de conteneur ne sont pas interchangeables.

### Vérifier l’adoption des skills

Après l’essai, noter la version de Hermes utilisée, le profil choisi et l’emplacement réel de chaque skill. Vérifier que les quatre noms `gd-*` n’ont pas écrasé un homonyme, que l’agent peut charger chaque procédure et qu’il lit le bon contrat de workspace. Consigner ce qui a été réellement testé ; ne pas déduire une installation réussie de la seule copie des fichiers.

Les instructions documentaires ne sont pas un contrôle d’accès technique. Pour protéger des données, limiter aussi les montages, comptes, outils et permissions. Le kit ne fournit ni sandbox, ni isolation de profil, ni garde-fou système.

## Pourquoi pas un export de profil ?

Un export complet peut emporter du contenu personnel. Une distribution Git de profil permet une sélection maintenable, mais son format, ses effets et ses exclusions doivent être vérifiés dans la version utilisée.[3] Ce kit ne fournit pas de distribution de profil : il évite ainsi d’imposer une identité ou une configuration pour adopter une méthode documentaire.

Le guide et le mini-vault sont utilisables immédiatement. L’installation automatique des skills, le chargement implicite des règles et l’usage dans chaque version de Hermes restent à vérifier localement.

## Recette d’adoption

- [ ] L’agent identifie les références, propositions et contenus dérivés.
- [ ] Il ne transforme pas un exemple fictif en fait réel.
- [ ] Une demande de lecture seule ne produit aucune modification.
- [ ] Il pose la question de conservation laissée ouverte dans le scénario.
- [ ] Il n’accorde pas une validation parce que le contrôle technique réussit.
- [ ] Les droits d’écriture et la publication externe restent distincts.
- [ ] La configuration et les notes de travail préexistantes restent intactes.

## Sources

[1] https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files

[2] https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills

[3] https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions
