# What is a Knowledge Graph?
## Details
* Category: [Foundational](../../categories/Foundational.md)
* Module Prerequisites: [What is Metadata?](../What_is_Metadata/What_is_Metadata.md), [What is an Ontology?](../What_is_an_Ontology/What_is_an_Ontology.md)
* Audience: [Any](../../audiences/Any.md)
* Level: [Beginner](../../levels/Beginner.md)

## Content

### Definition
A knowledge graph is a type of graphical representation of the connections between real-world objects or abstract concepts. These connections form a conceptualization of the world in a particular domain. 

The basic unit of the information contained in a knowledge graph is a fact. The “facts” are stored as triplets, which are made up of 2 nodes and an edge that connects them. There is more than one way to describe the 3 elements of a triplet [1]:
- Real-world objects: <head, relation, tail>
- Linguistic: <subject, predicate, object>
- Technical components: <node, edge, node>
- Example: <Hans, is a, cat>; <Hans, is the pet of, Megan>

Another way to describe knowledge graphs is that they’re a way to implement knowledge models that allows for a database structure that’s more compatible with the conceptualization of data as a semantic web. The tail node of one triple is connected to other nodes, which forms a network of related “things". Both humans and computers are able to reasonably understand the web of data because it’s based on formal semantics and logic [2]. 

There’s added complexity once you get into the semantics underlying the nodes and relations. They can be represented similarly to object-oriented design with classes. Hierarchical classification of nodes can represent sub-classes and their common superclass, such as a family tree. The edges that connect the nodes have types. Relationship types get at the meaning behind the connection by describing what the entities, are, do, are a part of, etc. There is underlying logic that allows for inferences to be made with the data by defining inverse and transitive relationship types. A third way of modeling semantic data is into categories. Categories describe an aspect of what an entity is [2].

### Ontology
The terms ontology and knowledge graph are often confused because there’s a lot of overlap in meaning. Google popularized the term knowledge graph in 2012, though they were building off of existing research such as knowledge representation, knowledge acquisition, natural language processing, ontology engineering, and the semantic web [3]. Ontologies represent the schema that uses formal semantics. When implemented correctly, the schema should map to a knowledge graph so that the meaning is properly represented. This ensures that there is a shared understanding between the creators of the graph and the users or software that will need to be able to effectively query the data [2]. There’s debate surrounding whether or not knowledge graphs and ontologies are essentially the same thing [5].

### Knowledge Graph vs Other Information Databases
A Knowledge Graph, or simply referred to as KG, is an alternative form for representing relationships between informational data.  Unlike relational databases, a knowledge graph can provide insight to the deep understanding of the data within the scope of the defined ontology, or rules listed out to define the connections between data and relationships.  A knowledge graph provides detailed information for data integration, unification, linking, and reuse [2].  A knowledge graph differentiates itself from a normal graph by [1]:  
- Supporting heterogeneous data:  knowledge graphs are not restricted by the typing of objects and relationships
- Modeling Real-World information:  knowledge graphs are modeled similar to how a human may comprehend a set of information
- Performing Logical Reasoning:  traversal of vertices between nodes results in  connections from the starting node to the end node and all relationships in between  

Although the focus of a knowledge graph is on relationship within data, the benefits of a knowledge graph include [1]:
- Structured Representation of Data compared to text-based display of information
- Removing Redundancy:  tabular databases require the use of empty columns and rows to represent new facts about the data
- Querying for Complex Information:  tabular databases may incorporate multiple statements to join varying tables together to extract a piece of information whereas a knowledge graph can simplify and improve the efficiency of querying.  

When compared against a traditional tabular database, a knowledge graph provides both  flexibility with data entry, and efficiency in data storage and the computational requirements for queries.

### Implementation of a Knowledge Graph
The process in implementing a knowledge graph begins with a collection of data and representative relationships between the different pieces of data.  Defining how the data should be used is critical with formulating the relationships connecting data points.  Ontology frameworks, such as Resource Description Framework (RDF) and Web Ontology Language (OWL), assist in connecting relationships between data.  Both RDF and OWL are standardized frameworks used to represent ontologies on the web, allowing information to be expressed and exchanged across a variety of applications without losing meaning [1].  A formal ontology of the dataset not only provides how the data and relationships can be utilized together to formulate queries to provide explicit and implicit understanding of the information, but also limits the implementation to a specific topic which provides the scope of the knowledge graph’s usage.  

General outline for creating a knowledge graph: 
* Determine use cases - Define the scope of the knowledge graph.  What topic area should it address?  Where and how will it be used?  Form competency questions that show off it’s capabilities
* Outline and organize necessary data - Determine what data is needed and what is not.  How much detail is needed? Which details can be overlooked?
* Create ontologies from relationships - Utilize resources such as RDF and OWL to create an ontology to represent the formal semantics and schema for the dataset.  
* Create knowledge graph and verify competency questions - Utilize the RDF triple stores created to create a visualization of the dataset, as well as verifying competency questions through SPARQL queries of the data.  


### Applications and Examples
Knowledge graphs can be used to organize data from multiple sources or organizations, capture information about entities of interest in a specific domain or task (like people, places or events), and create connections and relationships between them. Fields of research that benefit from the usage of knowledge graphs include data science and natural language processing with the tools from Artificial Intelligence and Machine Learning.  Example applications of knowledge graphs include [3]:
* Facilitating access to and integration of data sources
* Adding context, depth to other metadata to entities
* Allowing for humans and systems to use similar logic and reasoning

Specific examples and applications of knowledge graphs include:

Google’s Knowledge Graph:  The Knowledge Graph deployed by Google provides a resource to create a summarized box of relevant information within search results. With a large pool of data sources to logically reason with, users are able to efficiently find relevant information in these panels known as Knowledge Panels.

Retail Industry: Used for up-sell and cross-sell strategies, recommending products based on individual purchase behavior and tracking popular purchasing trends [5].

Entertainment Industry: Used alongside artificial intelligence for recommendation engines on media and social networking platforms.  Also used for leveraging online engagement behaviors to recommend new content for users to read, watch, or follow [5].

Finance Industry: Used for know-your-customer and anti-money laundering initiatives. They assist in financial crime prevention and investigation, allowing banking institutions to understand the flow of money across their clientele and identify noncompliant customers [5].

Healthcare Industry: Can be used for organizing and categorizing relationships within medical research client treatment. Information can be used to assist providers by validating diagnoses and identifying treatment plans based on individual needs [5]. 


### In Summary
Knowledge Graphs serve the purpose of representing a database with the functionality to query the information,  allowing users to understand deeper meaning found through undefined relationships.  While tabular databases can still serve a purpose for data storage, knowledge graphs provide an efficient method for querying.  

## Related KGC Media
* Workshop Example
* Tutorial Example

## External Media Reference
* [SPOKE: Scalable Precision Medicine Open Knowledge Engine.](https://spoke.ucsf.edu/)
* [Inventory Management using KG](https://www.youtube.com/watch?v=WKC0i47szjU)
* [Franz Inc's AllegroGraph](https://allegrograph.com/about-franz/)
* [Introducing the Knowledge Graph](https://blog.google/products/search/introducing-knowledge-graph-things-not/)
* [A Reintroduction to our Knowledge Graph and Knowledge Panels](https://blog.google/products/search/about-knowledge-graph-and-knowledge-panels/)
* [Knowledge Graph entry for Knowledge Graph](https://kgkg.factnexus.com/@3782~6.html)


## References
[1] Mayank, M. (2021, August 30). A guide to the knowledge graphs. Medium. Retrieved
February 1, 2023, <br> from https://towardsdatascience.com/a-guide-to-the-knowledge-graphs-bfb5c40272f1 <br>

[2] Ontotext. (n.d.). What is a Knowledge Graph? Ontotext. Retrieved February 1, 2023, <br> from
https://www.ontotext.com/knowledgehub/fundamentals/what-is-a-knowledge-graph/ <br>

[3] Pan, J., Simperl, E., Jiménez-Ruiz, E., & Horrocks, I. (n.d.). Knowledge graphs. The Alan
Turing Institute. Retrieved February 1, 2023, <br> from
https://www.turing.ac.uk/research/interest-groups/knowledge-graphs <br>

[4] McCusker, J., McGuinness, D., Erickson, J., Chastain, K. (n.d.). What is a Knowledge Graph? Authorea. Retrieved February 8, 2023, <br> from https://www.authorea.com/users/6341/articles/107281-what-is-a-knowledge-graph/_show_article <br>

[5] IBM. (n.d.). What is knowledge graph? IBM. Retrieved February 8, 2023, <br> from https://www.ibm.com/topics/knowledge-graph <br>

## Contributors
* Brandon Dave
* Megan Noble
* Ryan Miller
