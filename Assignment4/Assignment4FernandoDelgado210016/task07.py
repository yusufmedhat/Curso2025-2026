# -*- coding: utf-8 -*-
"""
Task07_2025.py
Querying RDF(s) for Assignment 4
"""

# !pip install rdflib  # comentado para entrega

from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS
from validation import Report

# Cargar el grafo
g = Graph()
ns = Namespace("http://oeg.fi.upm.es/def/people#")
g.namespace_manager.bind('ns', ns, override=False)

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials"
g.parse(github_storage + "/rdf/data06.ttl", format="TTL")

report = Report()

# -----------------------------------------------------
# 7.1a: RDFLib classes
# -----------------------------------------------------
result = []
for c in g.subjects(RDF.type, RDFS.Class):
    sc = g.value(subject=c, predicate=RDFS.subClassOf)
    result.append((c, sc if sc else None))
report.validate_07_1a(result)

# -----------------------------------------------------
# 7.1b: SPARQL
# -----------------------------------------------------
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?c ?sc
WHERE {
  ?c rdf:type rdfs:Class .
  OPTIONAL { ?c rdfs:subClassOf ?sc }
}
"""
report.validate_07_1b(query, g)

# -----------------------------------------------------
# 7.2a: Individuals of Person (RDFLib)
# -----------------------------------------------------
# incluir individuos de Person y de todas sus subclases
individuals = set()
for ind, t in g.subject_objects(RDF.type):
    # comprobar si el tipo es Person o subclase de Person
    if (t, RDFS.subClassOf, ns.Person) in g or t == ns.Person:
        individuals.add(ind)
report.validate_07_02a(list(individuals))

# -----------------------------------------------------
# 7.2b: SPARQL
# -----------------------------------------------------
query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?ind
WHERE {
  ?ind rdf:type/rdfs:subClassOf* ns:Person .
}
"""
report.validate_07_02b(g, query)

# -----------------------------------------------------
# 7.3: Name and type of those who know Rocky
# -----------------------------------------------------
query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
SELECT ?name ?type
WHERE {
  ?s ns:hasColleague ns:Rocky .
  ?s ns:hasName ?name .
  ?s rdf:type ?type .
}
"""
report.validate_07_03(g, query)

# -----------------------------------------------------
# 7.4: Name of entities with colleague who has a dog
# -----------------------------------------------------
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
report.validate_07_04(g, query)

# -----------------------------------------------------
# Save report
# -----------------------------------------------------
report.save_report("_Task_07")
