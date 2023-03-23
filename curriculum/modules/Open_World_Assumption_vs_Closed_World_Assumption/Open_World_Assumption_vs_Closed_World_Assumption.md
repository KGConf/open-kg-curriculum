# Open World Assumption vs Closed World Assumption
## Details
* Category: [Methods](../categories/Methods.md)
* Module Prerequisites: [Introduction to Logic](../modules/Introduction_to_Logic.md)
* Audience: [Any](../audiences/Any.md)
* Level: [Beginner](../levels/Beginner.md)

## Content

### Closed Word Assumption 
When it comes to answering questions and being able to understand natural processing tasks with detail, knowledge graphs are key, to be more specific, trust-worthy knowledge graphs. But what makes a knowledge graph trustable and how can we evaluate it as such?<br>
Knowledge graph embedding is the action of taking latest information of entities and relations and using them for future predictions. Therefore, the knowledge graph can get evaluated on it's reliability by using a "Closed World Assumption" - assuming that any triples not present in the graph are false. In more common language, something that is present/known to be true is true, but something that is not known to be true is false. [3]<br>
In the case of checking if a knowledge graph's predictions are true, a link prediction task can be perfomed : Given a test triple (h, r, t), we hold out one of its entities or its relation to form a query (h, r, ?), (?, r, t), or (h, ?, t). The model then scores all tail entities ti ∈ E, head entities hi ∈ E, or relations ri ∈ R as answers to the respective query such that higher-ranked completions (h, r, ti), (hi, r, t), or (h, ri, t) are more plausible. Prior to computing rankings, all true triples across train, validation, and test beyond the given test triple are filtered out. [3]
Under this assumption, models are being analyzed by scoring the true test triples (h, r, t) as high as possible since any triple not present is considered not correct.[4]<br>
Recent works have showed a gap between the "Open World Assumption " vs the "Closed World Assumption". This work reveals that the Closed World Assumption is of much importance when evaluating a knowledge graph while Open World Assumption models mostly fail to locate false information.[5]<br>
We could call Closed World Assumption a simple formalization of default reasoning since the negative parts of a domain can be greater than the positive parts.This can be used in database applications such as airline reservations or library lending databases that keep track of things that exist instead of things that do not.[6] & [7]


### Open World Assumption
The open world assumption is the assumption that a statement not directly stated to be true is not necessarily false. The statement is not assumed to be true, but it is allowed to exist in an unknown state [7]. This is useful when representing real-world systems in which we are trying to discover information, or when we know that information will be added that we cannot account for at the beginning. It acknowledges and reflects that no one person or group is capable of knowing everything.

Open world assumption is used in Semantic Web languages as the point of the Semantic Web is to discover new information [7]. If a knowledge graph states that a person is a man, and the man has brown hair and peach skin, then using the open world assumption we do not assume that the person does not have eyes simply because his eye color was not added to the graph. If this is the case, it would need to be directly stated. Similarly, we do not make the assumption that just because we have a list of traits about a place, that we know everything about it. Just because we do not see worms crawling in the grass doesn’t mean they aren’t in the soil. This assumption is the default logic used by most humans. People generally do not assume that something is false in a complete vacuum of knowledge.

### Partial Closed World Assumption
In the event that a fact must be represented as false, but while still generally using open world assumption, the partial closed-world assumption can be used. Partial closed-world assumption is when statements are represented as either open world assumption or closed world assumption based on what is more useful, within the same system [8]. In the real world we can assume that a cat has fur even if it has not been explicitly stated to be true, even though not all cats have fur. Because it is far more likely that a cat has fur than that it does not have fur, it makes more intuitive sense to represent this using the open world assumption. However, we also logically assume that a cat will not have green fur, even if it is not expressly stated to be false. This mix in how we make assumptions is an example of how humans generally use the partial closed-world assumption.


### Comparison    
One of the key benefits of using an Open World Assumption (OWA) is that the process of making an ontology based upon the Open World Assumption (OWA) is what could be called a process of elimination.<br> 
The ontology would be empty at the start and become more restricted and narrow by stating what is not possible. Thus, there exists the possibility of adding further individuals if it is not explicitly excluded [1]. 
This would be the better type of assumption to use in the case where one does not or can not know everything.<br>         
In comparison, the use of a Closed World Assumption (CWA) creates an ontology through the process of inclusion of knowledge and individuals.<br> 
The ontology would be assumed to contain all known individuals and facts. Thus, a new individual that was not explicitly included before is assumed to not exist and any other "facts" are assumed to be false.<br>    
Another way to phrase this would be to say that in the Closed World Assumption (CWA) the only true statements are the statements directly given in the database and those statements implied by the database and that everything else is assumed to be false [2].<br> 
One of the issues that is seen in the Open World Assumption (OWA) that can be fixed by using the Closed World Assumption (CWA) is a "lack of definitive answers" which causes uncertainty with queries needing a Boolean answer. An example of a field with "queries which require a definite yes/no answer" is that of robotics. Since robots are not well skilled in processing incomplete or ambiguous information and data they tend to prefer the Closed World Assumption (CWA) [1].<br>
Another problem with the Open World Assumption (OWA) occurs "when handling incomplete service descriptions" for the matchmaking process [1].<br>   
However, it is possible to simulate some behavior of the Closed World Assumption (CWA) in an Open World Assumption (OWA) based ontology. One way that this could be done is to explicitly state that two classes are disjoint. Meaning that the intersection of the two classes is an empty class. Thus, excluding all individuals that would have an is-a relation to both classes from the ontology and requiring that all included individuals have an is-a relation with exactly one or neither of the classes.<br>
Another way to make a similar simulated behavior would be with the negation of statements. Such as "isFriendOf" and the negation would be "isNotFriendOf" to allow the explicit statement that one person does not consider the other to be their friend.<br> 
An example of when the use of the Open World Assumption (OWA) with explicit negative data is preferred in a database is within the medical field. If a doctor is checking the database to see if the patient has diabetes, then it would be better to get an "answer generated by the
system using definite information" rather than the negative answer determined by a system using the Closed World Assumption (CWA) [2].

## Related KGC Media
* Workshop Example
* Tutorial Example

## External Media References
[3.9 DLs and the Open World Assumption](https://www.youtube.com/watch?v=QnxevuT4tQw)

## References 
[1] A. Elçi, B. Rahnama and S. Kamran, "Defining a Strategy to Select Either of Closed/Open World Assumptions on Semantic Robots," 2008 32nd Annual IEEE International Computer Software and Applications Conference, Turku, Finland, 2008, pp. 417-423, doi: 10.1109/COMPSAC.2008.182.<br>
[2] N. Viswanath and R. Sunderraman, "Handling disjunctions in open world relational databases," NAFIPS 2008 - 2008 Annual Meeting of the North American Fuzzy Information Processing Society, New York, NY, USA, 2008, pp. 1-6, doi: 10.1109/NAFIPS.2008.4531248.<br>
[3] T. Safavi, D. Koutra, and E. Meij, “Evaluating the calibration of knowledge graph embeddings for trustworthy link prediction,” Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2020. <br>
[4] “Translating embeddings for modeling multi-relational data - neurips.” [Online]. Available: https://proceedings.neurips.cc/paper/2013/file/1cecc7a77928ca8133fa24680a88d2f9-Paper.pdf<br>
[5]H. Yang, Z. Lin, and M. Zhang, “Rethinking knowledge graph evaluation under the open-world assumption,” arXiv.org, 19-Sep-2022.<br>
[6]“Closed world reasoning - tau.” [Online]. Available: https://www.cs.tau.ac.il/~annaz/teaching/TAU_winter08/Seminar/yulia.pdf. <br>
[7]J. Sequeda, “Introduction to: Open world assumption vs closed world assumption,” DATAVERSITY, 10-Jan-2015. [Online]. Available: https://www.dataversity.net/introduction-to-open-world-assumption-vs-closed-world-assumption/
[8] S. Razniewski, O. Savkovi and W. Nutt, “Turning The Partial-closed World Assumption
Upside Down,” Free University of Bozen-Bolzano. [Online]. Available: https://ceur-ws.org/Vol-1644/paper3.pdf

## Contributors
* Antrea Christou
* Erin Rogers
* Cogan Shimizu
* Sydney Woods
