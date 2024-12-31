# SHACL Curriculum

## Introduction to SHACL

### Overview

Shapes Constraint Language (SHACL) is a powerful language for validating RDF graphs against a set of conditions. These conditions are defined using shapes, which describe the structure that the data in the RDF graph should conform to. SHACL is particularly useful for ensuring data quality and consistency in knowledge graphs. This module will provide a comprehensive understanding of SHACL, its components, and how to use it effectively.

### Prerequisites

Before diving into SHACL, it is essential to have a solid understanding of RDF serializations. Familiarity with RDF, RDFS, and the various serialization formats such as RDF/XML, JSON-LD, and Turtle is assumed. This foundational knowledge will help in grasping the concepts and applications of SHACL more effectively.

## Understanding SHACL

### What is SHACL?

SHACL (Shapes Constraint Language) is a W3C recommendation designed to describe and validate RDF graphs. It allows you to define shapes that specify the expected structure of your RDF data. These shapes can then be used to validate the data, ensuring it conforms to the defined constraints. SHACL is particularly useful in scenarios where data integrity and consistency are critical.

### Key Components of SHACL

#### Shapes

Shapes are the core components of SHACL. They define the structure and constraints that the RDF data must adhere to. Shapes can be node shapes or property shapes:

- **Node Shapes**: These define constraints on RDF nodes (subjects or objects).
- **Property Shapes**: These define constraints on RDF properties (predicates).

#### Targets

Targets specify which nodes in the RDF graph a shape applies to. There are several ways to define targets:

- **Target Class**: All instances of a specific class.
- **Target Node**: A specific node.
- **Target Subjects Of**: All subjects of a specific property.
- **Target Objects Of**: All objects of a specific property.

#### Constraints

Constraints are the rules that the data must satisfy. SHACL provides a rich set of constraints, including:

- **Cardinality Constraints**: Specify the minimum, maximum, or exact number of values a property can have.
- **Datatype Constraints**: Specify the datatype of a property value.
- **Value Constraints**: Specify the allowed values for a property.
- **Pattern Constraints**: Specify that a property value must match a regular expression.
- **Class Constraints**: Specify that a node must be an instance of a specific class.

## Creating SHACL Shapes

### Defining Node Shapes

Node shapes are used to define constraints on RDF nodes. Here is an example of a node shape that specifies constraints on a `Person` class:

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <http://example.org/> .

ex:PersonShape a sh:NodeShape ;
    sh:targetClass ex:Person ;
    sh:property [
        sh:path ex:name ;
        sh:datatype xsd:string ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path ex:age ;
        sh:datatype xsd:integer ;
        sh:minInclusive 0 ;
    ] .
```

In this example:

- The shape `ex:PersonShape` targets all instances of the `ex:Person` class.
- It specifies that the `ex:name` property must be a string and must have at least one value.
- It specifies that the `ex:age` property must be an integer and must be non-negative.

### Defining Property Shapes

Property shapes are used to define constraints on RDF properties. Here is an example of a property shape that specifies constraints on the `ex:birthdate` property:

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <http://example.org/> .

ex:BirthdateShape a sh:PropertyShape ;
    sh:path ex:birthdate ;
    sh:datatype xsd:date ;
    sh:maxCount 1 .

```

In this example:

- The shape `ex:BirthdateShape` targets the `ex:birthdate` property.
- It specifies that the `ex:birthdate` property must be a date and can have at most one value.

## Validating RDF Data with SHACL

### Validation Process

The validation process involves checking the RDF data against the defined SHACL shapes. If the data does not conform to the shapes, validation reports are generated to highlight the issues. The validation process typically involves the following steps:

1. **Load the SHACL Shapes**: Load the SHACL shapes that define the constraints.
2. **Load the RDF Data**: Load the RDF data that needs to be validated.
3. **Perform Validation**: Use a SHACL validator to check the RDF data against the shapes.
4. **Generate Validation Report**: Produce a report that lists any violations of the constraints.

### Tools for SHACL Validation

Several tools are available for SHACL validation, including:

- **TopBraid SHACL**: A comprehensive tool for creating, editing, and validating SHACL shapes.
- **SHACL Playground**: An online tool for experimenting with SHACL shapes and validation.
- **SHACL API**: A Java API for programmatically working with SHACL shapes and validation.

## Advanced SHACL Features

### SHACL Functions

SHACL functions allow you to define custom constraints using SPARQL queries. This provides a powerful way to express complex constraints that are not covered by the built-in SHACL constraints. Here is an example of a SHACL function:

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <http://example.org/> .

ex:CustomShape a sh:NodeShape ;
    sh:targetClass ex:Person ;
    sh:sparql [
        sh:select """
            SELECT ?this
            WHERE {
                ?this ex:age ?age .
                FILTER (?age < 18)
            }
        """ ;
        sh:message "Age must be at least 18" ;
    ] .
```

In this example:

- The shape `ex:CustomShape` targets all instances of the `ex:Person` class.
- It uses a SPARQL query to check if the `ex:age` property is less than 18.
- If the condition is true, a validation message is generated.

### SHACL Rules

SHACL rules allow you to define inference rules that can be used to generate new RDF data based on existing data. This is useful for enriching the RDF graph with additional information. Here is an example of a SHACL rule:

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <http://example.org/> .

ex:AdultRule a sh:NodeShape ;
    sh:rule [
        sh:construct """
            CONSTRUCT {
                ?this a ex:Adult .
            }
            WHERE {
                ?this ex:age ?age .
                FILTER (?age >= 18)
            }
        """ ;
    ] .
```

In this example:

- The shape `ex:AdultRule` defines a rule that adds the `ex:Adult` class to all instances of the `ex:Person` class where the `ex:age` property is at least 18 and greater.

## Best Practices for Using SHACL

### Designing Effective Shapes

1. **Start Simple**: Begin with simple shapes and gradually add more complex constraints as needed.
2. **Use Descriptive Names**: Use clear and descriptive names for your shapes and properties to improve readability.
3. **Reuse Shapes**: Define reusable shapes that can be applied to multiple classes or properties.
4. **Document Your Shapes**: Provide documentation for your shapes to explain their purpose and constraints.

### Validating and Iterating

1. **Test Early and Often**: Validate your RDF data against your SHACL shapes early and often to catch issues quickly.
2. **Review Validation Reports**: Carefully review validation reports to understand and address any violations.
3. **Iterate on Shapes**: Continuously refine your SHACL shapes based on feedback and validation results.

## Conclusion

SHACL is a powerful tool for validating RDF graphs and ensuring data quality and consistency. By defining shapes that specify the expected structure of your data, you can catch and address issues early in the development process. Whether you are a student, developer, or practitioner, understanding and using SHACL can significantly enhance the reliability and integrity of your knowledge graphs.

## Exercises

1. **Create a Simple Node Shape**: Define a node shape that specifies constraints on a `Book` class, including properties for `title`, `author`, and `publicationDate`.
2. **Define a Property Shape**: Create a property shape that specifies constraints on the `ex:price` property, ensuring it is a positive decimal value.
3. **Validate RDF Data**: Use a SHACL validator to check a sample RDF graph against your defined shapes and generate a validation report.
4. **Implement a SHACL Function**: Write a SHACL function that checks if a `Book` has been published within the last year.
5. **Design a SHACL Rule**: Define a SHACL rule that adds a `BestSeller` class to all `Book` instances with a `sales` property greater than 1000.
