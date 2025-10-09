# Hands-on Assignment 2 – Self Assessment  
**Group 08**

---

## ✅ Checklist

### The “analysis.html” file
- [x] Includes the potential license of the dataset to be generated (CC BY 4.0).  
- [x] Includes the resource naming strategy with clear URI patterns.

### The resource naming strategy
- [x] Uses a custom domain (`http://group08.linkeddata.es/`) different from the default Protégé domain.  
- [x] Uses different paths for ontology resources (`/ontology/`) and individuals (`/resource/`).  
- [x] Ensures that the paths for individuals of different classes are distinct (e.g., `/station/`, `/trafficSection/`, `/bikeParking/`).  
- [x] Defines individual URIs independently of class URIs.

### The ontology file
- [x] Uses the `.ttl` extension.  
- [x] Is serialized in Turtle format.  
- [x] Follows the resource naming strategy defined in `analysis.html`.  
- [x] Contains several classes (`Station`, `TrafficSection`, `BikeParking`, `Observation`, `WeatherCondition`).  
- [x] Contains at least one object property (`:measuredAt`, `:hasWeather`).  
- [x] Contains at least one datatype property (`:hasValue`, `:capacity`, `:timestamp`).  
- [x] Defines the domain of all properties.  
- [x] Defines the range of all properties.  
- [x] Defines all class names starting with a capital letter.  
- [x] Defines all property names starting with a lowercase letter.  
- [x] Uses consistent labels in English only.  
- [x] Does not define multiple domains or multiple ranges for any property.  
- [x] Contains at least one class (`Station`, `TrafficSection`) that can be linked to other entities (e.g., DBpedia, Wikidata).

---

## 💬 Comments on the self-assessment
All deliverables for Hands-on 2 were completed successfully.  
The analysis includes licensing and URI design. The ontology is simple but correctly structured and follows Linked Data best practices.  
We created sample RDF data consistent with the ontology and validated it syntactically.  
Future improvements could include extending the ontology with external vocabularies (e.g., Geo, QUDT) and linking the data to external resources.
