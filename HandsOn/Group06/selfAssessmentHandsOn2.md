# Hands-on 2 — Self-Assessment (Group06)

## What went well
- We successfully selected and analyzed two compatible datasets: *Arbolado en parques y zonas verdes de Madrid* and *Zonas Verdes de Madrid (2024)*.
- The datasets were well structured, clearly documented, and both provided open CSV formats with proper licenses.
- We defined a simple and consistent ontology that connects tree species, parks, and green areas through spatial relationships.
- The team collaborated effectively by dividing tasks (dataset analysis, ontology design, and HTML documentation) and reviewing each other’s work.
- We were able to reuse parts of the previous hands-on structure (requirements and HTML templates) to maintain consistency.

## What was challenging
- Understanding and aligning the attributes of both datasets was complex, since they describe related but different environmental entities.
- Some attribute names in Spanish required translation and interpretation for RDF modeling.
- Designing an ontology that was specific enough for our use case but still compatible with existing vocabularies (e.g., GeoSPARQL, FOAF) took time.
- Ensuring license compatibility and correct attribution required checking the data portals carefully.

## Next steps
- Implement the RDF transformation using OpenRefine or Python scripts based on the designed ontology.
- Reconcile entities such as park names, species, and districts with external datasets like Wikidata and DBpedia.
- Validate the RDF files using SHACL or other quality assessment tools before publishing.
- Publish the datasets online with persistent URIs following the linked data principles.

## Checklist
- [x] README.md updated with all group members
- [x] analysis.html including data analysis, licensing information, resource naming strategy, and ontology overview
- [x] ontology/ontology.ttl containing the lightweight ontology in Turtle syntax
- [x] ontology/example.ttl containing a sample RDF instantiation using the ontology
- [x] selfAssessmentHandsOn2.md (this file)

