# Dublin Core
## Details
* Category: [Resources](../../categories/Resources.md)
* Module Prerequisites: [RDFS](../../modules/RDFS/RDFS.md)
* Audience: [Student](../../audiences/Student.md), [Developer](../../audiences/Developer.md)
* Level: [Beginner](../../levels/Beginner.md)

## Content

### Definition

Dublin Core is a foundational metadata standard first developed at a 1995 conference hosted by [OCLC](https://www.oclc.org/en/about.html?cmpid=md_ab) and the [National Center for Supercomputing Applications](https://www.ncsa.illinois.edu) (NCSA). The standard was named after Dublin, Ohio, the conference's location. Although initially expressed in the form of HTML, the Dublin Core is now [RDF](../modules/RDF/RDF.md)-compliant and straightforward to incorporate into users' own ontologies.

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

An extended set of terms was created starting in 2001, and the initial and extended sets were combined as the [Dublin Core terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) vocabulary in 2008. Note that the terms vocabulary is more restrictive than the original element set, specifying when the object of a property can be a literal or must refer to a member of a class. For example, here are the differences between the dc elements and dc terms namespaces for the property "format":

    URI:           http://purl.org/dc/elements/1.1/format
    Label:         Format
    Definition:    The file format, physical medium, or dimensions of the resource.
    Comment:       Recommended practice is to use a controlled vocabulary where available. 
                   For example, for file formats one could use the list of Internet Media Types [MIME].
    
    URI:           http://purl.org/dc/terms/format
    Label:         Format
    Definition:    The file format, physical medium, or dimensions of the resource.
    Comment:       Recommended practice is to use a controlled vocabulary where available. For example, for file formats one could use the
                   list of Internet Media Types [MIME]. Examples of dimensions include size and duration.
    Type of Term:  Property
    Range Includes:     
                   http://purl.org/dc/terms/MediaType
                   http://purl.org/dc/terms/Extent
      
### Application

It's natural for a beginning ontologist to want to start from scratch, minting a complete set of unique properties and related Universal Resource Identifiers (URIs) to meet their unique requirements. However, much of the power of the semantic web springs from its inherent ability to combine, in the triple format, multiple vocabularies from an enormous and increasingly diverse number of online resources. Dublin Core has wide applicability to the worlds of publishing and media and should be a first stop for any user working in those subject areas.

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
