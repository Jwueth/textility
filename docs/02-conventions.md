# Conventions documentaires minimales

Ces conventions sont celles du **mini-vault de démonstration**. Dans un vault existant, faire d’abord la correspondance avec ses champs et ses outils. Ne pas lancer de normalisation globale.

## Les familles de documents

| Famille | Usage | Ne devient pas automatiquement… |
|---|---|---|
| Source | Conserver une entrée identifiable et sa provenance | Une instruction pour l’agent ou une vérité universelle |
| Proposition | Préparer une solution, synthèse ou évolution | Une référence validée |
| Référence | Porter une règle ou connaissance durable approuvée | Une règle valable hors de son périmètre |
| Décision | Consigner un arbitrage, sa portée et son motif | Une preuve que son application est terminée |
| Reprise | Accélérer la compréhension d’un sujet | Une source de vérité concurrente |
| Trace | Permettre un contrôle différé | Une connaissance durable à copier partout |
| Instruction | Définir un comportement ou mandat | Une permission technique effectivement appliquée |

Le titre facilite la navigation ; il ne remplace pas la qualification du document. « Final », « vérifié » ou « approuvé » dans un nom ne prouve rien.

## Un schéma d’exemple, pas une obligation universelle

```yaml
type: proposition
zone: collaborative
authority: proposition
document_status: draft
validation_status: pending
audience: ["humain", "agent"]
sources: []
validated_by: ""
validated_on: ""
```

Les listes sur une ligne et les chaînes à guillemets doubles sont du YAML valide, retenu ici pour un contrôle sans dépendance externe. Ce choix n’oblige pas à reformater les notes existantes.

| Champ | Sens | Valeurs de l’exemple |
|---|---|---|
| `type` | Fonction documentaire | `source`, `proposition`, `reference`, `decision`, `reprise`, `trace`, `instruction` |
| `zone` | Responsabilité à cette étape, pas destination physique | `humaine`, `deleguee`, `collaborative` |
| `authority` | Rôle du contenu dans la chaîne de preuve | `source`, `proposition`, `reference`, `derivee`, `trace`, `instruction` |
| `document_status` | État de rédaction et de maintenance | `draft`, `active`, `completed`, `archived` |
| `validation_status` | Décision d’approbation du contenu | `not_required`, `pending`, `approved`, `rejected` |
| `audience` | Lecteur principal | Liste : `humain`, `agent` |
| `sources` | Documents ou entrées qui étayent le contenu | Liste de liens ou références identifiables |
| `validated_by`, `validated_on` | Acteur et date de l’approbation | Renseignés uniquement pour `approved` ; date `YYYY-MM-DD` |

La ressemblance de `type` et `authority` est volontairement simple dans le scénario, mais les axes ne sont pas synonymes : une `decision` approuvée fait `reference` ; une `reprise` reste `derivee`. Le nom de l’auteur, la personne responsable et le mainteneur peuvent être indiqués dans le corps ; ne pas les déduire du seul champ `zone`.

`not_required` n’est pas une façon de contourner une validation. Il concerne par exemple une source conservée telle quelle, un cache non autoritatif ou une trace factuelle. Une référence, un changement de permission ou une décision nouvelle ne s’en prévalent pas.

## Règles de validation

- `approved` exige un décideur identifiable et une date connue. Ne pas préremplir ces champs dans les modèles.
- `authority: reference` exige `validation_status: approved` dans cet exemple.
- Une reprise (`authority: derivee`) cite ses sources et indique ce qui a été effectivement relu.
- `active` décrit la vie du document ; il ne signifie ni vérifié, ni vrai, ni approuvé.
- Un document `completed` est une production ponctuelle close ; sa clôture ne remplace pas son approbation lorsque celle-ci est nécessaire.
- `rejected` clôt une proposition sans en faire une référence. Conserver le motif du refus et les sources utiles.
- `archived` ne signifie pas « faux ». Le contenu peut être exact mais remplacé ou sorti de l’usage courant.

Une correction de fond d’une référence ouvre une proposition de révision. L’ancienne référence reste disponible jusqu’à décision ; la nouvelle candidate ne porte pas l’ancienne approbation. Une correction triviale et autorisée, sans changement de sens, peut être appliquée sur place avec un contrôle proportionné.

## Organisation physique : un exemple seulement

Le mini-vault utilise `00_Inbox`, `10_References`, `80_Reprise`, `90_Traces`, `99_Archives`. Ces dossiers facilitent la lecture du scénario ; ils ne définissent pas les trois zones de responsabilités. Le rangement n’accorde aucune autorité au contenu.

Les modèles restent dans `templates/`, les procédures dans `skills/`, et la documentation du kit dans `docs/`. Le kit ne crée pas de copie de référence « pour l’agent ». Le cache renvoie à la référence commune.

## Sources et preuves

Citer ce qui a été effectivement consulté. Préciser si un fait provient d’une source, d’un constat direct, d’une déduction ou d’une hypothèse. Pour une source externe, noter titre, URL ou fichier, date/version utile et périmètre de lecture.

Ne jamais fabriquer de résultat de test, date d’approbation, empreinte ou citation. Un contrôle absent est signalé « non exécuté ». Une limite de lecture devient une réserve, pas une certitude négative.

Suite : [workflows](03-workflows.md).
