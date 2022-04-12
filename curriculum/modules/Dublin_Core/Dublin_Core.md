# Dublin Core
## Details
* Category: [Resources](../../categories/Resources.md)
* Module Prerequisites: [RDFS](../../modules/RDFS/RDFS.md)
* Audience: [Student](../../audiences/Student.md), [Developer](../../audiences/Developer.md)
* Level: [Beginner](../../levels/Beginner.md)

## Content

### Definition

Dublin Core is a foundational metadata standard first developed at a 1995 conference hosted by [OCLC](https://www.oclc.org/en/about.html?cmpid=md_ab) and the [National Center for Supercomputing Applications](https://www.ncsa.illinois.edu) (NCSA). The standard was named after Dublin, Ohio, the conference's location. Although initially expressed in the form of HTML, Dublin Core is now [RDF](../../modules/RDF/RDF.md)-compliant and straightforward to incorporate into users' own ontologies.

The initial schema, known as the Dublin Core Metadata Element Set, featured fifteen elements (i.e., properties) covering a broad range of library applications:

* contributor
* coverage
* creator
* date
* description
* format
* identifier
* language
* publisher
* relation
* rights
* source
* subject
* title
* type

The initial fifteen elements and an extended set were combined as the [Dublin Core terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) vocabulary in 2008. Note that the elements in the dc:terms collection, while mirroring the original fifteen, are more restrictive, specifying when the object of a property can be a literal or must refer to a member of a class. For example, here are the differences between the dc:elements and dc:terms namespaces for the property "format":

#### Elements Namespace:

    URI:           http://purl.org/dc/elements/1.1/format
    Label:         Format
    Definition:    The file format, physical medium, or dimensions of the resource.
    Comment:       Recommended practice is to use a controlled vocabulary where available. 
                   For example, for file formats one could use the list of Internet Media Types [MIME].
                   
#### Terms Namespace:
    
    URI:           http://purl.org/dc/terms/format
    Label:         Format
    Definition:    The file format, physical medium, or dimensions of the resource.
    Comment:       Recommended practice is to use a controlled vocabulary where available. For example, for file formats one could use the
                   list of Internet Media Types [MIME]. Examples of dimensions include size and duration.
    Type of Term:  Property
    Range Includes:     
                   http://purl.org/dc/terms/MediaType
                   http://purl.org/dc/terms/Extent
                   
                   
### Example

Here is a quick example of Dublin Core in the Turtle format. The ontology below defines two new classes--"Author" and "Publishing_company"--and three resources. Notice how the details of the book *The New Adventures of Melvin Cowznofski* are expressed entirely using a dc:terms class as an object and four dc:terms properties as predicates:

    @prefix : <http://tutorial.madmen.com/pub#> .
    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix owl: <http://www.w3.org/2002/07/owl#> .
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

    :Author
      rdf:type rdfs:Class ;
      rdfs:label "Author" ;
      rdfs:subClassOf dcterms:Agent ;
    .
    :Harvey_Kurtzman
      rdf:type :Author ;
      rdfs:label "Harvey Kurtzman" ;
    .
    :NewAdventuresMelvinCowznofski
      rdf:type dcterms:BibliographicResource ;
      dcterms:creator :Harvey_Kurtzman ;
      dcterms:identifier "0134589" ;
      dcterms:publisher :Potrzebie_Publications ;
      dcterms:title "The New Adventures of Melvin Cowznofski" ;
    .
    :Potrzebie_Publications
      rdf:type :Publishing_company ;
      rdfs:label "Potrzebie Publications" ;
    .
    :Publishing_company
      rdf:type rdfs:Class ;
      rdfs:label "Publishing Company" ;
    .

### Application

It's natural for a beginning ontologist to want to start from scratch, minting a complete set of unique properties and related Universal Resource Identifiers (URIs) to meet their unique requirements. However, much of the power of the semantic web springs from its inherent ability to combine, as triples, multiple vocabularies from established online resources. Here are two important reasons for making use of Dublin Core (or other existing standard ontologies) as a bases for independent work:

* Dublin Core is well-documented, well-supported, and so universally adopted that the potential for it continuing as a long-term, internationally applicable resource is very high. Other vocabularies, including those local to organizations, are more likely to disappear over time.
* Adopting a standard like Dublin Core simplifies the process of merging or connecting disparate ontologies. If two ontologists managing similar information employ the same DC elements (e.g., creator, publisher), they are much less likely to have to create new triples connecting properties and classes from one dataset to another.

### In Summary

Dublin Core is broadly applicable to content managed by libraries, publishing, media, and other entities. The standard should be a first stop for any developer seeking to build an ontology in those subject areas.

## Related KGC Media
* [Semantic Web for the Working Ontologist, Third Edition, Chapter 4, p72.](https://www.morganclaypoolpublishers.com/catalog_Orig/product_info.php?products_id=1564)
* Workshop Example
* Tutorial Example

## References
[1] [Dublin Core Metadata Initiative](https://www.dublincore.org) homepage
[2] [Dublin Core](https://en.wikipedia.org/wiki/Dublin_Core) on Wikipedia

## Contributors
* Cogan Shimizu
* Glenn Clatworthy
