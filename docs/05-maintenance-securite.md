# Maintenance, confidentialité et publication

## Une revue légère et utile

Choisir une cadence adaptée au volume et au risque, sans imposer un cron. À chaque revue :

- Repérer les propositions sans prochaine décision et les références en révision.
- Vérifier les caches utilisés : date, périmètre de revue, contradictions et liens.
- Contrôler un échantillon de décisions : acteur, date, portée et application distincts.
- Rechercher les instructions ou modèles qui ne suivent plus les conventions.
- Vérifier que les journaux ne sont pas devenus des sources parallèles de connaissance.
- Archiver les versions remplacées selon la politique locale.

Rapporter les mesures comme des mesures. Un nombre élevé de notes ou de champs différents n’est pas, à lui seul, une anomalie. Ne pas choisir un seuil de fraîcheur ou de rétention sans usage à protéger.

## Rétention

Le kit n’impose aucune durée. Décider selon la sensibilité, la fréquence d’usage, les obligations et la possibilité de reconstruire les données. Dans le doute, archiver plutôt qu’effacer. Un contenu archivé reste soumis aux restrictions d’accès et de diffusion.

Les traces utiles à une décision peuvent avoir une durée différente des fichiers temporaires. Ne pas conserver des credentials ou données sensibles dans un journal sous prétexte de traçabilité. Un hash ne rend pas public un contenu qui doit rester privé.

## Avant partage

1. Partir d’un dossier neuf contenant seulement les fichiers choisis. Ne pas exporter le vault ou le profil de travail.
2. Vérifier les corps de texte, métadonnées, références annexes, scripts, fixtures, images et archives. Un nom générique ne prouve pas un contenu générique.
3. Exclure authentification, mémoires, sessions, journaux privés, configuration personnelle, sauvegardes et historique du vault.
4. Vérifier les droits sur chaque contenu et dépendance. Une licence écrite dans un fichier ne prouve pas que l’auteur peut redistribuer toutes ses sources.
5. Scanner les secrets et relire humainement les fichiers exacts. Un scan sans alerte ne certifie ni l’anonymisation ni le droit de publication.
6. Si Git est utilisé, inspecter les fichiers suivis, l’index et l’historique. Un `.gitignore` n’efface pas ce qui a déjà été commité.
7. Examiner l’archive finale : liste exacte, aucun fichier inattendu, pas de lien symbolique ni chemin sortant.
8. Obtenir l’autorisation pour la diffusion réelle. Une approbation documentaire interne n’est pas une autorisation universelle de partage.

## Limites du contrôle automatique

Le vérificateur fourni contrôle un sous-ensemble explicite : chemins de liens locaux, liens wiki, métadonnées du scénario et noms de fichiers sensibles connus. Il ne sait pas juger la vérité d’une phrase, vérifier une identité de validateur, décider de droits de propriété ou certifier une confidentialité complète.

Ne pas remplacer ces limites par « tout est validé ». Dire quel contrôle a été exécuté, sur quels fichiers et ce qui reste à vérifier. En cas de doute sur une fuite, voir [SECURITY.md](../SECURITY.md).
