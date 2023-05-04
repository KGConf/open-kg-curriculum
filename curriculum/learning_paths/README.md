# Learning Paths within the Open Curriculum

##  The People Side of Knowledge Graphs
### Steep Learning Curve and Scarce Training
* Existing tools are not user-friendly: Why is the subject so 🤬 complicated?
* Why hasn’t anyone produced an educational starting point that isn’t mired in academic or technical jargon?
* Why is there no single, at least *semi*-canonical source of education about the subject?
* How can I learn this subject, really learn it, by building understanding and memory through repetition?
* What is the most basic starting point for learning KG?
- [Add who, what, how designations for the learning paths]

### Different Learning Levels
* What are the necessary prerequisites to learning about KG, and at what levels?
  * Computer science?
  * Math?
  * Logic?

### Knowledge Graph
* What is a “knowledge graph”?
  * Can you give me a straightforward high-level concept that doesn’t trip over itself?
  * How is a knowledge graph different from “linked data” or “the semantic web”?

## The Business Side of Knowledge Graphs
### Use Cases in Industry
* What is a KG used for?
* Why should I choose a KG over some other kind of technology?
* If they’re so great, why haven’t they taken over the world?

### Use Cases in Information Technology and Data Science
* How do knowledge graphs play with current and emerging IT?
* Why do people insist on muddying the subject with new variations, extensions to the basics (SHACL, entity extraction, machine learning)?

## The Process Side of Knowledge Graphs
### Design and Implementation Methods
* Tell me how to design, build, and query a knowledge graph in a freshman learning session using readily available technology. Go.
* Tell me how to reach the next level (whatever that is) of education in a sophomore learning session. Go.

### Design and Implementation Resources 
#### Schema.org
* What is Schema.org?
* How do I navigate Schema.org’s user interface?
* How do I embed properties and classes from Schema.org into my own ontology?

## The Stack: Architectural Layers for Knowledge Graphs
* What is the minimum "stack" (software and standards) that I could use to design, add data to, and query a linked data model?

### Trust
* If "anyone can say anything about anything" (i.e., the semantic web AAA slogan), how can I trust the results of combined data sources?

### Proof
* Give me an example of inference in action? 
* Is inference primarily used by ontology tools to check logic or can it be invoked using triple stores?

### Logic
* Many of the OWL-related references in particular seem to refer to logic. How much logic do I really need to know to design and use ontologies?

### Ontologies
* What is OWL (the Web Ontology Language)?
  * Predicate Logic, Description Logic, OWL
  * RDFS, Entailment Regimes, OWL
* What problems or challenges does OWL solve?
  * What is a Knowledge Graph?, What is an Ontology?
* What is the absolute minimum that I need to know about OWL?
  * Entailment Regimes, Closed World vs. Open World Assumptions
* What is the next-to-absolute minimum that I need to know about OWL?
  * `See` "What is OWL (the Web Ontology Language)?"
* Is there a single "right" combination of properties, classes, and resources to describe what you're modeling, or can there be many different ways of describing a collection?
  * Survey of Ontology Engineering Methodologies

#### Classes
* What is the difference between an RDFS class and an OWL class?
  * RDFS, OWL
  * What is a class?
* At what point in an ontology design does a class turn into a resource? That is, how do you know that you're referring not to a group of things but to a specific thing?
  * Survey of Ontology Engineering Methodologies

### Taxonomy
Learning Objective: "I am a beginner, and I want to know what a taxonomy is." 
Learning Path:
* What is a Metadata?
* Taxonomy vs Ontology
* SKOS

Learning Objective: "I am beginnering, and I want make a taxonomy." 
Learning Path:
* Taxonomy vs Ontology
* Turtle
* Protege
* RDF
* RDFS

### Querying

#### SPARQL
* What is SPARQL?
* What are the basics of using SPARQL to query a graph database?
* How is SPARQL similar to and different from SQL (the Structured Query Language)?
* How do I filter on partial strings when I'm writing a SPARQL query?
* How do I find SPARQL endpoints and connect to them in my queries? 

#### Cypher
* What is Cypher?
* What are the basics of using Cypher to query a graph database?
* When do I use Cypher and when do I use SPARQL?
* How is Cypher similar to and different from SQL (the Structured Query Language)?

### Knowledge Graphs
#### Resource Description Format (RDF)   
* What is a "graph" within the context of an RDF file? 
* Why would I need a knowledge graph and how would I create in RDF?
* Is it better to download the RDF files and import them into my own triple store?
* Do I need to add entity or language tags like “@en” to my values in RDF?
* Why should I create my data in RDF? Isn't it just easier to import worksheet data into a knowledge graph application?
* What does it take to redirect browsers to different formats of my data?

#### RDF Schema (RDFS)
* What does RDFS (RDF Schema) add to RDF (the Resource Description Format)? 
* Why would I use it in my ontology?

#### Property Graphs
* What is the difference between an RDF triple store and a property graph? 
* Why would someone choose to use one over the other?

#### Reification
* What is reification?
* Why is reification important?
* How would I implement reification in different graph systems?### Syntax. Serialization

### Syntax and Serialization
* What is the difference between the various serialization formats? What are the strengths and weaknesses of each? Which is the best for beginners?

### Identifiers
* How can the same values or URIs be used both subjects and objects in triples? Aren't they either one thing or the other?
* What is "dereferencing"? Can you show us an example of it in the wild?
* What is the difference between a URL, URI, and URN?
* What is this hash vs. slash business?
* How do I point to an RDF file in a URI without using an extension like “.rdf”?
