# What is a Knowledge Graph?
## Details
* Category: [Foundational](../../categories/Foundational.md)
* Module Prerequisites: [What is Metadata?](../What_is_Metadata/What_is_Metadata.md), [What is an Ontology?](../What_is_an_Ontology/What_is_an_Ontology.md)
* Audience: [Any](../../audiences/Any.md)
* Level: [Beginner](../../levels/Beginner.md)

## Content

### Definition

### Knowledge Graph vs Other Information Databases
A Knowledge Graph is an alternative form for representing relationships between informational data.  Unlike relational databases, a knowledge graph can provide insight to the deep understanding of the data within the scope of the defined ontology, or rules listed out to define the connections between data and relationships.  A knowledge graph provides detailed information for data integration, unification, linking, and reuse [2].  A knowledge graph differentiates itself from a normal graph by [1]:  
- Supporting heterogeneous data:  knowledge graphs are not restricted by the typing of objects and relationships
- Modeling Real-World information:  knowledge graphs are modeled similar to how a human may comprehend a set of information
- Performing Logical Reasoning:  traversal of vertices between nodes results in  connections from the starting node to the end node and all relationships in between  

Although the focus of a knowledge graph is on relationship within data, the benefits of a knowledge graph include [1]:
- Structured Representation of Data compared to text-based display of information
- Removing Redundancy:  tabular databases require the use of empty columns and rows to represent new facts about the data
- Querying for Complex Information:  tabular databases may incorporate multiple statements to join varying tables together to extract a piece of information whereas a knowledge graph can simplify and improve the efficiency of querying.  

When compared against a traditional tabular database, a knowledge graph provides both  flexibility with data entry, and efficiency in data storage and the computational requirements for queries.

### Implementation of a Knowledge Graph
The process in implementing a knowledge graph begins with a collection of data and representative relationships between the different pieces of data.  Defining how the data should be used is critical with formulating the relationships connecting data points.  Defining this data can be done through the use of ontology frameworks such as Resource Description Framework (RDF) and Web Ontology Language (OWL).  Both RDF and OWL are standardized frameworks used to represent ontologies on the web, allowing information to be expressed and exchanged across a variety of applications without losing meaning [1].  A formal ontology of the dataset not only provides how the data and relationships can be utilized together to formulate queries to provide explicit and implicit understanding of the information, but also limits the implementation to a specific topic which provides the scope of the knowledge graph’s usage.  

General outline for creating a knowledge graph: 
* Determine use cases - Define the scope of the knowledge graph.  What topic area should it address?  Where and how will it be used?  Form competency questions that show off it’s capabilities
* Outline and organize necessary data - Determine what data is needed and what is not.  How much detail is needed? Which details can be overlooked?
* Create ontologies from relationships - Utilize resources such as RDF and OWL to create an ontology to represent the formal semantics and schema for the dataset.  
* Create knowledge graph and verify competency questions - Utilize the RDF triple stores created to create a visualization of the dataset, as well as verifying competency questions through SPARQL queries of the data.  


### Applications and Examples
Knowledge graphs can be used to organize data from multiple sources or organizations, capture information about entities of interest in a specific domain or task (like people, places or events), and create connections and relationships between them. A few popular area's where knowledge graphs can be especially useful are: data science, natural language processing and AI/ML.  Some uses of knowledge graphs include [3]:
* Facilitating access to and integration of data sources
* Adding context, depth to other metadata to entities
* Allowing for humans and systems to use similar logic and reasoning

Specific examples and applications of knowledge graphs include:

Google’s Knowledge Graph:  The google knowledge graph provides a resource to create a summarized box of relevant information within search results. With a large pool of data sources to logically reason with, users are able to efficiently find relevant information in these panels known as Knowledge Panels.

Retail Industry: Used for up-sell and cross-sell strategies, recommending products based on individual purchase behavior and tracking popular purchasing trends [5].

Entertainment Industry: Used alongside artificial intelligence for recommendation engines on media and social networking platforms.  Also used for leveraging online engagement behaviors to recommend new content for users to read, watch, or follow [5].

Fiance Industry: Have been used for know-your-customer and anti-money laundering initiatives. They assist in financial crime prevention and investigation, allowing banking institutions to understand the flow of money across their clientele and identify noncompliant customers [5].

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
