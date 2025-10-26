# Task 06: Modifying RDF(s) — Complete solution aligned with validation.py

# 0) Imports and validator loader (uses the attached validation.py file)

from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS

import importlib.util, sys, os

validator_path = "validation.py"  # ensure this file is in the same folder
spec = importlib.util.spec_from_file_location("validation", validator_path)
validation = importlib.util.module_from_spec(spec)
sys.modules["validation"] = validation
spec.loader.exec_module(validation)
Report = validation.Report

# 1) Graph and namespaces (use the exact namespaces expected by the validator)
g = Graph()
PEOPLE = Namespace("http://oeg.fi.upm.es/def/people#")
PERSON = Namespace("http://oeg.fi.upm.es/resource/person/")
VCARD  = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")
FOAF   = Namespace("http://xmlns.com/foaf/0.1/")

g.namespace_manager.bind("people", PEOPLE, override=False)
g.namespace_manager.bind("person", PERSON, override=False)
g.namespace_manager.bind("vcard", VCARD, override=False)
g.namespace_manager.bind("foaf", FOAF, override=False)

r = Report()

# -----------------
# Task 6.1: Classes
# -----------------
# Required labels (exactly these) and subclass hierarchy:
#   Professor ⊑ Person
#   AssociateProfessor ⊑ Professor
#   InterimAssociateProfessor ⊑ AssociateProfessor
#   FullProfessor ⊑ Professor

# Declare classes
g.add((PEOPLE.Person, RDF.type, RDFS.Class))
g.add((PEOPLE.Professor, RDF.type, RDFS.Class))
g.add((PEOPLE.AssociateProfessor, RDF.type, RDFS.Class))
g.add((PEOPLE.InterimAssociateProfessor, RDF.type, RDFS.Class))
g.add((PEOPLE.FullProfessor, RDF.type, RDFS.Class))

# Labels (datatype must be xsd:string)
g.add((PEOPLE.Person, RDFS.label, Literal("Person", datatype=XSD.string)))
g.add((PEOPLE.Professor, RDFS.label, Literal("Professor", datatype=XSD.string)))
g.add((PEOPLE.AssociateProfessor, RDFS.label, Literal("AssociateProfessor", datatype=XSD.string)))
g.add((PEOPLE.InterimAssociateProfessor, RDFS.label, Literal("InterimAssociateProfessor", datatype=XSD.string)))
g.add((PEOPLE.FullProfessor, RDFS.label, Literal("FullProfessor", datatype=XSD.string)))

# Subclass relationships
g.add((PEOPLE.Professor, RDFS.subClassOf, PEOPLE.Person))
g.add((PEOPLE.AssociateProfessor, RDFS.subClassOf, PEOPLE.Professor))
g.add((PEOPLE.InterimAssociateProfessor, RDFS.subClassOf, PEOPLE.AssociateProfessor))
g.add((PEOPLE.FullProfessor, RDFS.subClassOf, PEOPLE.Professor))

# Validate Task 6.1
r.validate_task_06_01(g)

# --------------------
# Task 6.2: Properties
# --------------------
# Expected properties with exact labels and domain/range:
#   hasColleague: domain Person, range Person
#   hasName:      domain Person, range rdfs:Literal
#   hasHomePage:  domain FullProfessor, range rdfs:Literal

g.add((PEOPLE.hasColleague, RDF.type, RDF.Property))
g.add((PEOPLE.hasColleague, RDFS.label, Literal("hasColleague", datatype=XSD.string)))
g.add((PEOPLE.hasColleague, RDFS.domain, PEOPLE.Person))
g.add((PEOPLE.hasColleague, RDFS.range, PEOPLE.Person))

g.add((PEOPLE.hasName, RDF.type, RDF.Property))
g.add((PEOPLE.hasName, RDFS.label, Literal("hasName", datatype=XSD.string)))
g.add((PEOPLE.hasName, RDFS.domain, PEOPLE.Person))
g.add((PEOPLE.hasName, RDFS.range, RDFS.Literal))

g.add((PEOPLE.hasHomePage, RDF.type, RDF.Property))
g.add((PEOPLE.hasHomePage, RDFS.label, Literal("hasHomePage", datatype=XSD.string)))
g.add((PEOPLE.hasHomePage, RDFS.domain, PEOPLE.FullProfessor))
g.add((PEOPLE.hasHomePage, RDFS.range, RDFS.Literal))

# Validate Task 6.2
r.validate_task_06_02(g)

# --------------------
# Task 6.3: Individuals
# --------------------
# Must exist with labels "Oscar", "Asun", "Raul"
# Each individual URI must be in http://oeg.fi.upm.es/resource/person/
# Property counts must be EXACT:
#   Oscar: 4 predicates => rdf:type, rdfs:label, hasColleague, hasName
#   Asun:  4 predicates => rdf:type, rdfs:label, hasHomePage, hasColleague

oscar = PERSON.Oscar
asun  = PERSON.Asun
raul  = PERSON.Raul

# Types
g.add((oscar, RDF.type, PEOPLE.Person))
g.add((asun,  RDF.type, PEOPLE.FullProfessor))
g.add((raul,  RDF.type, PEOPLE.Person))

# Labels
g.add((oscar, RDFS.label, Literal("Oscar", datatype=XSD.string)))
g.add((asun,  RDFS.label, Literal("Asun", datatype=XSD.string)))
g.add((raul,  RDFS.label, Literal("Raul", datatype=XSD.string)))

# Exactly one colleague link for each (avoid duplicates to keep predicate count = 4)
g.add((oscar, PEOPLE.hasColleague, asun))
g.add((asun,  PEOPLE.hasColleague, oscar))

# Name and homepage (as plain literals; validator checks only predicate presence)
g.add((oscar, PEOPLE.hasName, Literal("Oscar", datatype=XSD.string)))
g.add((asun,  PEOPLE.hasHomePage, Literal("http://example.org/asun")))

# Validate Task 6.3
r.validate_task_06_03(g)

# --------------------
# Task 6.4: Person data
# --------------------
# Add to Oscar the VCARD.Given, VCARD.Family, and FOAF.email properties
# (values as literals; validator checks predicate namespaces only)

g.add((oscar, VCARD.Given,  Literal("Oscar", datatype=XSD.string)))
g.add((oscar, VCARD.Family, Literal("Corcho", datatype=XSD.string)))
g.add((oscar, FOAF.email,   Literal("oscar@upm.es", datatype=XSD.string)))

# Validate Task 6.4
r.validate_task_06_04(g)

# Optional: save report
r.save_report("_Task_06")

print("All Task 06 validations attempted. Check the generated report file for details.")
