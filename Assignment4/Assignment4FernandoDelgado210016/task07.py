# -*- coding: utf-8 -*-
"""
Task07_2025.py
Querying RDF(s) for Assignment 4
"""

# !pip install rdflib  # comentado para entrega

from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS, FOAF
from validation import Report

g = Graph()

# Namespaces
ns = Namespace("http://oeg.fi.upm.es/def/people#")
PERSON_NS = Namespace("http://oeg.fi.upm.es/resource/person/")
g.namespace_manager.bind('ns', ns, override=False)

# Cargar RDF
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials"
g.parse(github_storage + "/rdf/data06.ttl", format="TTL")

report = Report()

# ----------------------
# Task 7.1a: RDFLib classes
# ----------------------
result = []
for c in g.subjects(RDF.type, RDFS.Class):
    sc = g.value(subject=c, predicate=RDFS.subClassOf)
    result.append((c, sc if sc else None))
report.validate_07_1a(result)

# ----------------------
# Task 7.1b: SPARQL
# ----------------------
query = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?c ?sc
WHERE {
  ?c rdf:type rdfs:Class .
  OPTIONAL { ?c rdfs:subClassOf ?sc }
}
"""
for r in g.query(query):
    print(r.c, r.sc)
report.validate_07_1b(query, g)

# ----------------------
# Task 7.2a: Individuals of Person (RDFLib)
# ----------------------
# Recupera solo los individuos con el namespace correcto
individuals = [i for i in g.subjects() if str(i).startswith(str(PERSON_NS))]
report.validate_07_02a(individuals)

# ----------------------
# Task 7.2b: SPARQL
# ----------------------
query = """
PREFIX person: <http://oeg.fi.upm.es/resource/person/>
SELECT ?ind
WHERE {
  ?ind a ?type .
  FILTER(STRSTARTS(STR(?ind), STR(person:)))
}
"""
for r in g.query(query):
    print(r.ind)
report.validate_07_02b(g, query)

# ----------------------
# Task 7.3: Name and type of those who know Rocky
# ----------------------
query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
SELECT ?name ?type
WHERE {
  ?s ns:hasColleague ns:Rocky .
  ?s ns:hasName ?name .
  ?s rdf:type ?type .
}
"""
for r in g.query(query):
    print(r.name, r.type)
report.validate_07_03(g, query)

# ----------------------
# Task 7.4: Name of entities with colleague who has a dog
# ----------------------
query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
SELECT ?name
WHERE {
  ?x ns:hasColleague ?y .
  ?y ns:hasPet ?pet .
  ?pet rdf:type ns:Dog .
  ?x ns:hasName ?name .
}
"""
for r in g.query(query):
    print(r.name)
report.validate_07_04(g, query)

# ----------------------
# Save report
# ----------------------
report.save_report("_Task_07")


