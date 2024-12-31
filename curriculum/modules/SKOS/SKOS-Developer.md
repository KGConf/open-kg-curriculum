# SKOS Curriculum

## Module Overview

**Module Name:** SKOS (Simple Knowledge Organization System)

**Category:** Standards, Resources

**Prerequisites:** RDF (Resource Description Framework)

**Audience:** Developer

**Level:** Intermediate

**Covered Concepts:** This module will cover the fundamental concepts of SKOS, including its vocabulary, structure, and applications in knowledge organization.

## Introduction to SKOS

### What is SKOS?

SKOS (Simple Knowledge Organization System) is a W3C recommendation designed for representing knowledge organization systems such as thesauri, classification schemes, taxonomies, and subject heading systems using the Resource Description Framework (RDF). SKOS provides a standard way to represent concepts, their relationships, and labels in a structured and machine-readable format.

### Importance of SKOS

SKOS plays a crucial role in the Semantic Web by enabling interoperability between different knowledge organization systems. It allows for the integration of diverse vocabularies and facilitates the sharing and reuse of knowledge across different applications and domains. SKOS is particularly useful for developers who need to create, manage, and integrate controlled vocabularies and taxonomies in their applications.

## SKOS Vocabulary

### Core Concepts

#### skos:Concept

The `skos:Concept` class is the fundamental building block of SKOS. It represents a unit of thought or meaning, which can be identified by a URI. Concepts are the primary entities in a SKOS vocabulary and are used to describe the meaning of terms within a knowledge organization system.

#### skos:ConceptScheme

The `skos:ConceptScheme` class represents a set of concepts, typically organized in a hierarchical or associative structure. A concept scheme can be thought of as a container for concepts and provides a way to group related concepts together.

#### skos:broader and skos:narrower

The `skos:broader` and `skos:narrower` properties are used to define hierarchical relationships between concepts. The `skos:broader` property indicates that a concept is more general than another concept, while the `skos:narrower` property indicates that a concept is more specific.

#### skos:related

The `skos:related` property is used to define associative relationships between concepts. It indicates that two concepts are related in some way, but not in a hierarchical manner.

### Labeling Properties

#### skos:prefLabel

The `skos:prefLabel` property is used to assign a preferred label to a concept. The preferred label is the primary term used to refer to the concept and is typically the most commonly used term.

#### skos:altLabel

The `skos:altLabel` property is used to assign alternative labels to a concept. Alternative labels are synonyms or other terms that can be used to refer to the concept, but are not the primary term.

#### skos:hiddenLabel

The `skos:hiddenLabel` property is used to assign labels to a concept that should not be displayed to end-users. Hidden labels are typically used for indexing or search purposes.

### Documentation Properties

#### skos:definition

The `skos:definition` property is used to provide a textual definition of a concept. The definition should be a clear and concise description of the concept's meaning.

#### skos:scopeNote

The `skos:scopeNote` property is used to provide additional information about the scope or context in which a concept is used. Scope notes can include examples, usage guidelines, or other relevant information.

#### skos:example

The `skos:example` property is used to provide examples of how a concept is used. Examples can help clarify the meaning of a concept and illustrate its application in practice.

### Mapping Properties

#### skos:exactMatch

The `skos:exactMatch` property is used to indicate that two concepts from different concept schemes have the same meaning and can be used interchangeably.

#### skos:closeMatch

The `skos:closeMatch` property is used to indicate that two concepts from different concept schemes have similar meanings, but are not identical. Close matches are useful for identifying concepts that are closely related but not exact equivalents.

#### skos:broadMatch

The `skos:broadMatch` property is used to indicate that a concept from one concept scheme has a broader meaning than a concept from another concept scheme.

#### skos:narrowMatch

The `skos:narrowMatch` property is used to indicate that a concept from one concept scheme has a narrower meaning than a concept from another concept scheme.

#### skos:relatedMatch

The `skos:relatedMatch` property is used to indicate that two concepts from different concept schemes are related in some way, but not in a hierarchical manner.

## Creating a SKOS Vocabulary

### Defining Concepts

To create a SKOS vocabulary, you first need to define the concepts that will be included in the vocabulary. Each concept should be assigned a unique URI and labeled using the `skos:prefLabel` property. Additional labels can be assigned using the `skos:altLabel` and `skos:hiddenLabel` properties.

### Organizing Concepts

Once the concepts have been defined, they need to be organized into a hierarchical or associative structure. Hierarchical relationships can be defined using the `skos:broader` and `skos:narrower` properties, while associative relationships can be defined using the `skos:related` property.

### Documenting Concepts

Documenting concepts is an essential part of creating a SKOS vocabulary. Each concept should be documented using the `skos:definition`, `skos:scopeNote`, and `skos:example` properties. Documentation helps ensure that the meaning of each concept is clear and unambiguous.

### Mapping Concepts

Mapping concepts between different concept schemes is an important aspect of creating a SKOS vocabulary. Mapping properties such as `skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, and `skos:relatedMatch` can be used to establish relationships between concepts from different concept schemes.

## Advanced SKOS Topics

### SKOS Extensions

SKOS can be extended to include additional properties and classes that are not part of the core SKOS vocabulary. Extensions can be used to represent more complex relationships between concepts or to include additional metadata about concepts.

### SKOS and OWL

SKOS can be used in conjunction with OWL (Web Ontology Language) to create more expressive knowledge organization systems. OWL can be used to define additional constraints and relationships between concepts, while SKOS can be used to represent the basic structure and labeling of the concepts.

### SKOS and RDFS

SKOS is built on top of RDFS (RDF Schema), which provides a basic vocabulary for describing the structure of RDF data. RDFS properties such as `rdfs:label`, `rdfs:comment`, and `rdfs:seeAlso` can be used in conjunction with SKOS properties to provide additional metadata about concepts.

## Practical Applications of SKOS

### Thesaurus Management

SKOS is commonly used for managing thesauri, which are controlled vocabularies used for indexing and retrieving information. Thesauri can be represented using SKOS to enable interoperability between different thesauri and to facilitate the sharing and reuse of thesaurus data.

### Taxonomy Development

Taxonomies are hierarchical classifications of concepts used for organizing and categorizing information. SKOS can be used to represent taxonomies and to define the hierarchical relationships between concepts within a taxonomy.

### Subject Headings

Subject headings are controlled vocabularies used for describing the topics of documents or other resources. SKOS can be used to represent subject headings and to define the relationships between subject headings within a subject heading system.

### Classification Schemes

Classification schemes are systems used for organizing and categorizing information based on predefined criteria. SKOS can be used to represent classification schemes and to define the relationships between classes within a classification scheme.

## Conclusion

SKOS is a powerful and flexible standard for representing knowledge organization systems using RDF. It provides a comprehensive vocabulary for defining concepts, their relationships, and labels, as well as for documenting and mapping concepts between different concept schemes. By understanding and applying SKOS, developers can create interoperable and reusable knowledge organization systems that facilitate the sharing and integration of knowledge across different applications and domains.