# Properties
## Details
* Category: [Standards](../../categories/Standards.md), [RDFS](../../modules/RDFS.md), [OWL](../../modules/OWL.md)
* Module Prerequisites: None 
* Audience: [Any](../../audiences/Any.md)
* Level: [Beginner](../../levels/Beginner.md)

## Content
### What are *properties* in triples or knowledge graphs? 

Triples are defined in the Resource Definition Framework (RDF) developed by the World Wide Web Consortium (W3C) and introduced in the Open Curriculum’s [RDF Module](../RDF/RDF.md). Triples, the fundamental data structure of RDF, are made up of a subject, predicate, and object. [1] 

    subject    predicate    object

The *predicate* expresses how the subject is *related* to the object. Here are some sample definitions of knowledge graphs. Notice how relationships (italics ours) are integral to these definitions. 

>"[Google] has been working on an intelligent model—in geek-speak, a “graph”—that understands real-world entities and their *relationships* to one another: things, not strings." [2]

>“Knowledge graphs are large networks of entities, their semantic types, *properties*, and *relationships* between entities” [3]. 

>“A knowledge graph (i) mainly describes real-world entities and their *interrelations*, organized in a graph, (ii) defines possible classes and *relations* of entities in a schema, (iii) allows for potentially *interrelating* arbitrary entities with each other, and (iv) covers various topical domains.” [4]

In RDF triples, the predicate states the nature of the relationship between the subject and the object in a directional way, i.e., from subject to object. The RDF term for predicate is *property*. Predicate and property refer to the same concept and are often used interchangeably. [5, 6] 

### What other terms are used for properties?  ###



| Methodology | Subject | Predicate | Object|
| --- | --- | --- | --- |
| RDF | Resource  | Property | Value|
| Knowledge Graph Embedding (Fact) | head (h) | relation (r) | tail (t) |
| Solid Geometry | vertex | edge | vertex|
| Graphs | nodes  | arcs  | nodes|
| Entity-Relationship (ER) Model | entity type (category) or entity (instance) | attribute or relationships | value|
| Mind maps. Concept maps.  | Box, circle, diamond, etc.  | arrows | box, circle, diamond, etc. |
| Topic map (for indexes) | topics| associations | occurrences |
| RDFS and OWL | domain | object or data properties | range|
| Description Logics | concept or instance | roles (object properties) or attributes (data properties) |  

In solid geometry, a vertex is the meeting point of two or more edges of a solid shape. an edge connects two vertices, defining how the two vertices are related spatially. An edge, like a predicate, connects two elements.  

![Edge, vertex, node, and arc.](images/Edge vertex node arc.jpg)


## Related KGC Media
* KGC Book Club: Michael Uschold, *Demystifying OWL for the Enterprise*, Spring 2021
* KGC Book Club: Dean Allemang, *Semantic Web for the Working Ontologist*, Fall 2020



## References

[1] Allemang, Dean and James Hendler. *Semantic Web for the Working Ontologist.* p. 67

[2] Amit Singhal, Introducing the Knowledge Graph: things, not strings, (May 16, 2012) https://blog.google/products/search/introducing-knowledge-graph-things-not/

[3] Krötzsch, Markus and Gerhard Weikum. “Web Semantics: Science, Services and Agents on the World Wide Web.” Journal of Web Semantics 37–38 (March 2016): 53–54. https://doi.org/10.1016/j.websem.2016.04.002.)

[4] Paulheim, Heiko. “Knowledge Graph Refinement: A Survey of Approaches and Evaluation Methods.” Semantic Web 8, no. 3 (2017): 489–508. (https://doi.org/10.3233/SW-160218)>

[5] WC3, RDF 1.1 Primer, [3.1 Triples](https://www.w3.org/TR/rdf11-primer/#:~:text=The%20subject%20and%20the%20object,elements%20they%20are%20called%20triples)

[6] Uschold, Michael. *Demystifying OWL for the Enterprise.* Morgan & Claypool, 2018. Section 2.4.3, p 45




## Contributors
* Steve Gillespie
