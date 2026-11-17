# Complément documentaire — le HTML comme interface d'édition d'un maître dense

**Ce module ne livre aucun éditeur ni serveur à installer.** Il propose une démarche pour cadrer l'édition guidée. Le [chapitre HTML](../../docs/07-html-pour-comprendre.md) traite d'abord la compréhension ; le [cas fictif du festival](../../examples/HTML-MAITRE-DENSE.md) permet d'envisager une modification sans toucher à un maître réel.

## Le besoin

Un maître peut devenir difficile à modifier directement : colonnes nombreuses, informations liées dispersées ou risque de toucher une formule. L'interface peut présenter une tâche précise plutôt que toute la structure de stockage. Elle doit expliquer ce qui sera changé, où, avec quelle autorité et sur quelle version.

## 1. Choisir une opération limitée

Identifier l'acteur, les objets concernés, les champs accessibles, les valeurs permises et les éléments protégés. Distinguer correction de présentation, mise à jour de suivi et décision de fond.

Un formulaire détaillé et un raccourci dans une liste peuvent coexister. Définir les droits de chaque parcours ; ne pas les déduire de son apparence. Les valeurs autorisées viennent d'une référence désignée, pas des seules valeurs déjà rencontrées.

## 2. Définir les règles d'écriture

| Élément | À préciser |
|---|---|
| Source | Fichier ou stockage autorisé, distinct des copies d'essai |
| Acteur | Qui peut proposer, décider et appliquer ; authentification adaptée |
| Champs | Modifiables, calculés ou en lecture seule, selon l'état de l'objet |
| Valeurs | Catalogue autorisé et traitement des valeurs inconnues |
| Trace | Révision lue, changement demandé, résultat et réserves |

Cacher un bouton n'est pas un contrôle d'accès. Le mécanisme d'écriture doit vérifier les droits et les données, quelle que soit l'origine de la requête. L'interface, les contrôles d'écriture et le stockage ont des responsabilités distinctes ; leur réalisation technique dépend du contexte retenu.

## 3. Préparer, confirmer et relire

1. **Lire la bonne version** et garder sa révision.
2. **Préparer un changement borné**, avec les valeurs avant/après. Préserver le brouillon en cas d'erreur.
3. **Confirmer le contenu exact.** Une saisie modifiée après l'aperçu doit être réévaluée. Annuler ne déclenche pas d'écriture.
4. **Revérifier au moment d'écrire** les droits, valeurs, révision et conditions d'accès au fichier. En cas de conflit, ne pas écraser les changements intervenus.
5. **Enregistrer avec sauvegarde et trace**, sans altérer les parties non ciblées.
6. **Relire le résultat enregistré.** Une réponse réseau perdue ne prouve pas l'annulation : rechercher le résultat ou annoncer « enregistrement non confirmé ».

Un réessai ne doit pas répéter une modification déjà réalisée. Un redémarrage ne doit pas remplacer des éditions conservées par une ancienne copie. Ces comportements doivent être définis et testés, pas supposés.

## 4. Vérifier sur copie avant un usage réel

| Situation | Résultat attendu |
|---|---|
| Champ interdit ou valeur invalide | Refus explicite, source inchangée |
| Annulation | Aucune écriture |
| Saisie changée après l'aperçu | L'ancien aperçu ne permet pas d'appliquer le nouveau contenu |
| Source modifiée entre lecture et écriture | Conflit sans perte des changements intervenus |
| Classeur ouvert ailleurs | Comportement éprouvé dans l'application et l'environnement cibles |
| Réponse perdue, réessai ou redémarrage | Résultat réconcilié ou non confirmé, sans double modification |
| Enregistrement puis réouverture native | Valeurs et fonctions utiles conservées, sans réparation inattendue |
| Passage de l'essai au maître | Autorisation distincte et source courante sauvegardée ; pas de remplacement par une vieille copie |

Séparer tests automatisés, parcours dans l'application cible et acceptation humaine. Un formulaire compréhensible ne prouve pas la sécurité de son mécanisme d'écriture, ni l'inverse.

## Exercice proposé

L'étape dédiée du [scénario](../../examples/SCENARIO.md) demande seulement une proposition documentaire dans `atelier/`. Développer un éditeur, le déployer ou lui donner accès à un maître demande une décision et des contrôles distincts.
