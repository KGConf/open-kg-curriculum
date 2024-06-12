# Protege
## Details
* Category: [Technology](../categories/Technology.md)
* Module Prerequisites: [Manchester Syntax](../modules/Manchester_Syntax.md)
* Audience: [Student, Developer](../audiences/Student,_Developer.md)
* Level: [Intermediate](../levels/Intermediate.md)

## Content
* For building and managing ontologies, many people utilize the open-source software program known as Protégé. A organized representation of concepts, things, and their connections in a particular area is called an ontology. In order to construct, update, and visualize ontologies, Protégé offers a user-friendly interface. As a result, it is a preferred option among researchers, programmers, and organizations working on knowledge representation, semantic web applications, and artificial intelligence systems.
* Protégé is used to build the relevant [OWL](../modules/OWL.md) (Web Ontology Language) file after defining the [schema](../modules/Schema.org.md) for a particular Knowledge Graph, which captures the structure, entities, and relationships specified in the schema. Users can build complex associations between attributes and patterns , laying the groundwork for the semantic connections in the graph. Classes can be created, providing properties, and forming class hierarchies using the software's simple interface, which allows them to construct a cogent ontology. The OWL file that represents this ontology acts as the framework for the Knowledge Graph, ensuring that data instances follow the defined schema and promoting meaningful interlinking and data retrieval within the graph.
* Example on how entities can look in an owl file produced by Protege :
```
# Prefix declarations
@prefix : <http://example.org/> .
@prefix authors: <http://example.org/authors/> .

# Class definitions
:Author rdf:type owl:Class .
:Book rdf:type owl:Class .

# Object property definition
:authorOf rdf:type owl:ObjectProperty .

# Individual definitions and axioms
authors:Antrea rdf:type :Author .
:Book1 rdf:type :Book .
authors:Antrea :authorOf :Book1 .
```
## Related KGC Media
* Workshop Example
* Tutorial Example

## References
[1] https://www.w3.org/2001/sw/wiki/Protege


## Contributors
* Cogan Shimizu
* Antrea Christou