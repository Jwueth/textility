# Exemple de démarche : une règle commune pour plusieurs supports

**Illustration entièrement fictive.** Ce prolongement du Collectif Démo ne décrit aucun outil déployé, aucune séance réelle et aucun rendu testé. Il complète le [guide méthodologique](../docs/05-design-commun.md).

Cette illustration accompagne l’étape 3 du [scénario progressif](SCENARIO.md), après les registres. La procédure proposée est [gd-construire-design-commun](../skills/gd-construire-design-commun/SKILL.md). Dans l’essai, la sortie est une proposition méthodologique dans `atelier/`, pas une charte appliquée ni un rendu annoncé réussi.

## Le problème à traiter

La responsable fictive veut que la règle de prêt soit lisible dans une note, un tableau et un schéma d'explication. Les supports ne doivent pas faire croire qu'une proposition est déjà approuvée. Elle ne demande ni une nouvelle marque ni la refonte de tout son espace de travail.

L'agent propose de commencer par une note et un tableau dense, sur copies. Le schéma n'est décliné qu'après examen de ce premier échantillon.

## Ce que chacun prépare

| Objet | Travail proposé à l'agent | Choix laissé à l'humain |
|---|---|---|
| Brief d'usage | Lecteur, tâche, support et application cible | Périmètre du pilote et éléments à préserver |
| Petit échantillon | Titre long, statut visible, tableau dense, impression | Lisibilité et direction à retenir |
| Contrat `DESIGN.md` | Valeurs et règles issues des choix acceptés | Identité, exceptions et portée d'adoption |
| Adaptation par support | Styles de note, de table et de schéma | Compromis de densité et d'usage |
| Contrôles et comparaison | Texte, fonction et rendu avant/après | Acceptation du résultat pour l'usage convenu |

## Passer d'une remarque à une règle

Supposons que la responsable dise : « On doit voir qu'une question reste ouverte même sur une impression sans couleur. » L'agent ne choisit pas seulement une teinte différente. Il propose d'écrire le statut, puis d'en vérifier la présence à l'écran et à l'impression.

Un extrait de travail du contrat pourrait exprimer :

```md
## Règles de statut

Afficher le statut en texte ; une couleur ne le remplace pas.
Dans un tableau, conserver ce texte après filtrage et à l'impression.
Dans un schéma, distinguer les propositions des règles retenues.

## Adaptations et limites

La note privilégie la lecture ; le tableau, le repérage des lignes.
Les choix de police, de palette et de tailles restent à instruire.
Une copie générée ne devient pas la source des données.
```

Cet extrait illustre une règle et ses raisons. Ce n'est pas un contrat complet ni une identité visuelle prête à appliquer. Le format et les valeurs restent à choisir, puis leur prise en charge par les supports à vérifier.

## Choisir des outils à la mesure du besoin

Pour cette fiction, un éditeur Markdown et une revue dans l'application cible suffiraient à commencer. Si la production se répète, le collectif pourrait envisager un vérificateur de règles, des scripts d'application de styles ou des tests de navigateur pour les états HTML. Cette sélection reste à faire ; aucun de ces outils n'est présenté comme exécuté ici.

Un outil de critique de style peut signaler une taille inhabituelle. La responsable examine alors si le tableau en a besoin ; elle ne remplace pas cette décision par l'obligation de faire disparaître tous les avertissements.

## Relier le choix à sa preuve

Après un accord explicite, une entrée au registre des décisions pourrait consigner : règle des statuts écrits, supports concernés, décideur, date réelle de l'accord et éventuelles réserves. Les champs restent vides tant que l'accord n'existe pas.

La trace des contrôles rapporte séparément ce qui a été regardé ou exercé. Une ouverture sans erreur ne suffit pas à annoncer une modification, un recalcul et une réouverture réussis. Un PDF dont le texte tient sur une page peut encore être trop petit à lire.

## Capitaliser ce qui évite la prochaine correction

Dans ce scénario proposé, la règle irait dans le contrat puis dans les adaptateurs utiles. Une évolution du contrat amènerait à vérifier ses consommateurs ; elle ne déclencherait pas une migration générale des anciens fichiers.

L'exercice consiste à demander à l'agent de préparer cette démarche sans appliquer de charte : quels fichiers font foi, qui choisit, quels outils seraient nécessaires et quelles preuves manqueraient ? L'objectif est une proposition contrôlable, pas une palette inventée ni un succès d'exécution supposé.
