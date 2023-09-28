# OWL
## Details
* Category: [Standards](../categories/Standards.md)
* Module Prerequisites: [RDF Serializations, OWAxCWA, Description Logic](../modules/RDF_Serializations,_OWAxCWA,_Description_Logic.md)
* Audience: [Student, Developer](../audiences/Student,_Developer.md)
* Level: [Intermediate](../levels/Intermediate.md)

## Content
What was Learned in the Course 
	 
   This course helped reinforce my understanding of description logic, propositional logic, and predicate logic. While I was familiar with the concept of each, it had been a few years since I had last used them. This course taught me about ontologies and knowledge representation. I had never worked with knowledge graphs before, so this was a good experience for me. Additionally, I hadn’t had any experience with ontologies or Protégé, so building the small family tree ontology and visualizing it was helpful. Finally, all the rule surrounding Systematic Axiomization were new to me, but they helped me understand the relationships that we need to look for between sets of information. 

Web Ontology Language
   
  This research paper covers a brief history of Web Ontology, its relationship to Semantic Web, and its functionality.  To discuss Web Ontology Language effectively, one should first establish an understanding of ontology. Simply put, ontology is the study of being and the relationships surrounding it. An ontology in the concept of this paper, is the representation and organization of knowledge. 

After the development of the World Wide Web, researchers looked for a way to make the web not only human readable, but also machine readable. As the data on the web got larger in size and more diverse, the development of the Semantic Web was started to allow for the web to be easily machine understandable. Tim Berners-Lee, the founder of the Semantic Web, envisioned that the Semantic Web would be most effective with the development of Linked Open Data and Semantic Metadata [1]. Linked Open Data “is structured data modeled as a graph and published in a way that allows interlinking across servers [1].” This would continue to allow humans to access and read the data, but it would also allow for machines to better read and understand the information on the web. The Semantic Metadata would add descriptions on “web pages to better describe their meanings [1].” This would help to identify relationships between information on semantic web pages. To enable the representation of this knowledge, and achieve Tim Berners-Lee’s goal of the Semantic Web, Web Ontology Language was created.
	
 In 2004, the World Wide Web Consortium(W3C) created a “knowledge representation language” called Web Ontology Language [2]. This language was “derived from” a combination of Ontology Interference Layer (OIL) and DARPA Agent Markup Language (DAML) [2]. As Web Ontology Language evolved, development improved to include additional features and capabilities. Further developments lead to the release of Web Ontology Language 2 in 2009 [2].   
	
 Web Ontology Language is also built in combination with Resource Description Framework (RDF) to achieve the vision of the Semantic Web [3]. RDF helps with the automation of data processing as it maps out information according to the RDF triple, subject predicate object [3]. Web Ontology Language builds off this and can determine more complex and expressive representations. 
The strengths of Web Ontology Language are “expressive and flexible data modeling,” and “efficient automated reasoning [2].” Web Ontology Language is able to expressively represent specific bits of information as well as it’s relationships in both human and machine readable form [2]. Additionally, Web Ontology Language is very flexible. This allows for changes to made quickly and easily. Web Ontology Language is also proficient at automated reasoning. Web Ontology Language can also efficiently identify knowledge and relationships from data. This is beneficial to Machine Learning and Artificial Intelligence algorithms as it helps them improve learning and automation. 
Web Ontology Language was created to be a “markup language for publishing and sharing ontologies [4].” This representation of ontologies helps machines improve data processing. Web Ontology Language is built primarily on Description Logic. Description Logic is helpful for “defining, integrating, and maintaining ontologies [5].”  Furthermore in Christophe Debruyne’s lecture covering Description Logics, he defines Description Logics as “Describe[ing] the domain... in terms of concepts, roles, and individuals [6].” This definition of Description Logic helps Web Ontology Language have a means of defining classes, relationships, and constraints. 
	
 Web Ontology Language helps express knowledge through classes, properties, individuals, and datatypes [4]. Classes allow for the grouping of items “with similar characteristics [4].” This allows for a clearer representation of knowledge, from which further relationships can be determined through logic. Properties help represent “instances of” classes or values [4]. Properties also give information of domain and range. There are two main types of Properties: Object Properties, and Datatype Properties [4]. Object Properties are the representation and the relationships between individuals, and Datatype Properties are the representation of the links between the individual and the datatype [4]. Individuals can be classified “with individual axioms [4].” There are largely 2 kinds of these individual axioms, also known as individual facts, “facts about class membership and property values,” and “facts about individual identity [4].” Web Ontology Language expressing knowledge through individual axioms helps express the relationships that individuals have to classes, themselves, and others. And finally, Datatypes are an “instance of the class [4].” This helps represent information as it helps define the range.  
	
 To make the language both human readable and machine understandable there must be a certain syntax followed. Through Web Ontology Language, one can reference the objects in the knowledge graph and define them with a set of colons. Colons help to reference objects and define predicates. This language efficiently uses syntax to reference the relationships between the subjects, predicates, and objects. 
	
 Web Ontology Language helps provide a thorough framework for representing knowledge in machine readable form. Web Ontology Language can create classes from which one can represent separate instances of the classes. For example, a Person class could be created through ```:Person rdf:type owl:Class.``` From there, a specific instance of this class, or an individual person, could be defined using ```:Name rdf:type :Person.``` To continue the examples of Persons, Web Ontology Language could then define the specific relationships between individuals. An example of such is as follows: ```Jim :hasSon :Joe``` where it shows the familial relationship between a father and a son.  These examples are merely a few basic ways in which Web Ontology Language can represent knowledge and their relationships. Additionally, it can be used to represent properties. For example: 
```
schema:performer a owl:ObjectProperty ;
    rdfs:domain schema:Event ;
    rdfs:range schema:Person .
```
This identifies the relationship between a person, who is a performer, to a certain event [example taken from kgc2021-1.ttl]. These representations, written in Web Ontology Language, can easily be read by machines which allows for computer software to better understand and process the knowledge and relationships. 
	
 Through the examples shown above, it is shown how the language works with syntax to become both human and machine readable. One can use the syntax to initialize classes, reference objects, and define predicates. In the schema example, schema is the defined object, and it is being named performer. ```a``` denotes an RDF Triple, subject predicate object, to show how performer and ObjectProperty are related. ```owl:ObjectProperty``` defines the type of the performer. From there the event is defined as the ```rdfs:domain schema:Event ;```. And finally, the range is defined as ```rdfs:range schema:Person```. This example shows the relationships between the performer, the event, and the person. 
	
 Web Ontology Language has proven its usefulness in tackling real world scenarios today. 
Due to its ability in representing knowledge in both human readable and machine understandable format, it has played a role in helping many diverse organizations. For example, the health and science research departments are benefitting off Web Ontology Language in their efforts to discover new and improved drugs [7]. The Semantic Web provides researchers across the word with the means to share research more easily in the discovery of new drugs [7]. Furthermore, use of Semantic Web tools, such as Web Ontology Language, are beneficial as it helps identify previously unknown connections and properties of certain compounds of a drug [8]. These tools help researchers identify relationships between the drugs, which can assist in predicting better performing drug compounds. 
	
 In conclusion, Web Ontology Language builds off Description Logic and RDF and is useful in expressing and representing knowledge and its corresponding information. Web Ontology Language has many strengths including its flexibility, expressiveness, and the ability to reason autonomously. The features of Web Ontology Language allow for a clear representation of knowledge, and a complete identification of the relationships between the data. Most notably, Web Ontology Language is in human readable and machine understandable form, allowing for computers to have an improved understanding of the data. Finally, Web Ontology Language has significant real-world impact as it can autonomously help identify more complex and previously unknown relationships and characteristics within data. This shows the significance of Web Ontology Language, as it can be used to assist in many different problems across many industries and disciplines. 

### Questions

* I'm frightened by the apparent complexity of OWL (the Web Ontology Language). What problems or challenges does it solve?

* OWL enables inferences by drawing on logic. So, many OWL-related references in particular refer to logic. How much logic do I really need to know to design and use ontologies?


## Related KGC Media
* Workshop Example
* Tutorial Example

## External Media References
* Christophe Debruyne. “Lecture 3: Description Logics.” Youtube.  https://www.youtube.com/watch?v=ZxDoxT00GfI. Minutes 5:17-18:45. [Accessed 28 September 2023].
  
## References
[1] “What is the Semantic Web.” Ontotext.  https://www.ontotext.com/knowledgehub/fundamentals/what-is-the-semantic-web/. [Accessed 27 September 2023]. 

[2] “Learn OWL and RDFS.” Cambridge Semantics.  https://cambridgesemantics.com/blog/semantic-university/learn-owl-rdfs/owl-101/. [Accessed 25 September 2023]. 

[3] “Introduction to the Semantic Web.” Graph DB. https://graphdb.ontotext.com/documentation/8.9/enterprise/introduction-to-semantic-web.html. [Accessed 23 September 2023]. 

[4] Sean Bechhofer, et al. “OWL Web Ontology Language Reference.” W3C, 10 February 2004. https://www.w3.org/TR/owl-ref/. [Accessed 26 September 2023].

[5] Franz Baader, et al. “Description Logics as Ontology Languages for the Semantic Web.” Springer Link. https://link.springer.com/chapter/10.1007/978-3-540-32254-2_14. [Accessed 25 September 2023]. 

[6] Christophe Debruyne. “Lecture 3: Description Logics.” Youtube.  https://www.youtube.com/watch?v=ZxDoxT00GfI. Minutes 6:19-7:25. [Accessed 28 September 2023]. 

[7] Huajun Chen, et al. “The Use of Web Ontology Languages and Other Semantic Tools in Drug Discovery.” National Library of Medicine, 19 April 2010.  https://pubmed.ncbi.nlm.nih.gov/22823127/. [Accessed 27 September 2023]. 

[8] Samantha Kanza, et al. “A New Wave of Innovation in Semantic Web Tools for Drug Discovery.” Taylor and Francis Online, 19 March 2019. https://www.tandfonline.com/doi/full/10.1080/17460441.2019.1586880. [Accessed 28 September 2023]. 


## Contributors
* Cogan Shimizu
* Calvin Greenewald 
