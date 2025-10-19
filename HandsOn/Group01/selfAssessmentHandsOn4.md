# Self-Assessment — Hands-on 4 (GroupXX)

## 1. Overview
This submission transforms two TMB CSV datasets (metro **lines** and **stations per line**) into RDF using **RML/YARRRML mappings**, generating a Turtle file with the transformed data.

## 2. Files delivered
```
HandsOn/GroupXX/
├── mappings/
│   ├── metro_mapping.rml
│   └── metro_mapping.yml        # optional (YARRRML equivalent)
├── rdf/
│   ├── metro_data.ttl           # REQUIRED (RDF data in Turtle)
│   └── queries.sparql           # REQUIRED (verification queries)
└── selfAssessmentHandsOn4.md    # this document
```

## 3. Datasets
- `linies_metro.csv` — Metro lines metadata (id, code, name, colors, geometry).
- `estacions_linia.csv` — Stations per line (station id/name, line id, order, geometry).

## 4. Ontology
We rely on `ontology.ttl` which defines:
- Classes: `metro:MetroLine`, `metro:Station`, `metro:StationLine`
- Properties: `metro:hasStation`, `metro:hasLine`, `metro:stationOrder`, `metro:lineName`, `metro:lineColor`, etc.
Namespace used across mappings: `https://data.example.org/transport/bcn/metro/ontology#`.

## 5. Mapping summary
- **RML** (`mappings/metro_mapping.rml`) and **YARRRML** (`mappings/metro_mapping.yml`) map:
  - Lines → resources `ex:line/{ID_LINIA}` with labels, colors, (optional) description and geometry.
  - Stations → resources `ex:station/{ID_ESTACIO}` with names and geometry.
  - Relationship:
    - `metro:hasStation` (Line → Station)
    - `metro:hasLine` (Station → Line) (reverse link)
    - `metro:StationLine` resource to preserve `metro:stationOrder` along each line.

## 6. How requirements are met (FR1–FR6)
- **FR1** — Lines on map: `metro:MetroLine` + `metro:hasGeometry`.
- **FR2** — Stations on map: `metro:Station` + `metro:hasGeometry`.
- **FR3** — Lines per station: `metro:hasLine` (from Station) and `metro:hasStation` (from Line).
- **FR4** — Station details: `metro:stationId`, `metro:stationName`, `metro:hasGeometry`.
- **FR5** — Number of stops in a line: `metro:hasStation` with query `Q1` (COUNT).
- **FR6** — Line details: name/code/colors/origin/dest + station count with `Q5`.

## 7. Execution notes
- **Option A – Morph-KGC** (Python):
  1. Install: `pip install morph-kgc`
  2. Run with RML:
     ```bash
     morph-kgc -m mappings/metro_mapping.rml -o rdf/metro_data.ttl
     ```
  3. Or from YARRRML (if preferred):
     - Convert YARRRML → RML (e.g., using `yarrrml-parser`) or run through a compatible tool.
- **Option B – RMLMapper** (Java):
  ```bash
  java -jar rmlmapper.jar -m mappings/metro_mapping.rml -o rdf/metro_data.ttl
  ```

## 8. Queries
Provided in `rdf/queries.sparql`. Cover FR1–FR6:
- Q0: Lines (id, code, name, color)
- Q1: Station count per line
- Q2: Stations of a line ordered
- Q3: Lines serving a station
- Q4: Station details
- Q5: Line details + station count
- Q6: Station → Lines (compact list)

## 9. Assumptions and limitations
- Geometry is stored as a text literal via `metro:hasGeometry` (no GeoSPARQL reasoning assumed).
- Only columns required for FR1–FR6 were mapped. Extra attributes (operator, accessibility, etc.) can be added later without breaking the model.
- The namespace `https://data.example.org/transport/bcn/metro/` is a placeholder and can be replaced by the course repository domain if provided.

## 10. Future work (optional)
- Add GeoSPARQL compliance (`geo:asWKT`) and CRS definition.
- Extend mappings for operator/family/accessibility metadata.
- Publish dereferenceable IRIs and VoID/DCAT metadata.
- Provide SHACL shapes for data validation.
