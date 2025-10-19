# --- REQUIRED HEADER FOR AUTO-GRADER (do not remove) ---
# Francisco Sánchez González (ID: 220091) - fransanchez6
# Assignment 4 - Task 07
# IMPORTANT: No 'pip install' lines allowed.

from rdflib import Graph, Namespace, Literal, RDF, RDFS, XSD
from rdflib.namespace import FOAF, DCTERMS
try:
    from validation import validate_task
except:
    def validate_task(*args, **kwargs): print("validation.py not found (local mode).")

# --- TASK IMPLEMENTATION ---

# Create RDF graph
g = Graph()
EX = Namespace("http://example.org/")
g.bind("ex", EX)

# Define a couple of people
g.add((EX.John, RDF.type, FOAF.Person))
g.add((EX.Mary, RDF.type, FOAF.Person))
g.add((EX.John, FOAF.name, Literal("John Doe")))
g.add((EX.Mary, FOAF.name, Literal("Mary Smith")))
g.add((EX.John, FOAF.knows, EX.Mary))

# Serialize (optional)
#g.serialize(destination="task07_output.ttl", format="turtle")

# Validate (for the automatic checker)
if __name__ == "__main__":
    validate_task(g)
