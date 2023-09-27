# What is an Ontology
## Details
* Category: [](../categories/.md)
* Module Prerequisites: [](../modules/.md)
* Audience: [](../audiences/.md)
* Level: [](../levels/.md)

## Content
An ontology is a formal and explicit representation of knowledge or information about a particular domain. It serves as a structured framework for organizing and categorizing knowledge in a way that allows for clear and precise communication and reasoning. Ontologies are commonly used in various fields, including philosophy, computer science, information science, and artificial intelligence but our focus area is knowledge representation, knowledge graphs.

Ontology in Knowledge Graph (KG) is used to represent the entities and relationship between them. These can be categorized as below:
1. Concepts
2. Relationships
3. Attributes
4. Axioms

`Concepts:` Ontologies define the concepts or entities within a specific domain of knowledge. These concepts can be related to each other hierarchically, forming a taxonomy or ontology hierarchy. For example, In supply chain system, Product, Parts, Organization, can be the entities and are linked by relatoinships between them.

`Relationships:` In an ontology relationships between concepts are specifed, indicating how different concepts are connected or related to each other. These relationships can include "is-a" "part-of" "has-property" and many others, depending on the domain. For instance, Father is-a Person, Child hasFather Father. Here, hasFather and is-a are the relationships between entities.

`Attributes:` Ontologies often include attributes or properties associated with concepts. These properties describe characteristics, features, or attributes of the concepts. The attributes can simply be a Data or Literal defining the "name" "age" "salary" etc or it can be a object property defining another entity. For example, in a medical ontology, a "patient" concept might have attributes like "age" "gender" and "diagnosis"

`Axioms:` Ontologies may include logical axioms that define constraints, rules, or inference rules for reasoning about the domain. These axioms help ensure the consistency and accuracy of the ontology. We can define a rule for Father like, Father is-a Person and there exists a relation hasChild to a node of type Person.

If we look above for each part of ontology described. The example used was not from the same domain, the usage of diverse examples are intentional to point that the ontological desription is distinct for every domain. For Instance, the attributes associted with person in a family KG and in medical KG differs as we need to represent different Knowledge.

## Related KGC Media
* Workshop Example
* Tutorial Example

## References
[1] Reference example.

## Contributors
* Cogan Shimizu
