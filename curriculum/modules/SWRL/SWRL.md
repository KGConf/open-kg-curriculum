# SWRL
## Details
* Category: [Standards](../categories/Standards.md)
* Module Prerequisites: [SPARQL](../modules/SPARQL.md)
* Audience: [Student, Developer](../audiences/Student,_Developer.md)
* Level: [Intermediate](../levels/Intermediate.md)

## Content


### What is SWRL ?

SWRL stands for Semantic Web Rule Language, a **rule-based language** proposed to combine structured world of ontologies and inferential capabilities of rule-based reasoning. It is a conjunction of [OWL 2 DL with a subset of RuleML](https://arxiv.org/pdf/1903.11723.pdf), applying rules of datalog/RuleML onto OWL ontologies. It acts more like a complement to the knowledge represented in ontologies for more expressive semantic reasoning.

### What was the need for SWRL ?

Even with various powerful data modelling and knowledge representation standards such as RDF, RDFS, OWL being present, some key aspects like expressivity, inference or automated reasoning, specifying complex logical rules lacked accessibility. While OWL is excellent for ontology modelling, representing taxonomies and establishing relationships, due to absence of rule-based approach, it cannot perform inference or specific decision-making logic based on conditions. As a result, SWRL ([a W3C Member Submission in May 2004](https://www.w3.org/submissions/SWRL/)) emerged to derive new knowledge or make logical deductions based on the existing RDF data & providing higher degree of expressiveness.

### SWRL Syntax

[SWRL](https://www.w3.org/submissions/SWRL/) rules are typically an implication between an antecedent (body) and consequent (head). This can be interpreted as: whenever the conditions specified in the antecedent hold, then the conditions specified in the consequent must also hold.

a human readable syntax rule has the form:

    antecedent (body) ⇒ consequent (head)

where both antecedent and consequent are conjunctions of atoms (assertions) which can contain a combination of OWL constructs, written a1 ∧ ... ∧ an. 
Variables are indicated using the standard convention of prefixing them with a question mark (e.g., ?x)

#### Example1:

    hasParent(?x,?y) ∧ hasBrother(?y,?z) ⇒ hasUncle(?x,?z)

For example, "If X has a parent of Y and Y has a brother of Z, then it infers that X has an uncle of Z."

### SWRL Semantics

The [constructs of atoms](https://protege.stanford.edu/conference/2009/slides/SWRL2009ProtegeConference.pdf) can either be in the form of OWL-DL class descriptions, individual-valued properties, data-valued properties, OWL same individuals, OWL different individuals, or the specific built-in functions.

        | C(i) | R(i, j) | D(v) | U(i,v) | builtIn(p, v1,…,vn) | i = j | i ≠ j |

C = Class;						
D = Data type;
R = Object Property;					
U = Data type Property;
i, j = Object variable names or Object individual names;
v1,…, vn = Data type variable names or Data type value names;
p = Built-in names

SWRL atoms in the antecedent (body) are satisfied,
* if it is empty (trivially true)
* or every atom of it is satisfied

SWRL atom in the consequent (head) is satisfied,
* if it is not empty
* and it is satisfied

A rule is satisfied by an interpretation of ‘I’ iff every binding B(I) that satisfies the antecedent B(I) satisfies the consequent

Using this syntax, a rule asserting that the composition of parent and brother properties implies the uncle property can be written as:

#### Example2: 

        person(?x) ∧ hasAge(?x, ?age) ∧ swrlb:greaterThan(?age, 18) → adult(?x)
        
In this example, if an individual (?x) is of the class - person and has property - Age greater than 18, they are inferred to be an - adult.

### SWRL is Monotonic:

* SWRL does not Support [Negated Atoms](https://protege.stanford.edu/conference/2009/slides/SWRL2009ProtegeConference.pdf)

#### Example3.1:

        Person(?x) ∧  not hasParent(?x, ?y) → ParentlessPerson(?x)

The above rule is Not possible because language negation is not supported, as there is a built-in function swrlb:not() for negation.
The correct way to negate is as follows:

#### Example3.2:

        Person(?x) ∧  swrlb:not(hasParent(?x, ?y)) -> ParentlessPerson(?x)

### SWRL - OWL syntactic sugar & not OWL syntactic sugar

#### OWL Syntactic Sugar

SWRL rules which are easy to relate to OWL axioms, as in, making use of OWL class expressions, object property expressions to formulate rules. They align with OWL 2 DL semantics and are easy to translate from SWRL rules to OWL axioms and class expressions.

#### Example4.1:

        Person(?p) ∧   hasParent(?p, ?parent) -> Parent(?parent)

#### Not OWL Syntactic Sugar

SWRL rules that use more built-in functions and variables which cannot be easily & directly translated to OWL axioms and class expressions are Not OWL Syntactic Sugar. They do not relate to standard OWL constructs.

#### Example4.2:

        
        swrlb:greaterThan(?age, 18)  ∧  hasLicense(?person, ?license) -> hasDrivingPrivileges(?person)
        
### SWRL reasoners

SWRL reasoners are software tools that can execute SWRL rules, perform rule-based reasoning, and make inferences based on the knowledge represented in RDF data. Pellet, Jena Rules, Protégé Reasoners Plugin are few such softwares.

[Protégé](../../modules/Protege/Protege.md) Reasoners Plugin:

The Protégé ontology editor provides a plugin system named SWRLTab to perform SWRL rules & reasoning on ontologies.

### SWRLTab

* Supports editing and execution of rules
* Extension mechanisms to work with third-party rule engines
* Mechanisms for users to define built-in method libraries
* Supports querying of ontologies

### SQWRL (pronounced as Squirrel)

SWRL is a rule language, not a query language and so, it cannot essentially retrieve data from ontologies. But using the rule bodies (antecedents) as query can result data much similar like SQL. Thus, the Semantic Query-Enhanced Web Rule Language ([SQWRL](https://protege.stanford.edu/conference/2009/slides/SWRL2009ProtegeConference.pdf)) is indeed useful. Few examples are:

#### Example5: 

        Person(?p) ∧  hasAge(?p,?age) ∧  swrlb:greaterThan(?age,17) → sqwrl:select(?p, ?age)
        Person(?p) ∧  hasCar(?p, ?c) → sqwrl:count(?c)

*	First query would result in – all the People with age greater than 17 in the given ontology
*	Second query would result in – No.of cars that are owned by people in the given ontology

All the examples serve as a proof to the higher expressive & inferential power of SWRL over OWL.

#### Implementation

#### Sample Ontology:

        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix owl: <http://www.w3.org/2002/07/owl#> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix ex: <http://example.com/ontology#> .

        ex:Student a owl:Class .
        ex:Course a owl:Class .
        ex:enrolledIn a owl:ObjectProperty .
        ex:hasAge a owl:DatatypeProperty .
        ex:isEnrolled a owl:DatatypeProperty .
        ex:notEnrolledIn a owl:ObjectProperty .

        ex:Student1 rdf:type ex:Student .
        ex:CourseA rdf:type ex:Course .
        ex:Student1 ex:enrolledIn ex:CourseA .
        ex:Student1 ex:hasAge "20"^^xsd:integer .
        ex:Student1 ex:isEnrolled "true"^^xsd:boolean .

        ex:Student2 rdf:type ex:Student .
        ex:CourseA rdf:type ex:Course .
        ex:Student2 ex:enrolledIn ex:CourseB .
        ex:Student2 ex:hasAge "22"^^xsd:integer .
        ex:Student2 ex:isEnrolled "true"^^xsd:boolean .

OWL can only succesfully represent knowledge, describe classes, properties and establish relationships, but to get insights from this data, we make use of Query Languages. And this is not designed to do automated reasoning. For which making use of SWRL rules onto ontologies gives new knowledge/data/inference.

#### Sample SWRL Rules onto the Ontology:

        ex:Student(Student1) ^ ex:hasAge(Student1, ?age) ^ swrlb:greaterThanOrEqual(?age, 18) -> ex:AdultStudent(Student1)

        ex:Student(Student2) ^ ex:enrolledIn(Student2, ?c) ^ ex:Course(?c) -> ex:EnrolledStudent(Student2)

Here, from the represented knowledge, SWRL was able to infer that the Students with age greater than or equal to 18 as Adult Students, which cannot be acheived through OWL alone. We can perform logical reasoning and infer new knowledge by using SWRL rules.

#### Applying Negation:

        ex:Student(Student2) ^ swrlb:not(enrolledIn(Student2, CourseA)) ^ ex:Course(CourseA) -> ex:notEnrolledIn(Student2)

This shows how SWRL can be used to make inferences based on negation, which allows us to deduce information about the absence of certain conditions in any given ontology. This is particularly useful in scenarios where reasoning about the presence or absence of specific data or conditions is cruicial.

#### Applying SQWRL:

        Student(?p) ∧  hasAge(?p,?age) ∧  swrlb:greaterThan(?age,17) → sqwrl:select(?p, ?age)

As powerful as SWRL is, we can also extract or retrieve data using SQWRL, this query will result in a list of students who meet the criteria as

| ?p            |
| :---          |
| Student1      |
| Student2      |

## Related KGC Media
* Workshop Example
* Tutorial Example

## External Media Reference
* [SWRL](https://www.w3.org/RDF/](https://youtu.be/DNBSCK2OeBU?si=ye5N1u3RFC_Fo_x5))

## References
[1] [W3C](https://www.w3.org/submissions/SWRL/) at W3C

[2] [The Semantic Web Rule Language Expressiveness Extensions-A Survey](https://arxiv.org/pdf/1903.11723.pdf)

[3] [The Semantic Web Rule Language](https://protege.stanford.edu/conference/2009/slides/SWRL2009ProtegeConference.pdf) 


## Contributors
* Chaitanya Anumula
* Cogan Shimizu
