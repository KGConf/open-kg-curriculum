# Dublin Core
## Details
* Category: [Resources](../categories/Resources.md)
* Module Prerequisites: [RDFS](../modules/RDFS.md)
* Audience: [Student, Developer](../audiences/Student,_Developer.md)
* Level: [Beginner](../levels/Beginner.md)

## Content

Dublin Core is a widely used metadata standard first developed at a 1995 conference hosted by the [OCLC](https://www.oclc.org/en/about.html?cmpid=md_ab)--a global library organization--and the [National Center for Supercomputing Applications](https://www.ncsa.illinois.edu)(NCSA). Although the Dublin Core standard was initially defined in the form of HTML, the DC Terms vocabulary is fully RDF compliant and easy to incorporate into users' own ontologies.

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

An extended set of terms was created in 2001. The initial and extended sets were combined as the [Dublin Core terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) vocabulary in 2008. The terms vocabulary is more restrictive than the initial element set, specifying where the object of a property can be a literal or must refer to a member of a class. For example, here are the differences between the dc and dcterms:namespace for the property "format":

```URI:     http://purl.org/dc/elements/1.1/format
Label:      Format
Definition:     The file format, physical medium, or dimensions of the resource.
Comment:        Recommended practice is to use a controlled vocabulary where available. For example, for file formats one could use the list of Internet Media Types [MIME].```
    
```URI:     http://purl.org/dc/terms/format
Label:      Format
Definition:     The file format, physical medium, or dimensions of the resource.
Comment:        Recommended practice is to use a controlled vocabulary where available. For example, for file formats one could use the list of Internet Media Types [MIME]. Examples of dimensions include size and duration.
Type of Term:       Property
Range Includes:     
      http://purl.org/dc/terms/MediaType
      http://purl.org/dc/terms/Extent```



## Related KGC Media
* Workshop Example
* Tutorial Example

## References
[1] Reference example.

## Contributors
* Cogan Shimizu
* Glenn Clatworthy
