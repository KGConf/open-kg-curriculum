# What is a Taxonomy?
## Details
* Category: [Standards, Resources](../../categories/Standards,_Resources.md)
* Module Prerequisites: [RDF](../../modules/RDF.md)
* Audience: [Student](../../audiences/Student.md),[Developer](../../Developer.md)
* Level: [Beginner](../../levels/Beginner.md)

## Content
Taxonomy is the practice and science of categorization or classification [1]. The purpose of a taxonomy is for classification.

### Taxonomy and Hierarchy
A Taxonomy is a set of terms organized in a hierarchical fashion. Hierarchical relationships branch from general to increasingly specific nodes. Hierarchies are like trees which branch from a trunk to limbs with smaller branches that, in turn, may have even smaller branches. 

How do you know if a relationship is hierarchical? Heather Hedden, author of The Accidental Taxonomist, posits a guideline that uses the concepts *broader* and *narrower*:
>All members of a narrower concept’s category must be contained within the broader concept, but a broader concept is not limited to containing the members of a single narrower concept. Thus, only some members of a broader concept constitute the members of a given narrower concept. [2] 

Biologists recognize hierarchy within organisms. Carl Linnaeus pioneered the modern taxonomy of plants and animals; he defined seven layers of hierarchy to categorize a species such as ours [3]. 

Taxonomy systems, such as the Library of Congress Subject headings use "broader term" (BT) and "narrower term" (NT) to describe hierarchical relationships [4]. Human taxonomy consists of increasingly narrower terms. You can apply BT and NT to biological taxonomy.  

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
*  Are only *some* members of the broader concept members of the narrower concept? Some animals are human, some chordates are human, some mammals are human, some primates are human, etc. 
 
So this is hierarchical.

Nutritionists recognize hierarchy within food groups: meat, dairy, fruits and vegetables, grains, fat. There are different types of fruit including pome fruit (apples and pears) which includes dozens of varieties of apples [5]. 

W3C's Simple Knowledge Organization System (SKOS) uses ```skos:broader``` and ```skos:narrower``` to model hierarchical relations [6]. You can use SKOS to label increasingly narrow categories of fruit. 

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

Economists see hierarchy within industries. North American Industry Classification System (NAICS) defines sectors like manufacturing, construction, utilities, finance, entertainment, health care, education, and transportation. Each sector has subsectors and more-detailed subcategories. For example, NAICS breaks down the manufacturing sector hierarchically to include the parent subcategory food manufacturing which includes a more specific subcategory of animal food manufacturing which includes dog and cat food manufacturing [7]. 

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
This list is also hierarchical: All dog and cat food manufacturers are considered animal foor manufacturers, food manufacturers, and manufacturers. Only some manufacturers are food manufacturers, only some food manufacturers are manufacture food for animals. And only some animal food manufacturers specialize in dog and cat food. 

### Types of Hierarchy
The hierarchy may arise from subclass relations, such as that appear in RDF, or they may arise from e.g., 

According to the ANSI/NISO Z39.19-2005 standard (Section 8.3), there are three kinds of hierarchical relationships [8]: 

* Generic or generic–specific (Section 8.3.1)
* Instance (Section 8.3.2)
* Whole–part (8.3.3)

## Related Modules
* [SKOS](../SKOS/SKOS.md)
* [Class and Subclass](../Class_and_Subclass/Class_and_Subclass.md)
* 

## Related KGC Media
* Link to the Working Ontologist Videos?
* Link to the 

## References
[1] [https://en.wikipedia.org/wiki/Taxonomy](https://en.wikipedia.org/wiki/Taxonomy).

[2] Hedden, Heather. The Accidental Taxonomist, Third Edition (pp. 176-177). Information Today, Inc.. Kindle Edition.

[3] ([https://www.britannica.com/science/taxonomy/Classification-since-Linnaeus](https://www.britannica.com/science/taxonomy/The-Linnaean-system), accessed May 4, 2023

[4] Library of Congress Subject Headings PDF Files. https://www.loc.gov/aba/publications/FreeLCSH/freelcsh.html. 

[5] https://www.lacademie.com/different-types-of-apples/. Accessed May 2, 2023

[6] https://www.w3.org/TR/skos-primer/. SKOS Simple Knowledge Organization System Primer, 2.3.1 Broader/Narrower Relationships. Accessed May 4, 2023

[7] https://siccode.com/naics-code/311/food-manufacturing

[8] ANSI/NISO Z39.19-2005, Guidelines for the Construction, Format, and Management of Monolingual Controlled Vocabularies. https://www.niso.org/publications/ansiniso-z3919-2005-r2010. See also ISO 25964-1: 2011 thesaurus standard https://www.iso.org/standard/53657.html and Heather Hedden, The Accidental Taxonomist, Third Edition, Kindle (pp. 179-180). 

[3] Link to FOST
[4] Link to the working ontologist

## Contributors
* Cogan Shimizu
* Steve Gillespie
