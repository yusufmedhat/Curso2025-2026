# -*- coding: utf-8 -*-
"""
Task07_2025.py
Querying RDF(s) for Assignment 4
"""

# !pip install rdflib  # comentado para entrega

from rdflib import Graph, Namespace
from validation import Report
from rdflib.namespace import RDF, RDFS

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials"
g.parse(github_storage+"/rdf/data06.ttl", format="TTL")
report = Report()

# 7.1a: RDFLib classes
result = []
for c in g.subjects(RDF.type, RDFS.Class):
    sc = g.value(subject=c, predicate=RDFS.subClassOf)
    result.append((c, sc if sc else None))
report.validate_07_1a(result)

# 7.1b: SPARQL
query = """
SELECT ?c ?sc
WHERE {
  ?c rdf:type rdfs:Class .
  OPTIONAL { ?c rdfs:subClassOf ?sc }
}
"""
for r in g.query(query):
    print(r.c, r.sc)
report.validate_07_1b(query, g)

# 7.2a: Individuals of Person (RDFLib)
ns = Namespace("http://oeg.fi.upm.es/def/people#")
individuals = [i for i in g.subjects(RDF.type, ns.Person)]
report.validate_07_02a(individuals)

# 7.2b: SPARQL
query = """
SELECT ?ind
WHERE {
  ?ind rdf:type/rdfs:subClassOf* foaf:Person .
}
"""
for r in g.query(query):
    print(r.ind)
report.validate_07_02b(g, query)

# 7.3: Name and type of those who know Rocky (SPARQL)
query = """
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

# 7.4: Name of entities with colleague who has a dog (SPARQL)
query = """
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

report.save_report("_Task_07")
