# What is an Identifier
## Details
* Category: [Foundational](../categories/Foundational.md)
* Module Prerequisites: None
* Audience: [Any](../audiences/Any.md)
* Level: [Beginner](../levels/Beginner.md)

## Content

### Question

What is the difference between a URL, URI, and URN?
* URL :
  * A URL is a specific type of URI.
  * It provides both the address of a resource and the means to locate it.
  * Consists of a protocol (such as http, https), domain name or IP address, and optional path and query parameters.
* URI :
  * A broader term that encompasses both URLs and URNs.
  * Identifies a resource using a string of characters.
  * Used to locate or identify resources on the internet.
  * A string whose format depends on the naming scheme is followed by a naming scheme specifier to produce a complete URI. 
* URN :
  * A type of URI that identifies a resource by name in a particular namespace.
  * Focuses on naming a resource rather than its location.
* URIs (Uniform Resource Identifiers), URLs (Uniform Resource Locators), and URNs (Uniform Resource Names) serve crucial roles in identifying and connecting various entities and resources in the context of knowledge graphs.
* The primary method of identification is provided by URIs, whereas URLs provide information on the location of resources, and URNs provide consistent naming without relying on specific locations. The precise requirements of the graph and the characteristics of the resources being represented will determine which identifier should be used.
* A key component of Knowledge Graphs and the digital environment are URIs, which include URLs and URNs. They support consistent data integration and semantic interoperability while ensuring each entity's unique identification. URIs facilitate the development of interconnected and valuable graphs by facilitating linkages, data discovery, and accessibility. Data integrity over the long term is guaranteed by their contribution to durability, scalability, and interoperability with developing technologies. Furthermore, URIs play a crucial role in the Semantic Web's goal, which supports machine-understandable data representation for sophisticated search and knowledge applications.

## Example 
* Suppose we have a Knowledge Graph that represents information about books, authors, and publishers. Here's a simplified triple (subject-predicate-object) with a URI as the subject to demonstrate its usability and connectivity :
  * Triple:

    Subject (URI): http://example.org/authors/Antrea
    Predicate: http://example.org/authorOf
    Object: http://example.org/book




## Related KGC Media
* Workshop Example
* Tutorial Example

## References
[1] https://www.w3.org/Addressing/URL/uri-spec.html
[2] https://www.w3.org/TR/cooluris/

## Contributors
* Cogan Shimizu
* Antrea Christou