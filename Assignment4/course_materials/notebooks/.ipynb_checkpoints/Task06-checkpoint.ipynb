{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "nOOPLCHF7hLB"
   },
   "source": [
    "**Task 06: Modifying RDF(s)**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-10-11T11:35:37.925737Z",
     "start_time": "2025-10-11T11:35:35.708844Z"
    },
    "id": "Yl9npCt8n6m-"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: rdflib in /opt/anaconda3/lib/python3.11/site-packages (7.2.1)\r\n",
      "Requirement already satisfied: pyparsing<4,>=2.1.0 in /opt/anaconda3/lib/python3.11/site-packages (from rdflib) (3.0.9)\r\n"
     ]
    }
   ],
   "source": [
    "!pip install rdflib\n",
    "import urllib.request\n",
    "url = 'https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/refs/heads/master/Assignment4/course_materials/python/validation.py'\n",
    "urllib.request.urlretrieve(url, 'validation.py')\n",
    "github_storage = \"https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "XY7aPc86Bqoo"
   },
   "source": [
    "Import RDFLib main methods"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-10-11T11:35:42.615003Z",
     "start_time": "2025-10-11T11:35:42.263156Z"
    },
    "id": "9ERh415on7kF"
   },
   "outputs": [],
   "source": [
    "from rdflib import Graph, Namespace, Literal, XSD\n",
    "from rdflib.namespace import RDF, RDFS\n",
    "from validation import Report\n",
    "g = Graph()\n",
    "g.namespace_manager.bind('ns', Namespace(\"http://somewhere#\"), override=False)\n",
    "r = Report()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "gM3DASkTQQ5Y"
   },
   "source": [
    "Create a new class named Researcher"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-10-11T11:35:48.640592Z",
     "start_time": "2025-10-11T11:35:48.636022Z"
    },
    "id": "6vtudax8Xb7b"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://mydomain.org#Researcher http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n"
     ]
    }
   ],
   "source": [
    "ns = Namespace(\"http://mydomain.org#\")\n",
    "g.add((ns.Researcher, RDF.type, RDFS.Class))\n",
    "for s, p, o in g:\n",
    "  print(s,p,o)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ZX8w9jnV5Xhp"
   },
   "source": [
    "**Task 6.0: Create new prefixes for \"ontology\" and \"person\" as shown in slide 14 of the Slidedeck 01a.RDF(s)-SPARQL shown in class.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-10-11T11:47:17.838532Z",
     "start_time": "2025-10-11T11:47:17.829233Z"
    },
    "id": "b1ZQgYgB5vi7"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "@prefix ontology: <http://oeg.fi.upm.es/def/people#> .\n",
      "@prefix organization: <http://oeg.fi.upm.es/resource/organization/> .\n",
      "@prefix person: <http://oeg.fi.upm.es/resource/person/> .\n",
      "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n",
      "\n",
      "person:Raul ontology:hasBirthDate \"1975-12-26\"^^xsd:date ;\n",
      "    ontology:hasFullName \"Raúl García Castro\" ;\n",
      "    ontology:hasWebPage <http://oeg.fi.upm.es/> ;\n",
      "    ontology:isMemberOf organization:OEG .\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from rdflib import Graph, Namespace, Literal, URIRef\n",
    "from rdflib.namespace import RDF, RDFS, XSD\n",
    "\n",
    "g = Graph()\n",
    "\n",
    "\n",
    "person     = Namespace(\"http://oeg.fi.upm.es/resource/person/\")\n",
    "organization = Namespace(\"http://oeg.fi.upm.es/resource/organization/\")\n",
    "ontology   = Namespace(\"http://oeg.fi.upm.es/def/people#\")\n",
    "\n",
    "\n",
    "g.namespace_manager.bind(\"person\", person, override=False)\n",
    "g.namespace_manager.bind(\"organization\", organization, override=False)   # optional\n",
    "g.namespace_manager.bind(\"ontology\", ontology, override=False)\n",
    "g.namespace_manager.bind(\"rdf\", RDF); g.namespace_manager.bind(\"rdfs\", RDFS)\n",
    "g.namespace_manager.bind(\"xsd\", XSD)\n",
    "\n",
    "\n",
    "g.add((person.Raul, ontology.hasFullName, Literal(\"Raúl García Castro\")))\n",
    "g.add((person.Raul, ontology.hasBirthDate, Literal(\"1975-12-26\", datatype=XSD.date)))\n",
    "g.add((person.Raul, ontology.isMemberOf, organization.OEG))\n",
    "g.add((person.Raul, ontology.hasWebPage, URIRef(\"http://oeg.fi.upm.es/\")))\n",
    "\n",
    "ttl = g.serialize(format=\"turtle\")\n",
    "print(ttl.decode() if isinstance(ttl, (bytes, bytearray)) else ttl)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "qp1oe2Eddsvo"
   },
   "source": [
    "**TASK 6.1: Reproduce the taxonomy of classes shown in slide 34 in class (all the classes under \"Vocabulario\", Slidedeck: 01a.RDF(s)-SPARQL). Add labels for each of them as they are in the diagram (exactly) with no language tags. Remember adding the correct datatype (xsd:String) when appropriate**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-10-11T11:51:38.000079Z",
     "start_time": "2025-10-11T11:51:37.992430Z"
    },
    "id": "pnsrsgRUWF3A"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#AssociateProfessor\n",
      "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#label InterimAssociateProfessor\n",
      "http://oeg.fi.upm.es/resource/person/Raul http://oeg.fi.upm.es/def/people#hasBirthDate 1975-12-26\n",
      "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/resource/person/Raul http://oeg.fi.upm.es/def/people#hasWebPage http://oeg.fi.upm.es/\n",
      "http://oeg.fi.upm.es/resource/person/Raul http://oeg.fi.upm.es/def/people#isMemberOf http://oeg.fi.upm.es/resource/organization/OEG\n",
      "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
      "http://oeg.fi.upm.es/resource/person/Raul http://oeg.fi.upm.es/def/people#hasFullName Raúl García Castro\n",
      "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/2000/01/rdf-schema#label Person\n",
      "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
      "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#label FullProfessor\n",
      "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#label AssociateProfessor\n",
      "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#label Professor\n"
     ]
    }
   ],
   "source": [
    "from rdflib import Literal\n",
    "from rdflib.namespace import RDF, RDFS, XSD\n",
    "\n",
    "\n",
    "for cls, parent in [\n",
    "    (\"Person\", None),\n",
    "    (\"Professor\", \"Person\"),\n",
    "    (\"AssociateProfessor\", \"Professor\"),\n",
    "    (\"FullProfessor\", \"Professor\"),\n",
    "    (\"InterimAssociateProfessor\", \"AssociateProfessor\"),\n",
    "]:\n",
    "    c = ontology[cls]\n",
    "    g.add((c, RDF.type, RDFS.Class))\n",
    "    g.add((c, RDFS.label, Literal(cls, datatype=XSD.string)))\n",
    "    if parent:\n",
    "        g.add((c, RDFS.subClassOf, ontology[parent]))\n",
    "\n",
    "for s, p, o in g:\n",
    "    print(s, p, o)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-10-11T11:51:44.483497Z",
     "start_time": "2025-10-11T11:51:44.478101Z"
    },
    "id": "HdRPyusrjIuB"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The namespace is correct for http://oeg.fi.upm.es/def/people#Professor\n",
      "The namespace is correct for http://oeg.fi.upm.es/def/people#Person\n",
      "The namespace is correct for http://oeg.fi.upm.es/def/people#AssociateProfessor\n",
      "The namespace is correct for http://oeg.fi.upm.es/def/people#InterimAssociateProfessor\n",
      "The namespace is correct for http://oeg.fi.upm.es/def/people#FullProfessor\n",
      "Hierarchy OK\n",
      "TASK 6.1 OK\n"
     ]
    }
   ],
   "source": [
    "# Validation. Do not remove\n",
    "r.validate_task_06_01(g)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "MXBqtBkJd22I"
   },
   "source": [
    "**TASK 6.2: Add the 3 properties shown in slide 36. Add labels for each of them (exactly as they are in the slide, with no language tags), and their corresponding domains and ranges using RDFS. Remember adding the correct datatype (xsd:String) when appropriate. If a property has no range, make it a literal (string)**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-10-11T11:57:57.368615Z",
     "start_time": "2025-10-11T11:57:57.360710Z"
    },
    "id": "53hZNtXsXCNq"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#label hasHomePage\n",
      "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#label AssociateProfessor\n",
      "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#AssociateProfessor\n",
      "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
      "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#label InterimAssociateProfessor\n",
      "http://oeg.fi.upm.es/resource/person/Raul http://oeg.fi.upm.es/def/people#hasBirthDate 1975-12-26\n",
      "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#range http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#label hasName\n",
      "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/resource/person/Raul http://oeg.fi.upm.es/def/people#hasWebPage http://oeg.fi.upm.es/\n",
      "http://oeg.fi.upm.es/resource/person/Raul http://oeg.fi.upm.es/def/people#isMemberOf http://oeg.fi.upm.es/resource/organization/OEG\n",
      "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
      "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#label hasColleague\n",
      "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
      "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#FullProfessor\n",
      "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2000/01/rdf-schema#Literal\n",
      "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2000/01/rdf-schema#Literal\n",
      "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/2000/01/rdf-schema#label Person\n",
      "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
      "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
      "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#label FullProfessor\n",
      "http://oeg.fi.upm.es/resource/person/Raul http://oeg.fi.upm.es/def/people#hasFullName Raúl García Castro\n",
      "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#label Professor\n"
     ]
    }
   ],
   "source": [
    "from rdflib import Literal\n",
    "from rdflib.namespace import RDF, RDFS, XSD\n",
    "\n",
    "p = ontology.hasColleague\n",
    "\n",
    "g.remove((p, RDFS.domain, None))\n",
    "g.remove((p, RDFS.range,  None))\n",
    "g.remove((p, RDF.type,    None))\n",
    "g.remove((p, RDFS.label,  None))\n",
    "\n",
    "g.add((p, RDF.type, RDF.Property))\n",
    "g.add((p, RDFS.label,  Literal(\"hasColleague\", datatype=XSD.string)))\n",
    "g.add((p, RDFS.domain, ontology.Person))\n",
    "g.add((p, RDFS.range,  ontology.Person))\n",
    "\n",
    "for s, p, o in g:\n",
    "    print(s, p, o)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-10-11T11:57:59.697637Z",
     "start_time": "2025-10-11T11:57:59.693648Z"
    },
    "id": "pd2mE-vGaxbu"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TASK 6.2 OK\n"
     ]
    }
   ],
   "source": [
    "# Validation. Do not remove\n",
    "r.validate_task_06_02(g)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "OGct6k7Ld9O0"
   },
   "source": [
    "**TASK 6.3: Create the individuals shown in slide 36 under \"Datos\". Link them with the same relationships shown in the diagram.\"**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-10-11T12:01:34.654077Z",
     "start_time": "2025-10-11T12:01:34.640040Z"
    },
    "id": "jbMMSHSZcFcf"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
      "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/resource/person/Asun http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://oeg.fi.upm.es/def/people#FullProfessor\n",
      "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#range http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#label hasName\n",
      "http://oeg.fi.upm.es/resource/person/Oscar http://oeg.fi.upm.es/def/people#hasName Óscar Corcho García\n",
      "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#FullProfessor\n",
      "http://oeg.fi.upm.es/resource/person/Oscar http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/resource/person/Oscar http://oeg.fi.upm.es/def/people#hasColleague http://oeg.fi.upm.es/resource/person/Asun\n",
      "http://oeg.fi.upm.es/resource/person/Raul http://www.w3.org/2000/01/rdf-schema#label Raul\n",
      "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2000/01/rdf-schema#Literal\n",
      "http://oeg.fi.upm.es/resource/person/Asun http://oeg.fi.upm.es/def/people#hasHomePage http://oeg.fi.upm.es/\n",
      "http://oeg.fi.upm.es/resource/person/Raul http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://oeg.fi.upm.es/def/people#InterimAssociateProfessor\n",
      "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
      "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#AssociateProfessor\n",
      "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#label Professor\n",
      "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#label hasHomePage\n",
      "http://oeg.fi.upm.es/resource/person/Asun http://oeg.fi.upm.es/def/people#hasColleague http://oeg.fi.upm.es/resource/person/Raul\n",
      "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#label InterimAssociateProfessor\n",
      "http://oeg.fi.upm.es/resource/person/Oscar http://www.w3.org/2000/01/rdf-schema#label Oscar\n",
      "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
      "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#label hasColleague\n",
      "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
      "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2000/01/rdf-schema#Literal\n",
      "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/2000/01/rdf-schema#label Person\n",
      "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
      "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#label FullProfessor\n",
      "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#label AssociateProfessor\n",
      "http://oeg.fi.upm.es/resource/person/Asun http://www.w3.org/2000/01/rdf-schema#label Asun\n",
      "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n"
     ]
    }
   ],
   "source": [
    "from rdflib import Namespace, Literal\n",
    "from rdflib.namespace import RDF, RDFS, XSD\n",
    "\n",
    "\n",
    "person       = Namespace(\"http://oeg.fi.upm.es/resource/person/\")\n",
    "organization = Namespace(\"http://oeg.fi.upm.es/resource/organization/\")\n",
    "ontology     = Namespace(\"http://oeg.fi.upm.es/def/people#\")\n",
    "\n",
    "g.namespace_manager.bind(\"person\", person, override=True)\n",
    "g.namespace_manager.bind(\"organization\", organization, override=True)\n",
    "g.namespace_manager.bind(\"ontology\", ontology, override=True)\n",
    "\n",
    "\n",
    "for i in (person.Oscar, person.Asun, person.Raul):\n",
    "    g.remove((i, None, None))\n",
    "\n",
    "\n",
    "g.add((person.Oscar, RDF.type, ontology.Person))\n",
    "g.add((person.Oscar, RDFS.label, Literal(\"Oscar\", datatype=XSD.string)))\n",
    "\n",
    "g.add((person.Asun,  RDF.type, ontology.FullProfessor))\n",
    "g.add((person.Asun,  RDFS.label, Literal(\"Asun\", datatype=XSD.string)))\n",
    "\n",
    "g.add((person.Raul,  RDF.type, ontology.InterimAssociateProfessor))\n",
    "g.add((person.Raul,  RDFS.label, Literal(\"Raul\", datatype=XSD.string)))\n",
    "\n",
    "\n",
    "g.add((person.Oscar, ontology.hasName,\n",
    "       Literal(\"Óscar Corcho García\", datatype=XSD.string)))\n",
    "\n",
    "g.add((person.Asun, ontology.hasHomePage,\n",
    "       Literal(\"http://oeg.fi.upm.es/\", datatype=XSD.string)))\n",
    "\n",
    "g.add((person.Oscar, ontology.hasColleague, person.Asun))\n",
    "g.add((person.Asun,  ontology.hasColleague, person.Raul))\n",
    "\n",
    "# Visualize the results\n",
    "for s, p, o in g:\n",
    "  print(s,p,o)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-10-11T12:01:37.451493Z",
     "start_time": "2025-10-11T12:01:37.447854Z"
    },
    "id": "-3q4Wv2EfYew"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TASK 6.3 OK\n"
     ]
    }
   ],
   "source": [
    "r.validate_task_06_03(g)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "tD383J__eHfV"
   },
   "source": [
    "**TASK 6.4: Add to the individual person:Oscar the email address, given and family names. Use the properties already included in example 4 to describe Jane and John (https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials/rdf/example4.rdf). Do not import the namespaces, add them manually**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-10-11T12:04:53.170358Z",
     "start_time": "2025-10-11T12:04:53.161989Z"
    },
    "id": "hWmwlAfBcgN-"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
      "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/resource/person/Asun http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://oeg.fi.upm.es/def/people#FullProfessor\n",
      "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#range http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#label hasName\n",
      "http://oeg.fi.upm.es/resource/person/Oscar http://www.w3.org/2001/vcard-rdf/3.0/Family Corcho\n",
      "http://oeg.fi.upm.es/resource/person/Oscar http://oeg.fi.upm.es/def/people#hasName Óscar Corcho García\n",
      "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#FullProfessor\n",
      "http://oeg.fi.upm.es/resource/person/Oscar http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/resource/person/Oscar http://oeg.fi.upm.es/def/people#hasColleague http://oeg.fi.upm.es/resource/person/Asun\n",
      "http://oeg.fi.upm.es/resource/person/Oscar http://www.w3.org/2001/vcard-rdf/3.0/Given Oscar\n",
      "http://oeg.fi.upm.es/resource/person/Raul http://www.w3.org/2000/01/rdf-schema#label Raul\n",
      "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2000/01/rdf-schema#Literal\n",
      "http://oeg.fi.upm.es/resource/person/Asun http://oeg.fi.upm.es/def/people#hasHomePage http://oeg.fi.upm.es/\n",
      "http://oeg.fi.upm.es/resource/person/Raul http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://oeg.fi.upm.es/def/people#InterimAssociateProfessor\n",
      "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
      "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#AssociateProfessor\n",
      "http://oeg.fi.upm.es/resource/person/Oscar http://xmlns.com/foaf/0.1/email oscar@example.com\n",
      "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#label Professor\n",
      "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#label hasHomePage\n",
      "http://oeg.fi.upm.es/resource/person/Asun http://oeg.fi.upm.es/def/people#hasColleague http://oeg.fi.upm.es/resource/person/Raul\n",
      "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#label InterimAssociateProfessor\n",
      "http://oeg.fi.upm.es/resource/person/Oscar http://www.w3.org/2000/01/rdf-schema#label Oscar\n",
      "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
      "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#label hasColleague\n",
      "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
      "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2000/01/rdf-schema#Literal\n",
      "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
      "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/2000/01/rdf-schema#label Person\n",
      "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#Person\n",
      "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
      "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#label FullProfessor\n",
      "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#label AssociateProfessor\n",
      "http://oeg.fi.upm.es/resource/person/Asun http://www.w3.org/2000/01/rdf-schema#label Asun\n",
      "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n"
     ]
    }
   ],
   "source": [
    "from rdflib import Namespace, Literal\n",
    "from rdflib.namespace import XSD\n",
    "\n",
    "# Namespaces manuell anlegen (wie in example4.rdf)\n",
    "foaf  = Namespace(\"http://xmlns.com/foaf/0.1/\")\n",
    "vcard = Namespace(\"http://www.w3.org/2001/vcard-rdf/3.0/\")\n",
    "\n",
    "# (optional für schöne Turtle-Ausgabe)\n",
    "g.namespace_manager.bind(\"foaf\", foaf, override=False)\n",
    "g.namespace_manager.bind(\"vcard-rdf\", vcard, override=False)\n",
    "\n",
    "# Werte für Oscar setzen (Strings ohne Sprach-Tag)\n",
    "g.add((person.Oscar, foaf.email,     Literal(\"oscar@example.com\", datatype=XSD.string)))\n",
    "g.add((person.Oscar, vcard.Given,    Literal(\"Oscar\",             datatype=XSD.string)))\n",
    "g.add((person.Oscar, vcard.Family,   Literal(\"Corcho\",            datatype=XSD.string)))\n",
    "# Visualize the results\n",
    "for s, p, o in g:\n",
    "  print(s,p,o)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-10-11T12:04:56.283486Z",
     "start_time": "2025-10-11T12:04:56.278969Z"
    },
    "id": "Y1NiIQMyfgyF"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TASK 6.4 OK\n"
     ]
    }
   ],
   "source": [
    "# Validation. Do not remove\n",
    "r.validate_task_06_04(g)\n",
    "r.save_report(\"_Task_06\")"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
