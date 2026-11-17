# Un classeur maître, des projections régénérables

Un tableau est corrigé dans Excel, un résumé dans une note et une vue dans un autre fichier. Quelques jours plus tard, ils divergent. Le problème n'est pas le nombre de supports : c'est l'absence d'une règle disant **quelle information fait foi, où la corriger et comment propager le changement**.

Ce chapitre décrit une méthode, puis un petit module optionnel l'illustre. Il ne livre ni éditeur de classeur, ni synchronisation, ni contrôle d'accès.

![Un maître désigné alimente un modèle de lecture puis plusieurs vues de la même base. Un circuit d'édition distinct et facultatif passe par une écriture autorisée et des contrôles, puis par la régénération des vues.](../assets/maitre-et-vues.svg)

## 1. Attribuer l'autorité par information

| Objet | Ce qui fait foi | Ce qui n'en découle pas |
|---|---|---|
| Lignes de travail | Le maître explicitement désigné, dans son périmètre | Qu'un fichier nommé « final » ou copié dans le cloud soit automatiquement maître |
| Choix de règle, validation | La décision attribuée, sa source et sa portée | Qu'une cellule remplie ou un test réussi approuve le fond |
| Question ouverte | Son suivi et les réponses réellement reçues | Qu'une couleur, un export ou une mise en forme la clôture |
| Vue générée | La source enregistrée et la recette de génération | Qu'éditer cette vue corrige la source |

Un registre de prêts contient des transactions ; les registres de sources, questions et décisions du [chapitre 4](04-registres.md) organisent leur gouvernance. Ils ne se remplacent pas. Un maître n'est pas nécessairement l'autorité de toutes les informations : après une publication dans un autre système, certains champs peuvent relever de ce système selon une règle explicite.

Désigner explicitement le maître, le rôle des copies de partage et l'autorité qui arbitre les conflits. Ne pas déduire ces rôles du nom des fichiers.

## 2. Séparer proposition, écriture et projection

1. **Lire la base réellement utilisée.** Repérer le maître, son état enregistré, les consommateurs, les colonnes et les règles de saisie. Conserver une empreinte et préciser ce qui n'a pas été lu. Les modifications non enregistrées dans Excel ne sont pas visibles par un lecteur de fichier.
2. **Préparer un delta sur copie.** Distinguer lignes ajoutées, valeurs existantes changées et éléments intangibles. Réutiliser les identifiants lorsqu'ils existent ; ne pas les normaliser silencieusement. Un petit exemple sans ID ne justifie pas un rapprochement automatique de deux grands classeurs.
3. **Contrôler le candidat.** Comparer valeurs, formules, validations, commentaires et parties utiles du classeur selon le risque. Tester les consommateurs contre cette copie, pas contre le vivant. Un chargement par une bibliothèque ne démontre pas un enregistrement sans perte.
4. **Obtenir l'accord sur le changement exact.** L'acteur qui prépare peut différer de l'autorité qui tranche. Une permission d'intégrer une proposition ne valide pas le contenu métier de toutes les lignes.
5. **Appliquer avec protection de la base.** Avant toute écriture réelle : vérifier fermeture/verrou pertinent, relire la base, sauvegarder et respecter les droits. Si les empreintes ont changé, comparer le contenu et préserver les changements intervenus ; un réenregistrement par Excel peut changer les octets sans changer les valeurs. Ne pas attribuer ce drift sans preuve.
6. **Tracer et régénérer.** Rapporter le delta réellement appliqué et ses limites, puis reconstruire les dérivés depuis la source retenue. Conserver le dernier dérivé connu en cas d'échec, mais ne pas le présenter comme courant. Rafraîchir le lecteur n'est pas régénérer les données.

Cette chaîne décrit l'entretien d'un maître réel. Le module ci-dessous ne l'automatise pas : il **lit** un exemple et crée une nouvelle projection, sans appliquer de changement au maître.

## 3. Choisir l'outillage selon le classeur

Un tableur compatible permet le travail humain ; un lecteur de fichiers peut servir à comparer ou générer des vues. Les capacités varient selon les formats et les fonctions du classeur : éprouver la conservation des formules, validations et autres éléments utiles avant toute écriture automatisée.

Les empreintes identifient une version technique, pas son auteur ni sa justesse. Les sauvegardes permettent une reprise ; les générateurs reconstruisent les dérivés. Ces rôles restent distincts. Un contrôle dans une application ne prouve pas un comportement identique dans une autre.

**Un XLSX n'impose pas `openpyxl`.** Le fichier s'ouvre avec un tableur compatible ; un lecteur peut aussi être construit avec la bibliothèque standard ZIP/XML. Le module choisit `openpyxl` pour rester court et lisible : c'est une dépendance de son outillage optionnel, pas une condition de lecture du kit ou de ses contrôles de socle.

## 4. Essayer sur le même cas fictif

Le [module classeur maître](../modules/classeur-maitre/README.md) fournit un XLSX neuf, sa projection Markdown et les scripts propres à cet exemple. Il conserve exactement les quatre informations de prêt de la référence fictive : objet, personne emprunteuse, date de sortie, retour prévu.

- Le classeur est **un support proposé pour l'exercice**, pas une décision historique supplémentaire du collectif.
- Les personnes et opérations sont inventées. Le maître de démonstration porte seulement les lignes de prêt ; la durée de conservation reste non décidée.
- L'onglet `LIRE` explique le fonctionnement ; `Prets` porte les données ; `Journal` est une trame vide, pas un journal de validations déjà obtenues.
- Le Markdown est une projection en lecture seule par convention : un éditeur de texte peut encore le modifier. Il indique l'empreinte de sa source ; il ne retourne rien vers le XLSX.

L'étape dédiée du [scénario](../examples/SCENARIO.md) permet de comparer source et vue, modifier une seule valeur sur copie, régénérer et observer le delta. Les essais techniques peuvent être exécutés sans simuler une approbation de l'humain.

## 5. Limites délibérées du module

Ce petit registre n'a pas d'ID de transaction, de calcul, de concurrence multi-utilisateur, de données personnelles réelles, de synchronisation ou de politique de conservation appliquée. La répétition d'un objet peut être légitime : le script ne transforme pas son nom en identifiant unique.

L'exporteur n'est pas un lecteur XLSX général. Il contrôle le format de l'exemple, exporte aussi les lignes masquées ou filtrées et refuse les formules dans les données. Il ne recalcule rien, ne lit pas les choix en cours dans une fenêtre Excel et ne réécrit pas la source. Les validations, styles ou protections d'une feuille ne constituent pas une sécurité ni une preuve de conformité métier.

Avant une adoption réelle : décider l'autorité, les droits, les identifiants et les règles de saisie ; éprouver lecture, modification, enregistrement et réouverture dans l'application cible ; qualifier sauvegarde, concurrence et consommateurs. Une projection correcte sur cet exemple ne suffit pas à autoriser un traitement de production.

Suite : [le HTML pour rendre un maître dense intelligible](07-html-pour-comprendre.md).
