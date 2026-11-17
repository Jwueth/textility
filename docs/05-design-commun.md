# Construire et entretenir un design commun

Un document, un schéma et un tableau de suivi peuvent porter la même identité sans avoir la même mise en page. Le besoin apparaît quand chaque nouvelle production réinvente ses styles et que les corrections ne se retrouvent pas dans la suivante.

La démarche consiste à expliciter les choix communs, les adapter par support et vérifier les résultats. Un fichier `DESIGN.md` peut en conserver les règles ; sa présence ne suffit pas à rendre les livrables cohérents.

## 1. Définir l'usage avant la palette

Préciser le lecteur, la tâche, le support éditable, l'application cible, le canal de diffusion et la charte qui s'impose. Examiner quelques fichiers représentatifs avant de proposer une évolution.

Distinguer :

- les règles partagées de lisibilité, de hiérarchie et de présentation des statuts ;
- l'identité retenue pour une organisation ou un produit ;
- la composition adaptée à chaque usage : lire un texte, comprendre un schéma, projeter un message ou saisir des données.

La charte du destinataire prime dans son périmètre. Une interface dense ne doit pas devenir une présentation publicitaire pour paraître harmonisée.

## 2. Examiner un petit échantillon

L'agent prépare une proposition sur copies : titre long, tableau dense et cas limite pertinent. L'humain choisit une direction et formule ses corrections avant une déclinaison complète.

Vérifier le contenu et les droits des images, logos et polices. Une empreinte prouve l'identité des octets, pas le sens d'une image ni le droit de la réutiliser. L'accord sur un échantillon ne vaut pas refonte de tout le corpus.

## 3. Formaliser les choix communs

Une référence par identité rassemble les valeurs convenues et leurs raisons : couleurs et usages, hiérarchie typographique, espacement, composants pertinents et exceptions par support. `DESIGN.md` est une possibilité, pas une obligation.

L'agent traduit les choix approuvés ; l'humain conserve la responsabilité de la direction visuelle et des exceptions. Les exports de valeurs de style restent des dérivés régénérables, pas des chartes concurrentes.

Nommer le mainteneur, la portée et la décision qui autorise les choix. Un contrôle de structure ou de contraste ne valide ni la composition ni le sens des textes.

## 4. Adapter à chaque support

| Support | Adaptation nécessaire | Comportement à préserver |
|---|---|---|
| HTML | Styles et composants, thèmes et impression | Liens, filtres, clavier, états et données |
| Document de texte | Styles natifs, tableaux et pagination | Structure, champs et éditabilité |
| Présentation | Masques et compositions adaptées à la projection | Objets modifiables et ordre de lecture |
| Tableur | Formats, zones de saisie, filtres et impression | Formules, validations et distinction saisie/résultat |
| PDF | Export depuis la bonne source et contrôle des pages | Lisibilité, texte, liens et pagination |

Les unités et les usages diffèrent : une taille de corps ne se transpose pas telle quelle d'un document à des diapositives. Un changement de police impose de contrôler à nouveau la pagination. Pour une sortie générée, corriger la source ou l'adaptateur plutôt que le seul fichier qui sera remplacé.

## 5. Choisir les outils et les preuves nécessaires

Un éditeur Markdown et une revue dans l'application cible peuvent suffire. Si la production se répète, des modèles natifs, des scripts d'application de styles ou des tests de navigateur peuvent réduire les corrections manuelles. Les choisir selon le besoin, leurs limites, leurs droits d'utilisation et leur coût d'entretien.

Un skill décrit une procédure ; une bibliothèque manipule des fichiers ; un moteur produit un rendu. Lire la procédure ne signifie pas avoir exécuté les outils.

| Contrôle | Conclusion possible |
|---|---|
| Vérification de la référence de styles | Les erreurs visées par ce contrôle ont été recherchées |
| Comparaison du fichier produit | Les contenus et fonctions examinés sont préservés |
| Inspection visuelle | Le rendu examiné convient dans le périmètre regardé |
| Ouverture dans l'application cible | Le fichier s'ouvre, sans prouver encore son édition ou son recalcul |
| Modification, enregistrement et réouverture | Le parcours natif testé fonctionne sur cette copie |
| Acceptation humaine | Les aspects nommés sont acceptés pour l'usage convenu |

Rapporter les substitutions de polices, contrôles impossibles et fonctions non testées. Un aperçu PDF ne prouve pas le comportement du fichier éditable.

## 6. Entretenir les règles sans tout migrer

Reporter les choix retenus dans la référence et les procédures utiles. Conserver les versions remplacées, puis travailler depuis la référence courante plutôt que depuis une ancienne démonstration.

Lors d'un changement, identifier les supports affectés et refaire les contrôles correspondants. La généralisation à d'autres fichiers reste une décision distincte. L'humain choisit et autorise la diffusion ; l'agent prépare, applique et contrôle dans son mandat. Le [registre des décisions](04-registres.md) peut conserver les choix significatifs, leur portée et leurs réserves.

## Essayer la démarche

Le [cas fictif](../examples/DESIGN-COMMUN.md) montre comment passer d'une correction à une règle réutilisable, sans imposer d'outillage. L'ébauche [gd-construire-design-commun](../skills/gd-construire-design-commun/SKILL.md) en propose la procédure. L'étape 3 du [scénario](../examples/SCENARIO.md) l'applique à la préparation de notes et de registres, sans génération ni installation implicite.

Suite : [un classeur maître et ses projections](06-classeur-maitre.md).
