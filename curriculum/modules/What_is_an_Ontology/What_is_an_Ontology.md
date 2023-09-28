# What is an Ontology
## Details
* Category: [](../categories/.md)
* Module Prerequisites: [](../modules/.md)
* Audience: [](../audiences/.md)
* Level: [](../levels/.md)

## Content

### Definition of Ontology
An ontology is a formal and explicit representation of knowledge or information about a particular domain. It serves as a structured framework for organizing and categorizing knowledge in a way that allows for clear and precise communication and reasoning. Ontologies are commonly used in various fields, including philosophy, computer science, information science, and artificial intelligence but our focus area is knowledge representation, knowledge graphs.

Ontology in Knowledge Graph (KG) is used to represent the entities and relationship between them. These can be categorized as below:

`Concepts:` Ontologies define the concepts or entities within a specific domain of knowledge. These concepts can be related to each other hierarchically, forming a taxonomy or ontology hierarchy. For example, In supply chain system, Product, Parts, Organization, can be the entities and are linked by relatoinships between them.

`Relationships:` In an ontology relationships between concepts are specifed, indicating how different concepts are connected or related to each other. These relationships can include "is-a" "part-of" "has-property" and many others, depending on the domain. For instance, Father is-a Person, Child hasFather Father. Here, hasFather and is-a are the relationships between entities.

`Attributes:` Ontologies often include attributes or properties associated with concepts. These properties describe characteristics, features, or attributes of the concepts. The attributes can simply be a Data or Literal defining the "name" "age" "salary" etc or it can be a object property defining another entity. For example, in a medical ontology, a "patient" concept might have attributes like "age" "gender" and "diagnosis"

`Axioms:` Ontologies may include logical axioms that define constraints, rules, or inference rules for reasoning about the domain. These axioms help ensure the consistency and accuracy of the ontology. We can define a rule for Father like, Father is-a Person and there exists a relation hasChild to a node of type Person.

Below is the example ontology of product:

    @prefix kastle: <http://www.kastle-lab.org/ld/ontology/>
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix schema: <http://schema.org/> .

    kastle:N1 a schema:Product ,
       schema:hasPart kastle:P1 ,
       schema:hasPart kastle:P2;
       
    kastle:N2 a schema:Product ,
       schema:hasPart kastle:P2 ,
       schema:hasPart kastle:P3;

    kastle:P1 a kastle:Part .
    kastle:P2 a kastle:Part .
    kastle:P3 a kastle:Part .

    kastle:Part rdfs:subClassOf schema:Product
    
In examining the components of ontology, it becomes evident that the examples provided span various domains intentionally. This diversity underscores a crucial point: ontological descriptions are distinct and tailored to the unique requirements of each domain. For instance, consider the attributes associated with the concept of a "person" in a family knowledge graph versus a medical knowledge graph. In the family knowledge graph, attributes like "relationship status" and "family role" might be pertinent, reflecting the familial context. On the other hand, in a medical knowledge graph, attributes such as "medical history," "diagnoses," and "allergies" become central, aligning with the healthcare focus. This illustrates how ontology construction necessitates domain-specific customization to accurately represent the knowledge within that domain.

### Vocabulary in Ontology

Vocabulary serves as the foundation of ontology, offering a standardized set of words and their meanings that enable precise knowledge representation, effective communication, and smooth interoperability within a particular domain. It brings clarity and consistency to the naming and description of concepts, attributes, and relationships, reducing confusion and enhancing automated reasoning capabilities. This linguistic foundation also plays a crucial role in data integration, semantic search, and knowledge retrieval, ensuring seamless blending of data from various sources and promoting accurate information exchange between humans and machines. In the world of ontology development, vocabulary is the building block, providing the essential tools for structuring and organizing domain-specific knowledge. It encourages collaboration among domain experts and enhances the overall usefulness of ontological models.

In the intricate field of ontology development, the choice of vocabulary depends on specific domains and use cases. Schema.org stands out as a versatile and widely-used option, known for structuring web content and improving online discoverability. Additionally, when dealing with social networks and linked data complexities, the Friend of a Friend (FOAF) vocabulary takes the spotlight, offering a standardized framework for representing individuals and their intricate web of social connections and online identities.

For domains requiring specialized knowledge representation, dedicated vocabularies come into play. In healthcare, vocabularies like SNOMED CT and LOINC provide standardized codes for clinical concepts, medical procedures, and data interoperability. In the financial sector, the Financial Industry Business Ontology (FIBO) offers a comprehensive vocabulary for describing financial instruments, securities, and regulatory compliance.

When exploring geospatial data and location-based services, GeoNames and GeoSPARQL provide standardized terms for describing geographical features and enabling spatial queries. This array of vocabulary options empowers ontology developers to create precise and contextually relevant models, tailored to their specific domains. Whether the focus is on enhancing web content, capturing medical knowledge, modeling social networks, or navigating the intricacies of finance and geospatial data, vocabulary choices play a critical role in successful ontology development.

### Unveiling the Super Trio in Ontologies

These three components are foundational in every ontology, forming essential building blocks crucial for defining schemas, ontologies, and constructing Knowledge Graphs:

`RDF (Resource Description Framework):` RDF is a foundational ontology language used for representing and linking data on the web. It provides a simple and flexible way to describe resources and their relationships, using subject-predicate-object triples. RDF enables the creation of knowledge graphs by expressing facts and relationships in a machine-readable format, making it a fundamental component of the Semantic Web. Please [click here](../RDF/RDF.md) to get more information on RDF.

`RDFS (RDF Schema):` RDFS builds upon RDF by introducing a basic ontology vocabulary for defining classes and properties. It allows for more structured knowledge representation, enabling the creation of hierarchies of classes and specifying domains and ranges for properties. RDFS is valuable for organizing RDF data and providing a level of semantic expressiveness. Please [click here](../RDFS/RDFS.md) to get more information on RDFS.

`OWL (Web Ontology Language):` OWL is a powerful and expressive ontology language that extends RDF and RDFS. It offers a rich set of constructs for modeling complex ontologies, including classes, individuals, properties, and logical axioms. OWL supports formal reasoning and inference, making it suitable for advanced knowledge representation tasks, such as knowledge-based systems and automated reasoning applications. Please [click here](../OWL/OWL.md) to get more information on OWL.

### Additional Information about Ontology
Ontologies serve as the foundation for every Knowledge Graph (KG), and when available on the web, they can be seamlessly integrated into our KGs. Leading examples include OWL, RDF, and RDFS:

        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix owl: <http://www.w3.org/2002/07/owl#> .
        
If you aim to address domain-specific challenges or create a generalized ontology, there's an opportunity to define a new ontology that can be adopted by KG developers across the board, ensuring consistent knowledge representation. For example:

        @prefix kastle: <http://www.kastle-lab.org/2024/uowl#> .

The above URI can be become base URI, if you create a generalized Universal Web Ontology Language (UOWL).
        

## Related KGC Media
* Workshop Example
* Tutorial Example


## References
[1] [Difference between Ontology and Knowledge Graph](https://enterprise-knowledge.com/whats-the-difference-between-an-ontology-and-a-knowledge-graph/)

[2] [Understanding Ontologies](https://medium.com/codex/understanding-ontologies-and-knowledge-graphs-4664afc4f961)

[3] [Schema.org Vocabulary](https://schema.org/)

[4] [FOAF Vocabulary](http://xmlns.com/foaf/0.1/)

[5] [RDF](https://www.w3.org/RDF/)

[6] [RDFS Schema](https://www.w3.org/TR/rdf12-schema/)

[7] [OWL](https://www.w3.org/OWL/)

[8] Dean Allemang and Jim Hendler Semantic Web for Working Ontologist [link](https://www.sciencedirect.com/book/9780123859655/semantic-web-for-the-working-ontologist)


## External Media References
* [Detailed Explanation of Ontology by Synaptica](https://www.youtube.com/watch?v=7qIBex7a0kE&t=1856s)
* [Brief Explantion Of Ontology](https://www.youtube.com/watch?v=5pKD1DgeLBA)
* [The powerful duo: RDF and OWL](https://www.youtube.com/watch?v=zteyEk9LADs)

## Contributors
* Cogan Shimizu
* Rakesh Kandula
