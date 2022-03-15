# RDF
## Details
* Category: [Standards, Markup Languages](../categories/Standards,_Markup_Languages.md)
* Module Prerequisites: None
* Audience: [Student, Developer](../audiences/Student,_Developer.md)
* Level: [Beginner](../levels/Beginner.md)

## Content

#### Introduction

The world wide web serves up billions, if not trillions, of pages of content describing a seemingly infinite number of subjects. As a mechanism for advanced research, however, the web's strength can also be its greatest weakness. The sheer number of pages--as well as most users' dependence on commercial search engines--can make researching and sharing knowledge about a single topic a challenge. The [semantic web](https://github.com/KGConf/open-kg-curriculum/blob/master/curriculum/modules/History_of_the_Semantic_Web/History_of_the_Semantic_Web.md), linked data, and RDF provide an alternative approach to consolidating information from the web.

#### What Is RDF?

RDF, or the **Resource Description Framework**, is ["a standard model for data interchange on the Web."](https://www.w3.org/RDF/) Maintained and promoted by the [World Wide Web Consortium (W3C)](https://www.w3.org), RDF helps organizations, companies, and individuals organize information from multiple websites and other internet sources in a structured format supporting advanced knowledge sharing and discovery.

#### The Structure of RDF

Basic RDF is composed of three-part statements, known as *triples*, which point to resources on the web and assign values to properties describing them.  For example, the statement:

    William Shakespeare | wrote | Hamlet
    
tells us that an individual (Shakespeare) has a property (wrote), the value of which is "Hamlet." That statement also can be expressed as:

    <https://en.wikipedia.org/wiki/William_Shakespeare>  <https://schema.org/author>  "Hamlet".
    
In the RDF lexicon, the three columns in the above triple are called **subject**, **predicate**, and **object**. The *subject* column points to a web resource that the triple is describing, in this case the Wikipedia entry for William Shakespeare. The predicate column defines some aspect, or *property*, that you want to attribute to the subject. Here it points to a property called "author" that is documented at a website called schema.org. The third column, *object*, contains the value of the property, namely "Hamlet."

Notice that the first two columns above are written as [**URIs**](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) (uniform resource identifiers), which are a more generalized form of URLs, and the last is a text string in quotation marks. A fundamental rule of RDF is that *subject and predicate columns must always contain URIs*. The object column may be written either as a text string (as above) or as another URI.

URIs serve as unique identifiers, similar to a U.S. Social Security number or the item number of a component in a warehouse. Although there's no reason why a URI has to point to a real resource on the web, it is considered best practice to do so, allowing a user to follow a URI to its source in order to find out more about it.

RDF's structure is similar to rows in spreadsheets in that it allows the repetition of elements. For example:

    <https://en.wikipedia.org/wiki/William_Shakespeare>  <https://schema.org/author>  "Hamlet".
    <https://en.wikipedia.org/wiki/William_Shakespeare>  <https://schema.org/author>  "Macbeth".

are two perfectly valid triples, differing only in the different works to which they refer.

Finally, notice that the first two columns refer to resources available at two different locations. The true power of RDF lies in its ability to seemlessly combine information, whether it be Wikipedia pages, articles from commercial websites, or terms from a variety of online vocabularies. Thus the disparate, chaotic world wide web can be interconnect and organized using the simple structural components of RDF.

#### Serializations

It's important to note that RDF is *not* a file format. A variety of formats, known as [serializations](https://github.com/KGConf/open-kg-curriculum/blob/master/curriculum/modules/RDF_Serializations/RDF_Serializations.md), are available, each differing in the way triples are structured in text files. For example, the above examples are written as [n-triples](https://www.w3.org/TR/n-triples/), which arguably is the simplest and most straightforward RDF serialization format.

Users choose serializations based on their needs and compatibility with other systems. One of the most compact and therefore popular formats is called **Turtle**. Here is the above example expressed in Turtle form:

    @prefix wiki: <https://en.wikipedia.org/wiki/>.
    @prefix sch: <https://schema.org/>.
    
    wiki:William_Shakespeare sch:author "Hamlet", "Macbeth".

#### Composing RDF documents

Composing an RDF document can be as simple as opening up a text editor and writing triples in the author's preferred format. However, a wide variety of commercial and open source [modeling tools](https://github.com/KGConf/open-kg-curriculum/tree/master/curriculum/modules/Survey_of_Modeling_Tools/Survey_of_Modeling_Tools.md) are available to assist the user in composing RDF. Third party software offers two advantages: it provides a standard interface that can simplify the construction of triples; and it may provide checking capabilities to prevent the user from committing structural and logical errors.

#### RDF and Triplestores

RDF's value begins to emerge when it is loaded into a special kind of database called a [triple store.](https://github.com/KGConf/open-kg-curriculum/blob/master/curriculum/modules/Survey_of_Triplestores/Survey_of_Triplestores.md) Triple stores can be used to import, combine, update, query, and often [visualize](https://github.com/KGConf/open-kg-curriculum/blob/master/curriculum/modules/Survey_of_Visualization_Tools/Survey_of_Visualization_Tools.md) the information stored in RDF formats. Similar to modelling tools, triple stores are available as paid commercial, free commercial, and open source versions distributed by various companies and organizations. These applications employ a query language called [SPARQL](https://github.com/KGConf/open-kg-curriculum/blob/master/curriculum/modules/SPARQL/SPARQL.md), which is similar in structure to the Turtle example above.

#### Beyond Basic RDF

While RDF provides the basic template for organizing linked data, it's only a starting point. Extensions to RDF as found in standards like RDFS ...
 
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
