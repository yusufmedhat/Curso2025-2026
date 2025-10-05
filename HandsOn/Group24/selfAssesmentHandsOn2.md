# Self-Assessment — Hands-On 2 (Group24)

## Tasks completed
- Analysed the three CSV datasets (schema, quantities, value ranges).
- Reviewed licensing at source and defined a compatible license for generated RDF (CC BY 4.0).
- Defined a Resource Naming Strategy (base domain, URI patterns, content negotiation plan).
- Developed a lightweight ontology in Turtle (`ontology/urban-env-ontology.ttl`).
- Created a sample RDF instantiation (`ontology/urban-env-example.ttl`) aligned with the naming strategy.

## What went well
- Reused standard vocabularies (SOSA/SSN, DCAT) to maximize interoperability.
- Kept the ontology small and focused (clear classes/properties and datatypes).
- URI patterns are predictable and stable (dataset scope + stable codes like `SEZ2011`, ISO codes, year).

## Challenges
- Some CSV exports lacked explicit spatial identifiers (e.g., empty “Territorio”), reducing linkability.
- Normalizing units and concepts across heterogeneous datasets (NO2 vs. expenditure vs. green index).
- Selecting the right level of granularity for observations (annual vs. daily).
