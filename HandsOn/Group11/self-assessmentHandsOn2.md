# Hands-on assignment 2 – Self assessment

## Checklist

**The "analysis.html" file:**

- [x] Includes the potential license of the dataset to be generated
- [x] Includes the resource naming strategy

**The resource naming strategy:**

- [x] Uses a domain that is not the one given by default in Protégé
- [x] Uses different paths for ontology resources (i.e., classes and properties) and individuals
- [x] Ensures that the paths for individuals of different classes are not the same
- [x] Defines individual URIs independently of class URIs

**The ontology file:**

- [x] Uses the .ttl extension
- [x] Is serialized in the Turtle format
- [x] Follows the resource naming strategy
- [x] Contains at least one class
- [x] Contains at least one object property (where the value of the property is a resource)
- [x] Contains at least one datatype property (where the value of the property is a string literal, usually typed)
- [x] Defines the domain of all the properties (the origin of the property)
- [ ] Defines the range of all the properties (the destination of the property)
- [ ] Defines all class names starting with a capital letter
- [x] Defines all property names starting with a non-capital letter
- [x] Does not mix labels in different languages (e.g., Spanish and English)
- [ ] Does not define multiple domains or multiple ranges in properties
- [ ] Contains at least one class that will be used to link to other entities

## Comments on the self-assessment

### Completed elements:

1. **analysis.html file**: The file (analysis-1.html) correctly includes:
   - License information: CC BY 4.0 for the generated dataset
   - Resource naming strategy with custom domain: `http://eventFinder.org/madrid-data/`
   - Clear separation between ontology namespace (#) and data namespace (/)

2. **Resource naming strategy**: Well-defined with:
   - Custom domain not from Protégé default
   - Ontology namespace: `http://eventFinder.org/madrid-data/ontology#`
   - Data namespace: `http://eventFinder.org/madrid-data/resource/`
   - Different URI patterns for different resource types (event, date, etc.)

3. **Data files**: The TTL files contain data instances with:
   - Proper Turtle format
   - Consistent use of lowercase property names
   - Typed literals (e.g., xsd:date)
   - Spanish labels maintained consistently

### Missing or incomplete elements:

1. **On the Ontology definition file**:
   - Class definitions (e.g., Event, Location, etc.)
   - Property definitions with explicit domains and ranges
   - Object properties linking resources
   - At least one class for linking to external entities

2. **Property domains and ranges**: The current data files use properties but don't explicitly define their domains and ranges in an ontology file.

### Recommendations:

- Classes like `mdo:Event`, `mdo:Location`, `mdo:EventType`
- Object properties like `mdo:hasLocation` with proper domain and range
- Datatype properties with explicit domains and ranges
