# -*- coding: utf-8 -*-
# Task 07: RDFLib + SPARQL queries with validation

# 0) Setup: install rdflib and load the validator the notebook/script expects
#!pip install rdflib -q

import urllib.request

url = 'https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/refs/heads/master/Assignment4/course_materials/python/validation.py'
urllib.request.urlretrieve(url, 'validation.py')

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials"
print("✅ rdflib installed and validation script downloaded.")

from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS
from validation import Report

# 1) Create graph and parse TTL file
g = Graph()

# Bind the common namespace used in the course (helps pretty-printing)
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)

# Download/parse the data file from the repo
data_url = github_storage + "/rdf/data06.ttl"

try:
    g.parse(data_url, format="ttl")
    print("✅ Parsed TTL directly from remote repo.")
except Exception as e:
    # Fallback: download to local file then parse
    print("⚠️ Could not parse directly from URL (likely network rule). Falling back to local download:", str(e))
    urllib.request.urlretrieve(data_url, 'data06.ttl')
    g.parse('data06.ttl', format="ttl")
    print("✅ Parsed data06.ttl from local file.")

report = Report()
print("✅ Graph loaded. Triples in graph:", len(g))

# -----------------------
# Task 7.1a (RDFLib API)
# -----------------------
# List all classes with their (direct) superclasses, or None if they have no rdfs:subClassOf.
result = []
for s in g.subjects(RDF.type, RDFS.Class):
    superclasses = list(g.objects(s, RDFS.subClassOf))
    if superclasses:
        for sc in superclasses:
            result.append((s, sc))
    else:
        result.append((s, None))

print("\n--- Task 7.1a (RDFLib) results ---")
for r in result:
    print(r)

print("\nRunning validator for 7.1a ...")
report.validate_07_1a(result)
print("✅ Validation 7.1a completed.")

# ------------------------
# Task 7.1b (SPARQL query)
# ------------------------
# Classes with optional direct superclass
query_71b = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?c ?sc
WHERE {
  ?c a rdfs:Class .
  OPTIONAL { ?c rdfs:subClassOf ?sc . }
}
"""

print("\n--- Task 7.1b (SPARQL) results ---")
for row in g.query(query_71b):
    print(row.c, row.sc)

print("\nRunning validator for 7.1b ...")
report.validate_07_1b(query_71b, g)
print("✅ Validation 7.1b completed.")

# --------------------------------
# Task 7.2a (RDFLib): Individuals
# --------------------------------
# All individuals of people:Person and any of its subclasses.
ns_people = Namespace("http://oeg.fi.upm.es/def/people#")

def get_subclasses(cls, graph):
    subclasses = set()
    for sub in graph.subjects(RDFS.subClassOf, cls):
        if sub not in subclasses:
            subclasses.add(sub)
            subclasses |= get_subclasses(sub, graph)
    return subclasses

person_and_subs = {ns_people.Person} | get_subclasses(ns_people.Person, g)

individuals = []
seen = set()
for cls in person_and_subs:
    for ind in g.subjects(RDF.type, cls):
        if ind not in seen:
            seen.add(ind)
            individuals.append(ind)

print("\n--- Task 7.2a (RDFLib) individuals ---")
for ind in individuals:
    print(ind)

print("\nRunning validator for 7.2a ...")
report.validate_07_02a(individuals)
print("✅ Validation 7.2a completed.")

# ------------------------
# Task 7.2b (SPARQL query)
# ------------------------
# Individuals that are instances of people:Person or any subclass (via rdfs:subClassOf*).
query_72b = """
PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
PREFIX people: <http://oeg.fi.upm.es/def/people#>

SELECT DISTINCT ?ind
WHERE {
  ?ind a ?class .
  ?class rdfs:subClassOf* people:Person .
}
"""

print("\n--- Task 7.2b (SPARQL) results ---")
for row in g.query(query_72b):
    print(row.ind)

print("\nRunning validator for 7.2b ...")
report.validate_07_02b(g, query_72b)
print("✅ Validation 7.2b completed.")

# ------------------------
# Task 7.3 (SPARQL query)
# ------------------------
# For every subject that foaf:knows someone, return its foaf:name and rdf:type.
query_73 = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?name ?type
WHERE {
  ?s foaf:knows ?o .
  ?s foaf:name ?name .
  ?s a ?type .
}
"""

print("\n--- Task 7.3 (SPARQL) results ---")
for row in g.query(query_73):
    print(row.name, row.type)

print("\nRunning validator for 7.3 ...")
report.validate_07_03(g, query_73)
print("✅ Validation 7.3 completed.")

# ------------------------
# Task 7.4 (SPARQL query)
# ------------------------
# Names of people reachable via one-or-more people:hasColleague hops who have a pet that is an animals:Dog.
query_74 = """
PREFIX people:  <http://oeg.fi.upm.es/def/people#>
PREFIX animals: <http://oeg.fi.upm.es/def/animals#>
PREFIX foaf:    <http://xmlns.com/foaf/0.1/>

SELECT DISTINCT ?name
WHERE {
  ?x foaf:name ?name .
  ?x (people:hasColleague)+ ?y .
  ?y people:hasPet ?dog .
  ?dog a animals:Dog .
}
"""

print("\n--- Task 7.4 (SPARQL) results ---")
for row in g.query(query_74):
    print(row.name)

print("\nRunning validator for 7.4 ...")
report.validate_07_04(g, query_74)
report.save_report("_Task_07")
print("✅ Validation 7.4 completed and report saved as _Task_07")
