# SHACL
## Details
* Category: [Standards](../categories/Standards.md)
* Module Prerequisites: [RDF serializations](../modules/RDF_serializations.md)
* Audience: [Student, Developer](../audiences/Student,_Developer.md)
* Level: [Intermediate](../levels/Intermediate.md)

## Content
* Ensuring data quality , interpretation and code validation can be challenging,  
RDF graph validation is crucial and one strong tool in doing so is SHACL.
* SHACL : “Shapes Constraint Language”
* How to use it : Input -> Data Graph and/or Shapes Graph  written in ttl format or JSON. Output -> Validation Report expressed as a graph.
* Tools used : 1. Python library called pyshacl. 2.Apache Fuseki. - [link here](https://jena.apache.org/documentation/shacl/index.html) 3. GraphDB.
* SHACL helps to detect errors, inconsistencies, and incomplete data in RDF data graphs.It improves data quality, interoperability, and consistency. Also it can help when “translating” code from one language to another.
* Examples : 1. Ensuring that all instances of a certain class have a required property. 2.Verifying that the value of a property is within a certain range or matches a specific format. 3. Checking that the structure of a graph conforms to a specified template.
* The SHACL Advanced Features specification extends the core SHACL specification with additional capabilities, including conditional constraints, parameterized constraints, and custom constraint components.For example, let's say we have a dataset of books, where each book has a title, author, and year of publication. We want to create a SHACL validation that checks that each book conforms to a certain set of rules:
1. The title must be a string with a minimum length of 3 characters.
2. The author must be a resource with a name and a biography.
3. The year of publication must be a valid integer between 1000 and the current year.
4. If the book is part of a series, the series title must be a string with a minimum length of 3 characters.

## Related KGC Media
* Workshop Example
* Tutorial Example

## References
[1] We can use GraphDB for Shacl validation :  https://graphdb.ontotext.com/documentation/10.1/shacl-validation.html
[2] https://graphdb.ontotext.com/documentation/10.1/shacl-validation.html
[3] https://www.w3.org/TR/shacl/ - introduction
[4] https://jena.apache.org/documentation/shacl/index.html
[5] https://github.com/KnowWhereGraph/KWG-SHACL
[6] https://www.w3.org/TR/shacl-af/ : Advanced Features 


## Contributors
* Cogan Shimizu
* Antrea Christou