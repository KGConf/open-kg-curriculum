# Nanopublications
## Details
* Category: [Methods](../categories/Methods.md)
* Module Prerequisites: [RDF Star](../modules/RDF_Star.md)
* Audience: [Student, Developer](../audiences/Student,_Developer.md)
* Level: [Intermediate](../levels/Intermediate.md)

## Content
"A nanopublication is the smallest unit of publishable information [1]". They are used so that scientists can make data more accessable and usable to each other. Nanopublications are typically formatted in resource description framework and has to have at minimum three elements to be complete. Those three needed elements are an assertation, a provenence, and the publication information. There is also sometimes a fourth element called a head but it is not always needed. Nanopublications can be visualized as a graph since they are based off of an RDF graph. An RDF statement is a triple representing a subject, predicate, and object in a <subject, predicate, object> format. Since they are based off of the RDF statements nanopublications can be searched and cited. Nanopublications contain scientific information, context for the information provided, and they contain metadata about the author and attribute information.

An assertation, also called an assertion, is the body of the nanopublication. This would be the main info that the scientists reading the publication will want to use. The assertion could be anything from what a certain scientist claims about something to the actual outcome of a scientific study. This means that the people using nanopublications for their research need to be careful and make sure that they know if the information they are using is coming from a reliable source whether it is from a study or just a claim from a scientist. Although this is the main body of the nanopublication it will usually be the smallest part of the nanopublication since it should be the smallest amount of publishable information possible. The provenence will add context to the assertation for the reader to know how the author came up with their assertation.

A provenence is information about how the assertation was made. This would be where someone could see if the assertion came from a claim or an actual scientific study. A provence is the appropriate place to store the parameters, how a study was conducted, and the scientific method used for the study if the assertation came from a scientific study. Provenences also contain any contextual information [2] that would be useful for the reader to know. This could be things like references that the scientists use to either make a claim or used to help with their study. The provenence could be fairly large or small depending on the assertation and how much context is needed for the reader. Publication information would be where you would cite any of the references that you used in your assertation.

Publication information in a nanopublication would contain data about the authors, the topic of the assertation, and any rights information that is needed. This is where information about the authors, credit given, and any citations would be found. This is important so the reader can both find out who the author(s) are and where they got their information so that they can make an informed decision on whether or not to use the nanopublication. The publication information could be the reason that stops a reader from using the assertation or not. The relation between the assertation, provenence, and the publication information comes from the head of the nanopublication.

A head is what correlates the assertation, provenence, and the publication information together. These can be useful if you have multiple assertations that you are dealing with but you will not always have to have one. It would be nice to have but you would not need one when you are only using one assertation since it is by itself it could be assumed that the provenence and publication information would go with it. Some implementations of nanopublications will not accept heads and will only use the assertation, provenence, and the publication information.

![image](https://github.com/KGConf/open-kg-curriculum/assets/97766241/bfc85f1a-17e8-47b6-ba73-0bdb758ff677) <br/>
[2] This example shows a gene-disease association of Colorectal Cancer. This example shows that the assertation is not in a way that you could use natural language or keywords to search for.

![image](https://github.com/KGConf/open-kg-curriculum/assets/97766241/13e35a3c-c871-448f-a016-39409a430442) <br/>
[3] This example shows thyroid hormone production and the effects of congenital hypothyroidism

![image](https://github.com/KGConf/open-kg-curriculum/assets/97766241/c69747b1-cf9d-4fc5-80bc-c1e31fe18a9b) <br/>
[4] This example shows that you could use a nanopublication to store information for a cipher so you could encrypt plaintext and decrypt ciphertext. However you would not want to publish this publically because then the keys would also be public.

Nanopublications can be used in a plethora of ways. They can be used to support scientific claims since they themselves are supposed to have some sort of scientific backing with the provenece and publication information provided in the nanopublication. Since nanopublications can be easily searched by machines [2] you can abuse that and write a program that scrapes them and finds any useful information for you. As you can imagine this could be extremely useful when trying to research a topic because you would be able to easily find a lot of information about it immediately from a computer. Them being able to be searched easily means that you can index them almost like a database and it would be a lot easier than trying to find the information on your own. One of the major motivations behind encouraging the use of nanopublications is once there are enough of them we would possibly be able to create a network of relations between different related nanopublications. 

Even with the benefits of nanopublications described above, they are not used much. Since they are not used much outside of certain circles this makes it hard and more time consuming to find and therefore they are rarely if ever cited. The nanopublications that are made are typically not human readable and as such can not be searched using natural language or keywords. There are also no current tools available that allow someone to relate or figure out the relation between two assertation so they are not yet able to be used to build a relationship network. I would assume that if more people knew about nanopublications than it would become more widely used as the benefits of using it could cause research to go much faster for everyone if they could easily find wanted and related accurate scientific information quickly because as of right now it usually takes a while for someone to sift though a bunch of bad information to find good scientific information to help them in their research or study. 

In conclusion I believe that right now most scientist are missing out on their research potential and could be more productive if we made it more of a standard in more diciplines. If we started teaching students in high school and college about nanopublications then overtime we may be able to get them to make some on their own and help grow nanopublications enough to where we can take full advantage of all of its benefits. With more people making nanopublications then there would be more nanopublications that are human readable and therefore would be able to be searched using natural language and keywords. We would also probably get many tools to help with the creation and relating of nanopublications because when more people are making them more people would want a tool to be made to make it easier to do a nanopublication. In my opinion by teaching more people about nanopublications and how to use them we could boost the efficiency of all future research since previous research would be more accessable faster and easier to more people.

## Related KGC Media
* Workshop Example
* Tutorial Example

## External Media References
iDigBio, “Nanopublications for biodiversity- concept, formats and implementation,” Vimeo, https://vimeo.com/196875207 (accessed Sep. 25, 2023). 

## References
[1] Nanopublications, https://nanopub.net/ (accessed Sep. 25, 2023). 
[2] F. Giachelle, D. Dosso, and G. Silvello, “Search, access, and explore life science nanopublications on the web,” PeerJ. Computer science, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7959622/ (accessed Sep. 25, 2023). 
[3] Supplement 5: Semantic micro-contributions with decentralized ..., https://s11.no/2021/phd/nanopub/ (accessed Sep. 25, 2023). 
[4] Nanopublications, https://np.petapico.org/RAMc79WFgK30tHAeWj6PugKxfcqFsgErU2n8pLPJnwNrU (accessed Sep. 25, 2023). 

## Contributors
* Cogan Shimizu
* Skyler Gentner
