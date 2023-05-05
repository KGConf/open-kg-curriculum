# What is a Taxonomy?
## Details
* Category: [Standards, Resources](../../categories/Standards,_Resources.md)
* Module Prerequisites: [RDF](../../modules/RDF.md)
* Audience: [Student](../../audiences/Student.md),[Developer](../../Developer.md)
* Level: [Beginner](../../levels/Beginner.md)

## Content
Taxonomy is the practice and science of categorization or classification [1]. The purpose of a taxonomy is for classification. The term *taxonomy* draws on two Ancient Greek words: τάξις (taxis) meaning 'arrangement', and -νομία (-nomia) 'method'. The ideas may be ancient, but the first use of the term was *taxonomie*, a French word coined by a Swiss botanist in the early 1800s [2]. 

Taxonomy, as a method, focuses on arranging or organizing information hierarchically in parent/child, class/subclass, class/instance, or part/whole relationships. Hierarchical relationships are important in developing knowledge graphs, as discussed in the [Class and Subclass](../Class_and_Subclass/Class_and_Subclass.md) module. 

Taxonomies focus primarily on hierarchical relationships but recognize concepts can be related in other ways: as equivalent terms (synonyms, lexical variants) and as associated terms. s [3]. 

Writers use a thesaurus to find roughly equivalent terms. In fact, taxonomies can model equivalence relationships and so they are sometimes called a thesauri. Taxonomies are also sometimes called controlled vocabulary because they specify preferred and nonpreferred terms. For example the term *bird* might be preferrred to *Aves*. In that case, when citing Aves, you would point to bird as the preferred term (Aves USE bird); or when citing bird, you can point to Aves as a nonpreferred term (bird USE FOR Aves). Similarly, Simple Knowledge Organization System (SKOS) uses labels to designate preferred terms (```skos:prefLabel```), alternative terms (```skos:altLabel```), and even mis-spelled terms (```skos:hiddenLabel```)[4].  

How do taxonomies handle associated terms? For example, the term *biologist* is clearly associated with *biology* (as practitioner/discipline); *writer* is associated with *publication* (creator/creation). Taxonomies model associated terms at a high level, by simply calling them related terms (RT). Knowledge graphs and ontologies model different types of relationships as properties, the edges between nodes.  

### Taxonomy and Hierarchy
A Taxonomy is primarily a set of terms organized in a hierarchical fashion, branching like trees from general to increasingly specific nodes. Trees typically branch from a trunk to limbs with smaller branches that, in turn, have even smaller branches. 

How do you know if a relationship is hierarchical? Heather Hedden, author of The Accidental Taxonomist, posits a guideline that uses the concepts *broader* and *narrower*:
>All members of a narrower concept’s category must be contained within the broader concept, but ... only some members of a broader concept constitute the members of a given narrower concept. [4] 

Think of it as the *all/some* rule for hierarchical relationships. We will apply this rule was we look at some examples.

**Hierarchy in Biology.** Biologists recognize hierarchy within organisms. Carl Linnaeus pioneered the modern taxonomy of plants and animals; in 1735 he defined seven layers of hierarchy to categorize species such as ours [5]. 

Taxonomy systems, such as the Library of Congress Subject Headings use "broader term" (BT) and "narrower term" (NT) to describe hierarchical relationships [6]. The categories Human taxonomy consists of increasingly narrower terms. You can apply BT and NT to biological taxonomy.  

```
Kingdom - Animalia
 |
  NT: Phylum - Chordata
  |
   NT: Class - Mammalia
   | 
    NT: Order - Primates
    |
      NT: Family - Hominidae
      |
       NT: Genus - Homo
       |
        NT: Species - Sapiens
```
Is this hierarchical? 
* Are *all* members of the narrower concept also members of the broader concept? All homo sapiens are hominidae, primates, mammals, chordates, and animals. OK, so far.
*  Are only *some* members of the broader concept members of the narrower concept? Some (not all!) animals are human, some chordates are human, some mammals are human, some primates are human, etc. 
 
So these categories are hierarchical.

**Hierarchy in Food.** Nutritionists recognize hierarchy within food groups: meat, dairy, fruits and vegetables, grains, fat. There are different types of fruit including pome fruit (apples and pears) which includes dozens of varieties of apples [7]. 

W3C's Simple Knowledge Organization System (SKOS) uses ```skos:broader``` and ```skos:narrower``` to model hierarchical relations [8]. You can use SKOS to label increasingly narrow categories of fruit. 

```
Fruit
 |
  skos:narrower Pome fruit
  |
   skos:narrower Apples
   | 
    skos:narrower Jonathan Apples
```
Is this hierarchical? All Jonathan Apples are apples, pome fruit, and fruit. Some fruit, some pome fruit, and some apples are Jonathan apples. So this list is hierarchical.

**Hierarchy in Industry.** Economists see hierarchy within industries. North American Industry Classification System (NAICS) defines sectors like manufacturing, construction, utilities, finance, entertainment, health care, education, and transportation. Each sector has subsectors and more-detailed subcategories. For example, NAICS breaks down the manufacturing sector hierarchically to include the parent subcategory food manufacturing which includes a more specific subcategory of animal food manufacturing which includes dog and cat food manufacturing [9]. 

Since ```skos:broader``` and ```skos:narrower``` are the inverse of each other; you can represent this manufacturing example from narrower to broader concepts.
```
    Dog and cat food manufacturing
    | 
   skos:broader: Animal food manufacturing
  |
  skos:broader: Food manufacturing
 | 
skos:broader: Manufacturing

```
This list is also hierarchical: All dog and cat food manufacturers are considered animal food manufacturers, food manufacturers, and manufacturers. Only some manufacturers are food manufacturers, only some food manufacturers are manufacture food for animals. And only some animal food manufacturers specialize in dog and cat food. 

### Types of Hierarchy
The hierarchy may arise from subclass relations, such as that appear in RDF, or they may arise from e.g., 

According to the ANSI/NISO Z39.19-2005 standard (Section 8.3), there are three kinds of hierarchical relationships [10]: 

* Generic or generic–specific (Section 8.3.1)
* Instance (Section 8.3.2)
* Whole–part (8.3.3)

Example data from the 2023 knowledge graph Conference illustrate each type: 

Generic relationships identify a link between a class and members or subclasses. In this case, KGC has several types of events within a conference.   
```
Event Type
    NT Keynote
    NT Workshop
    NT Tutorial
    NT Masterclass
```
Instance relationships link a class and instances of that class typically expressed as proper nouns. In this case, speakers is a common noun and the instances are speaker names.
```
Speakers  
    NT Pete Rivett
    NT Leia Dickerson
    NT Deborah McGuinness
    NT Heather Hedden
```
Whole-part relationships link an object with its parts or components. In this case, a speaker profile includes narrower terms as integral parts of the speaker profile. 
```
Speaker Profile  
    NT Speaker Name
    NT Speaker Picture
    NT Speaker Biography
    NT Speaker LinkedIn Profile
    NT Speaker Company
    NT Speaker Position 
```
## Related Modules
* [SKOS](../SKOS/SKOS.md)
* [Class and Subclass](../Class_and_Subclass/Class_and_Subclass.md)

## Related KGC Media
* Link to the Working Ontologist Videos?
* Link to the Heather Hedden's KGC Bookclub, Spring 2023, The Accidental Taxonomist

## References
[1] [https://en.wikipedia.org/wiki/Taxonomy](https://en.wikipedia.org/wiki/Taxonomy).

[2] Hedden, Heather. The Accidental Taxonomist, Third Edition (p. 33). Information Today, Inc.. Kindle Edition.

[3] Section 8 Relationships in ANSI/NISO Z39.19-2005 (R2010 describes hierarchical, equivalent, and associated relationships. https://www.niso.org/publications/ansiniso-z3919-2005-r2010

[4] Simple Knowledge Organization System Reference, Section 5.2 Vocabulary. https://www.w3.org/TR/skos-reference/#labels

[4] Hedden, Heather. The Accidental Taxonomist, Third Edition (pp. 176-177). Information Today, Inc.. Kindle Edition.

[5] ([https://www.britannica.com/science/taxonomy/Classification-since-Linnaeus](https://www.britannica.com/science/taxonomy/The-Linnaean-system), accessed May 4, 2023

[6] Library of Congress Subject Headings PDF Files. https://www.loc.gov/aba/publications/FreeLCSH/freelcsh.html. 

[7] https://www.lacademie.com/different-types-of-apples/. Accessed May 2, 2023

[8] https://www.w3.org/TR/skos-primer/. SKOS Simple Knowledge Organization System Primer, 2.3.1 Broader/Narrower Relationships. Accessed May 4, 2023

[9] https://siccode.com/naics-code/311/food-manufacturing

[10] ANSI/NISO Z39.19-2005, Guidelines for the Construction, Format, and Management of Monolingual Controlled Vocabularies. https://www.niso.org/publications/ansiniso-z3919-2005-r2010. See also ISO 25964-1: 2011 thesaurus standard https://www.iso.org/standard/53657.html and Heather Hedden, The Accidental Taxonomist, Third Edition, Kindle (pp. 179-180). 

[3] Link to FOST
[4] Link to the working ontologist

## Contributors
* Cogan Shimizu
* Steve Gillespie
