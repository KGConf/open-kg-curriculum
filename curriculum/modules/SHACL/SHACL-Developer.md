# SHACL Curriculum for Developers

## Overview

This module introduces SHACL, a language for validating RDF graphs. It is designed for developers who need to ensure the quality and consistency of their RDF data. The curriculum covers the fundamentals of SHACL, its syntax, and practical applications. By the end of this module, you will have a comprehensive understanding of SHACL and be able to implement it in your projects.

## Prerequisites

Before starting this module, you should have a solid understanding of RDF serializations, including RDF/XML, JSON-LD, and Turtle. Familiarity with RDFS and basic knowledge of SPARQL is also beneficial.

## Learning Outcomes

By the end of this module, you will be able to:

- Understand the purpose and benefits of SHACL.
- Write SHACL shapes to validate RDF graphs.
- Implement SHACL validation in your applications.
- Troubleshoot common issues in SHACL validation.

## Introduction

### What is SHACL?

SHACL (Shapes Constraint Language) is a W3C recommendation for validating RDF graphs. It allows developers to define constraints on RDF data, ensuring that the data conforms to specific requirements. SHACL is particularly useful for ensuring data quality, consistency, and interoperability.

### Why Use SHACL?

- **Data Quality**: Ensures that RDF data meets specific criteria, reducing errors and inconsistencies.
- **Interoperability**: Enables data exchange between different systems by ensuring that data conforms to agreed-upon standards.
- **Flexibility**: Allows for complex validation rules, including conditional constraints and data transformations.

## Syntax

### Basic Concepts

SHACL is built on the concept of "shapes," which define the structure and constraints of RDF data. A shape can be thought of as a template for RDF nodes, specifying the types of properties and values that are allowed.

### Defining Shapes

A shape is defined using the `sh:Shape` class. The following example defines a simple shape for a `Person`:

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <http://example.org/> .

ex:PersonShape a sh:Shape ;
  sh:targetClass ex:Person ;
  sh:property ex:PersonNameShape .

ex:PersonNameShape a sh:PropertyShape ;
  sh:path ex:name ;
  sh:datatype xsd:string .
```

### Property Shapes

Property shapes define constraints on the properties of a node. They can be nested within a shape or defined as standalone shapes.

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <http://example.org/> .

ex:PersonNameShape a sh:PropertyShape ;
  sh:path ex:name ;
  sh:datatype xsd:string ;
  sh:minLength 1 ;
  sh:maxLength 50 .
```

### Cardinality Constraints

SHACL allows for specifying cardinality constraints, such as the minimum and maximum number of occurrences of a property.

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <http://example.org/> .

ex:PersonEmailShape a sh:PropertyShape ;
  sh:path ex:email ;
  sh:datatype xsd:string ;
  sh:minCount 1 ;
  sh:maxCount 3 .
```

## Advanced Features

### Conditional Constraints

SHACL supports conditional constraints, allowing for more complex validation rules. For example, you can define a constraint that only applies if a certain condition is met.

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <http://example.org/> .

ex:PersonAgeShape a sh:PropertyShape ;
  sh:path ex:age ;
  sh:datatype xsd:integer ;
  sh:minInclusive 18 ;
  sh:condition [
    sh:property ex:hasDriverLicense ;
    sh:hasValue true ;
  ] .
```

### Data Transformations

SHACL can also be used to transform data, allowing you to derive new properties or values from existing data.

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <http://example.org/> .

ex:PersonFullNameShape a sh:PropertyShape ;
  sh:path ex:fullName ;
  sh:message "Full name should be in the format 'First Last'." ;
  sh:sparql [
    sh:prefixes ex: ;
    sh:select """
      SELECT ?this (STR(?first) || ' ' || STR(?last) AS ?fullName)
      WHERE {
        ?this ex:firstName ?first ;
              ex:lastName ?last .
      }
    """ ;
  ] .
```

## Implementation

### Tools and Libraries

Several tools and libraries are available for implementing SHACL validation. Some popular options include:

- **Apache Jena**: A Java framework for building Semantic Web and Linked Data applications.
- **TopBraid SHACL**: A commercial tool for SHACL validation and data modeling.
- **PySHACL**: A Python library for SHACL validation.

### Integration with Applications

To integrate SHACL validation into your applications, you can use the following steps:

1. **Define SHACL Shapes**: Write SHACL shapes to define the constraints on your RDF data.
2. **Load SHACL Shapes**: Load the SHACL shapes into your application using a SHACL processor.
3. **Validate RDF Data**: Validate your RDF data against the SHACL shapes.
4. **Handle Validation Results**: Handle the validation results, such as displaying errors or correcting data.

### Example: Validating RDF Data with PySHACL

```python
from pyshacl import validate

# Define SHACL shapes
shapes = """
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <http://example.org/> .

ex:PersonShape a sh:Shape ;
  sh:targetClass ex:Person ;
  sh:property ex:PersonNameShape .

ex:PersonNameShape a sh:PropertyShape ;
  sh:path ex:name ;
  sh:datatype xsd:string ;
  sh:minLength 1 ;
  sh:maxLength 50 .
"""

# Define RDF data
data = """
@prefix ex: <http://example.org/> .

ex:Person1 a ex:Person ;
  ex:name "John Doe" .

ex:Person2 a ex:Person ;
  ex:name "Jane" .
"""

# Validate RDF data
conforms, results_graph, results_text = validate(data, shacl_graph=shapes)

# Print validation results
print("Conforms: ", conforms)
print("Results Text: ", results_text)
```

## Troubleshooting

### Common Issues

- **Syntax Errors**: Ensure that your SHACL shapes are syntactically correct.
- **Targeting Issues**: Make sure that your shapes are targeting the correct classes or properties.
- **Data Type Mismatches**: Verify that the data types in your RDF data match the expected data types in your SHACL shapes.

### Debugging Tips

- **Use SHACL Validators**: Use online SHACL validators to test your shapes and RDF data.
- **Check Logs**: Review the logs generated by your SHACL processor for detailed error messages.
- **Simplify Shapes**: Start with simple shapes and gradually add complexity to isolate and identify issues.

## Conclusion

SHACL is a powerful tool for validating RDF data, ensuring data quality, consistency, and interoperability. By understanding SHACL's syntax and advanced features, you can implement robust validation in your applications. With the knowledge gained in this module, you are well-equipped to define and enforce constraints on RDF data, enhancing the reliability and usability of your knowledge graphs.

## Assessment

### Quiz

1. What is SHACL, and why is it important for validating RDF data?
2. How do you define a shape in SHACL?
3. What are property shapes, and how are they used in SHACL?
4. Explain how to implement SHACL validation in your applications.
5. What are some common issues and debugging tips for SHACL validation?

### Practical Exercise

1. Write a SHACL shape to validate a `Person` with properties `name` and `age`.
2. Use a SHACL processor to validate a sample RDF graph against your shape.
3. Implement SHACL validation in a small application using a tool or library of your choice.
