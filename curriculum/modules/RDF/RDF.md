# RDF
## Details
* Category: [Standards, Markup Languages](../categories/Standards,_Markup_Languages.md)
* Module Prerequisites: None
* Audience: [Student, Developer](../audiences/Student,_Developer.md)
* Level: [Beginner](../levels/Beginner.md)

## Content
RDF, or the **Resource Description Framework**, is [a standard model for data interchange on the Web](https://www.w3.org/RDF/). Maintained and promoted by the [World Wide Web Consortium (W3C)](https://www.w3.org), RDF helps individuals and organizations link information from multiple websites and other internet sources in a structured format supporting advanced knowledge sharing and discovery.

Basic RDF is composed of three-part statements defining the attributes of the web resources it's describing. For example:

    William Shakespeare | wrote | Hamlet
    
can resolve to:

    <https://en.wikipedia.org/wiki/William_Shakespeare> | <https://schema.org/author> | "Hamlet"
    
In the RDF lexicon, these three columns are called **subject**, **predicate**, and **object**. The subject column refers to the thing the source is describing, in this case William Shakespeare. The predicate column defines some aspect, or property, that you want to attribute to William Shakespeare. The third column, object, contains the value of the property.

## Related Questions
* RDF vs. RDFS:
  * [What does RDFS (RDF Schema) add to RDF (the Resource Description Format)? Why would I use it in my ontology?](https://github.com/GlennClatworthy/kgc_discussion_group/wiki/Questions,-we-have-questions)

## Related KGC Media
* Knowledge Graph Conference Bookclub Session: [Semantic Web for the Working Ontologist, Third Edition, Chapters 1-3](https://watch.knowledgegraph.tech/packages/kgc-21-attendees/videos/bookclub2)

* Tutorial Example

## References
[1] Reference example.

## Contributors
* Cogan Shimizu
