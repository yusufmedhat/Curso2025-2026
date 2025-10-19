# validation.py
# -------------------------------------------------------------
# Validation script for Assignment 4 (Curso2025-2026)
# DO NOT MODIFY THIS FILE.
# -------------------------------------------------------------

from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import FOAF, XSD
import inspect

def validate_task(graph=None):
    """
    This function validates the content of your task file
    by checking the presence of expected triples and namespaces.
    """

    # 1. Check that a Graph is provided
    if graph is None or not isinstance(graph, Graph):
        print("❌ No RDFLib Graph found. Please ensure 'g = Graph()' exists and is used.")
        return False

    # 2. Check namespaces
    namespaces = [prefix for prefix, uri in graph.namespaces()]
    if "ex" not in namespaces:
        print("❌ Missing 'ex' namespace binding.")
        return False

    # 3. Check that at least one FOAF.Person triple exists
    if (None, RDF.type, FOAF.Person) not in graph:
        print("❌ No FOAF.Person triple found.")
        return False

    # 4. Check for literals (some property must have a literal value)
    literals = [o for s, p, o in graph if isinstance(o, Literal)]
    if len(literals) == 0:
        print("❌ No literal values found in the RDF graph.")
        return False

    # 5. Basic sanity checks on Python structure
    try:
        source_lines = inspect.getsource(graph.__class__)
    except Exception:
        pass  # Safe fallback, ignore if restricted env

    print("✅ Validation passed successfully!")
    return True


if __name__ == "__main__":
    # Test basic behavior in local mode
    g = Graph()
    EX = Namespace("http://example.org/")
    g.bind("ex", EX)
    g.add((EX.John, RDF.type, FOAF.Person))
    g.add((EX.John, FOAF.name, Literal("John Doe", datatype=XSD.string)))
    validate_task(g)
