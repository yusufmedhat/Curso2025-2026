# Checklist  
## Assignment 4 – CSV ➜ RDF Transformation with RML  
**Group 20 – Web Semantics 2025**

---

### 📁 `mapping` directory  

#### 📄 `mapping.rml.ttl`  
- [x] Contains two `rr:TriplesMap`s: `ParkingTM` and `LocationTM`  
- [x] Source declared as `rml:source "csv/parkings-updated.csv"`  
- [x] Generates URIs following the pattern `http://group20.linkeddata.es/parkings/resource/{id}`  
- [x] Correctly typed literals using `xsd:integer`, `xsd:double`, `xsd:boolean`, `xsd:string`  
- [x] Links parkings and locations through `rr:parentTriplesMap` and `rr:joinCondition` on `id`  
> [Open mapping.rml.ttl](./mapping/mapping.rml.ttl)

---

### 📁 `rdf` directory  

#### 📄 `parkings.ttl`  
- [x] Generated from the RML mapping using RMLMapper 8.0.0  
      "java -jar ..\rmlmapper-8.0.0-r378-all.jar -m ..\mappings\mapping.rml.ttl -o ..\rdf\parkings.ttl" from 📁`csv` directory
- [x] Valid RDF in Turtle syntax (validated with `riot --validate`)  
- [x] Contains all instances of `ns:Parking` and `ns:Location`  
- [x] Data types and IRIs correctly generated  
> [Open parkings.ttl](./rdf/parkings.ttl)

#### 📄 `queries.sparql`  
- [x] Includes SPARQL queries used to verify the generated RDF  
  - List first 10 parkings (id, name, address)  
  - List parkings where `ns:isEMTParking = true`  
  - Count total parkings  
  - Count parkings whose address contains “plaza”  
- [x] All queries tested successfully with `rdflib` and `arq`  
> [Open queries.sparql](./rdf/queries.sparql)



