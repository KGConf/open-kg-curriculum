# RDF
## Details
* Category: [Standards, Markup Languages](../categories/Standards,_Markup_Languages.md)
* Module Prerequisites: None
* Audience: [Student, Developer](../audiences/Student,_Developer.md)
* Level: [Beginner](../levels/Beginner.md)

## Content

#### Introduction

The world wide web serves up billions, if not trillions, of pages of content describing a seemingly infinite number of subjects. As a mechanism for advanced research, however, the web's strength can also be its greatest weakness. The sheer number of pages--as well as most users' dependence on commercial search engines--can make researching and sharing knowledge about a single topic difficult or impossible. The [semantic web](https://github.com/GlennClatworthy/open-kg-curriculum/blob/master/curriculum/modules/History_of_the_Semantic_Web/History_of_the_Semantic_Web.md), linked data, and RDF provide an alternative approach to consolidating information from the web.

#### What Is RDF?

RDF, or the **Resource Description Framework**, is [a standard model for data interchange on the Web](https://www.w3.org/RDF/). Maintained and promoted by the [World Wide Web Consortium (W3C)](https://www.w3.org), RDF helps organizations, companies, and individuals organize information from multiple websites and other internet sources in a structured format supporting advanced knowledge sharing and discovery.

#### The Structure of RDF

Basic RDF is composed of three-part statements, known as *triples*, which describe the attributes of resources on the web. For example, the statement:

    William Shakespeare | wrote | Hamlet
    
can resolve to:

    <https://en.wikipedia.org/wiki/William_Shakespeare>  <https://schema.org/author>  "Hamlet"
    
In the RDF lexicon, the three columns in a triple are called **subject**, **predicate**, and **object**. The subject column refers to the thing the source is describing, in this case William Shakespeare. The predicate column defines some aspect, or property, that you want to attribute to William Shakespeare. The third column, object, contains the value of the property.

Notice that the first two columns above are **URIs** (a more generalized form of URLS) and the last is a text string in quotation marks. One hard and fast rule of RDF is that subject and predicate columns must always be expressed in URI form. The object column may be expressed either as a text string or as another URI, the value of which will become apparent later.

URIs serve as unique identifiers, similar to a U.S. Social Security number or the item number of a component in a warehouse. Although, theoretically, a user could mint their own fake URIs as a unique identifier, good practice is to insure that 



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
* Glenn Clatworthy
