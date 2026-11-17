# Module optionnel — classeur maître et projection

**Données entièrement fictives, créées pour cet exercice.** Ce module illustre la [méthode](../../docs/06-classeur-maitre.md) sur les quatre informations de prêt du [scénario](../../examples/SCENARIO.md). Le choix du XLSX est proposé pour l'exercice ; aucune décision du collectif n'est ajoutée à ses notes historiques.

## Lire sans exécuter de code

- [maitre-prets-demo.xlsx](maitre-prets-demo.xlsx) : ouvrir une copie avec un tableur compatible. `LIRE` contient le mode d'emploi ; `Prets` contient trois opérations inventées ; `Journal` est une trame vide.
- [prets-generes.md](prets-generes.md) : vue déjà produite des seules lignes de `Prets`. L'empreinte indiquée permet de l'associer à la version exacte du XLSX.

Le registre des transactions ne remplace pas les registres de gouvernance. La durée de conservation reste non décidée. Une cellule renseignée ne valide pas une règle ; aucun statut métier supplémentaire n'est introduit. Les trois transactions n'ont pas d'ID stable : ce modèle ne suffit pas pour rapprocher automatiquement des versions ou gérer des prêts récurrents.

## Dépendances de l'outillage seulement

Les scripts de ce dossier requièrent Python 3.10+ et `openpyxl`, fixé à la version exercée dans [requirements.txt](requirements.txt). Le socle documentaire et les sept tests de `scripts/` restent en bibliothèque standard. Le fichier XLSX lui-même ne requiert pas une bibliothèque Python.

Pour choisir d'exécuter le module, utiliser un environnement de test isolé et installer explicitement ses dépendances selon les règles de son poste. Par exemple, avec **le Python de cet environnement** :

```sh
python -m pip install -r modules/classeur-maitre/requirements.txt
```

Cette commande contacte un registre de paquets. La lecture du guide ou du scénario n'autorise aucune installation automatique. Aucune dépendance n'est installée au simple lancement de l'exporteur.

## Reproduire la projection sur copie

Depuis la racine d'une copie indépendante du kit, créer un dossier `atelier/` vide et autoriser ces sorties seulement. Si `python` s'appelle `python3`, adapter le nom.

```sh
python modules/classeur-maitre/export_markdown.py modules/classeur-maitre/maitre-prets-demo.xlsx atelier/prets.md
python -m unittest discover -s modules/classeur-maitre -p "test_*.py" -v
```

L'exporteur lit un instantané des octets enregistrés, contrôle le format attendu et crée la destination. **Il refuse un fichier de sortie existant**, y compris le classeur lui-même. Choisir un nom neuf pour chaque révision : il n'existe pas d'option d'écrasement. Il n'y a ni écriture XLSX, ni synchronisation inverse, ni publication. Une erreur ne remet pas l'ancienne vue à jour ; conserver celle-ci comme historique, pas comme preuve de fraîcheur.

L'export est déterministe pour un même fichier source : pas de date de génération mouvante. Une modification du contenu, des styles ou un simple réenregistrement peut changer l'empreinte du XLSX et donc le bandeau, même si les lignes de prêt sont identiques. Comparer séparément le bandeau de provenance et les lignes de données ; ne pas attribuer un changement à une personne depuis le seul hash.

## Régénérer un exemplaire neuf, pas le maître livré

```sh
python modules/classeur-maitre/build_demo.py atelier/maitre-neuf.xlsx
python modules/classeur-maitre/export_markdown.py atelier/maitre-neuf.xlsx atelier/prets-neufs.md
```

Le générateur refuse lui aussi une destination existante. Il reproduit les cellules et la structure de l'exemple, pas nécessairement des octets ZIP identiques. Générer à nouveau ne teste pas l'entretien d'un maître vivant et ne doit pas effacer des modifications humaines.

## Ce que l'exporteur traite

- Onglets et quatre en-têtes attendus ; données textuelles et dates réelles de tableur.
- Toutes les lignes de données, **même masquées ou filtrées**. Un filtre n'est pas une permission d'export ou d'anonymisation.
- Lignes entièrement vides ignorées ; noms d'objets répétés possibles.
- Refus des champs manquants, formules dans `Prets`, colonnes non prévues remplies et dates incohérentes. Aucune valeur n'est réparée silencieusement.
- Échappement des caractères de table Markdown et du HTML. Ni les styles, ni le journal, ni les validations du classeur ne sont exportés.

Il ne s'agit pas d'un convertisseur universel ni d'une sandbox pour des classeurs non fiables. Les contrôles concernent cet exemple borné ; ils ne valident ni le fond métier ni la sécurité de tout document bureautique.

## Contrôles de cette préparation locale

- Sept tests du socle exécutés sans paquets tiers ; neuf tests propres au module réussis, avec quatre cas de données invalides dans un test paramétré.
- Projection livrée reproduite à l'identique depuis les octets du XLSX ; refus d'écrasement, source égale à destination, champs absents, dates incohérentes, formules et colonnes supplémentaires contrôlés. Lignes masquées et noms d'objets répétés exercés.
- Essai borné sur copie : seul `Prets!D2` passe du 19 au 20 janvier 2026 ; seule la ligne correspondante change dans les données projetées, en plus du bandeau de provenance. La source livrée reste inchangée.

Ces résultats techniques ne sont ni une recette Microsoft Excel, ni une acceptation humaine, ni une preuve d'édition concurrente. Ils ne démontrent pas la qualité visuelle des supports.

## Recette humaine à compléter

Sur une copie : ouvrir le XLSX dans l'application cible, vérifier les trois onglets et les dates, modifier un retour prévu, enregistrer, fermer puis rouvrir. Contrôler la valeur conservée et produire une nouvelle projection sous un nom neuf. Vérifier qu'une retouche de la vue Markdown ne change pas le XLSX et qu'un second export vers une destination occupée est refusé.

Les tests Python et un éventuel aperçu PDF ne prouvent pas cette recette Microsoft Excel. Le [scénario](../../examples/SCENARIO.md) sépare l'essai technique du choix humain d'adopter ou non ce mode de travail.
