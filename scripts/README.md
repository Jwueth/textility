# Ce que contrôlent les scripts

Python 3.10 ou plus récent, bibliothèque standard uniquement. Aucun appel réseau, installation, écriture de note ou activation d’agent. Lancer depuis la racine du dépôt :

```sh
python scripts/check_pack.py .
python -m unittest discover -s scripts -p "test_*.py" -v
```

Le premier programme émet un JSON `errors` et renvoie 0 si aucun écart couvert n’est détecté, 1 sinon. Un dossier absent est un écart. Le second exécute les tests dans des répertoires temporaires ; il ne fait pas agir un agent dans le mini-vault.

## Contrôles couverts

- Existence des cibles de liens Markdown relatifs simples, sans interroger les URLs externes ni vérifier les ancres de titres.
- Résolution des liens wiki utilisés dans le mini-vault, sans utiliser le vault parent. Les liens dans des exemples de code sont exclus. Les liens wiki hors mini-vault sont résolus dans le dossier fourni. Une cible explicite (`..`, chemin absolu) doit rester sous la racine de périmètre : une sortie est signalée, sans repli vers une note homonyme qui la masquerait. Les liens simples, fragments, alias et chemins relatifs internes restent acceptés.
- Valeurs et listes du frontmatter des huit notes gouvernées de l’exemple ; les fichiers d’accueil et de contrat sont exclus. Les modèles vides ne sont pas des documents instanciés. Une liste mal typée (`audience`, `sources` : objet, liste imbriquée, nombre) produit un diagnostic et un code de sortie 1, sans exception non rattrapée.
- Approbation avec acteur/date ; référence sans approbation ; cache dérivé sans source ; clés dupliquées et résidus d’approbation sur contenu non approuvé.
- Détection de quelques noms de fichiers d’état ou de données privées, et des liens symboliques dans le paquet. Les métadonnées Git et caches Python ne sont pas analysés.

## Portée volontairement limitée

Le parseur accepte le **sous-ensemble YAML du kit** : une clé par ligne, valeurs scalaires et listes JSON sur une ligne. Il n’est pas un parseur YAML général et ne doit pas servir à migrer un vault arbitraire. Il ne vérifie ni identité, ni vérité, ni qualité éditoriale, ni droit de publication.

Il ne contrôle pas toutes les combinaisons entre `type` et `authority`. Par exemple, vérifier qu’une décision approuvée porte bien l’autorité de référence reste un contrôle de cohérence documentaire. Les contraintes codées sont celles énumérées ci-dessus, pas l’ensemble de la convention.

Le résolveur de liens n’est pas une réimplémentation d’Obsidian : pas de validation de fragments, de rendu, d’alias de propriétés ou de tous les cas de noms de fichiers. Les liens simples de ce kit sont la cible des tests. Le confinement au périmètre est un contrôle lexical : il n’évalue pas les liens symboliques d’un chemin intermédiaire, et les liens symboliques du paquet restent refusés séparément. Les noms sensibles détectés ne couvrent pas toutes les données personnelles ou secrets possibles.

Les tests ajoutés pour ces deux corrections vérifient l’évasion explicite d’un wikilink et le typage des listes du frontmatter. Ils ne prouvent pas la conformité générale de la convention documentaire, ni l’absence d’autres évasions de chemin, ni la validité sémantique des valeurs permises.

Une sortie sans erreur signifie seulement que les contrôles listés n’ont pas trouvé d’écart. La revue des fichiers exacts, la recette native et l’autorisation de diffusion restent distinctes.
