# Le HTML pour rendre un maître dense intelligible

Un classeur peut conserver correctement des données, tout en demandant trop d'efforts pour répondre à une question simple. Le lecteur passe entre les onglets, retrouve des lignes et reconstitue leurs relations.

Le HTML permet d'organiser l'accès à ces informations selon les tâches humaines. **Le XLSX reste maître des données dans le périmètre qui lui est attribué ; le HTML en facilite la compréhension.**

Le [schéma maître et vues](../assets/maitre-et-vues.svg) relie cette source, le modèle de lecture et les différents parcours de consultation. Le circuit d'édition éventuel reste séparé ; le dessin ne représente pas un writer livré.

## 1. Pourquoi le HTML ?

| Besoin | Apport possible | Point de vigilance |
|---|---|---|
| Se repérer | Vue d'ensemble et niveaux de lecture | Ne pas cacher une réserve essentielle dans un détail replié |
| Trouver | Recherche et filtres | Montrer les filtres actifs et les résultats vides |
| Comprendre les liens | Fiches liées et navigation contextuelle | Distinguer relation établie, interprétation et lien absent |
| Approfondir | Détails à la demande et retour au contexte | Préserver le parcours, y compris au clavier |
| Partager | Fichier autonome si ses ressources sont embarquées | Vérifier sa fraîcheur et toutes les données qu'il contient |

HTML structure le contenu, CSS règle sa présentation et JavaScript peut porter les interactions. Une page simple peut suffire. Pour la saisie libre en masse ou les calculs personnels, le tableur peut rester plus adapté. L'impression et l'accessibilité nécessitent leurs propres contrôles.

## 2. Concevoir les vues à partir des questions

1. **Choisir les tâches.** Qui consulte, pour trouver ou décider quoi ? Partir de quelques questions concrètes plutôt que d'une liste d'écrans.
2. **Relier les informations.** Identifier les objets, leurs identifiants, leurs relations et les valeurs inconnues. Un modèle intermédiaire peut les réunir sans modifier les données sources.
3. **Composer les niveaux de lecture.** Séparer vue d'ensemble, sélection et détail. Prévoir les objets sans affectation, les liens absents, les cas vides et le retour au filtre initial.
4. **Vérifier la fidélité.** Comparer valeurs et relations à la source. Examiner aussi ce que les filtres excluent. Ne pas transformer une proposition en choix confirmé ni additionner des objets de nature différente.
5. **Faire essayer les tâches.** Observer si le lecteur retrouve et comprend l'information utile. Des tests techniques ne prouvent pas à eux seuls une réduction de l'effort humain.

Le [cas fictif du festival](../examples/HTML-MAITRE-DENSE.md) permet d'exercer cette démarche sur un modèle relationnel. Il fournit un exercice de conception, pas une application HTML prête à utiliser.

## 3. Rendre la fraîcheur explicite

| Mode | Données lues | Actualisation |
|---|---|---|
| HTML autonome | Instantané embarqué à la génération | Régénérer le fichier ; recharger la page seule ne change pas les données |
| Consultation servie | Source définie par le service | Relire selon le fonctionnement annoncé du service |
| Interface d'édition | Source autorisée et révision contrôlée | Relire les données effectivement enregistrées après modification |

Afficher la source et la version lues. Si la génération échoue, l'ancienne vue reste une ancienne vue, pas une représentation courante par défaut.

## 4. Garder les responsabilités visibles

L'humain définit les usages, tranche les ambiguïtés et accepte le résultat pour un périmètre donné. L'agent peut préparer le modèle, les vues et les contrôles dans son mandat. Une présentation soignée n'ajoute pas d'autorité aux données.

Un champ caché ou une ligne filtrée **reste dans le fichier si ses données y sont embarquées**. Avant partage, sélectionner les données à la source et examiner le contenu distribué.

Si le besoin devient la modification d'un maître trop difficile à manipuler, le [complément sur l'édition guidée](../modules/html-edition/README.md) présente les exigences supplémentaires. Un formulaire HTML ne suffit pas à écrire dans un XLSX.

Suite : [adopter et essayer le kit](08-adoption.md).
