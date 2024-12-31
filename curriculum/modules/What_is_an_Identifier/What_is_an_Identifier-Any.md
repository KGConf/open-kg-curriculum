# Curriculum: What is an Identifier?

## Module Overview

This module introduces the fundamental concepts of identifiers, focusing on URIs, hash or slash conventions, and namespaces. By the end of this module, students will understand the role of identifiers in knowledge graphs, their structure, and best practices for their use.

## Target Audience

- **Any**: This module is designed to be accessible to anyone interested in understanding identifiers, regardless of their background.

## Learning Outcomes

By the end of this module, students will be able to:

1. Explain what a URI is and its significance in identifying resources.
2. Understand the differences between hash and slash URIs.
3. Describe what a namespace is and how it is used in the context of identifiers.
4. Apply best practices for creating and using identifiers in knowledge graphs.

## Content

### 1. Introduction to Identifiers

Identifiers play a crucial role in knowledge graphs by providing a unique way to reference resources. They ensure that resources can be unambiguously identified and accessed, facilitating data integration and interoperability.

### 2. Understanding URIs

#### 2.1 Definition and Structure

A Uniform Resource Identifier (URI) is a string of characters used to identify or name a resource on the internet. URIs are fundamental to the web and are used to locate and access resources such as web pages, images, and services.

A URI is composed of several components:

- **Scheme**: Specifies the protocol used to access the resource (e.g., `http`, `https`, `ftp`).
- **Authority**: Includes the domain name and optional port number (e.g., `www.example.com:80`).
- **Path**: The specific location of the resource on the server (e.g., `/path/to/resource`).
- **Query**: Optional parameters passed to the resource (e.g., `?key=value`).
- **Fragment**: A reference to a specific part of the resource (e.g., `#section`).

Example:
```
https://www.example.com:80/path/to/resource?key=value#section
```

#### 2.2 Types of URIs

URIs can be classified into two main types:

- **URL (Uniform Resource Locator)**: A type of URI that specifies the location of a resource and how to retrieve it.
- **URN (Uniform Resource Name)**: A type of URI that provides a persistent, location-independent name for a resource.

#### 2.3 URIs in Knowledge Graphs

In knowledge graphs, URIs are used to identify entities, properties, and classes. They ensure that each resource is uniquely identifiable, enabling data integration and querying across different datasets.

### 3. Hash vs. Slash URIs

#### 3.1 Hash URIs

Hash URIs use the fragment identifier (`#`) to specify a particular part of a resource. They are often used to identify specific sections within a document.

Example:
```
http://example.com/document#section1
```

**Advantages**:
- **Simplicity**: Easy to create and understand.
- **Hierarchy**: Allows for a hierarchical structure within a single document.

**Disadvantages**:
- **Limited Scope**: Fragments are not sent to the server, limiting their use in certain scenarios.

#### 3.2 Slash URIs

Slash URIs use the path component (`/`) to specify the location of a resource. They are commonly used to identify resources that are separate from the main document.

Example:
```
http://example.com/resource/section1
```

**Advantages**:
- **Server-Side Processing**: The entire URI is sent to the server, allowing for server-side processing and redirection.
- **Flexibility**: Can be used to identify a wide range of resources, not limited to sections within a document.

**Disadvantages**:
- **Complexity**: May require more complex server-side logic to handle.

#### 3.3 Choosing Between Hash and Slash URIs

The choice between hash and slash URIs depends on the specific use case and requirements:

- Use **hash URIs** when you need to identify sections within a single document and do not require server-side processing.
- Use **slash URIs** when you need to identify separate resources and require server-side processing or redirection.

### 4. Namespaces

#### 4.1 Definition and Purpose

A namespace is a container for a set of identifiers, providing a way to group related resources and avoid naming conflicts. Namespaces are essential in knowledge graphs for organizing and managing identifiers.

#### 4.2 Using Namespaces

Namespaces are typically defined using a base URI, which serves as a prefix for all identifiers within that namespace. This ensures that each identifier is unique and can be unambiguously referenced.

Example:
```
http://example.com/namespace/resource1
http://example.com/namespace/resource2
```

#### 4.3 Best Practices for Namespaces

- **Consistency**: Use a consistent naming convention for namespaces to ensure clarity and avoid confusion.
- **Descriptive**: Choose descriptive names for namespaces that reflect their purpose and content.
- **Persistence**: Ensure that namespaces are persistent and do not change over time, as this can break references to resources.

### 5. Best Practices for Identifiers

#### 5.1 Uniqueness

Ensure that each identifier is unique within its namespace to avoid conflicts and ensure accurate referencing.

#### 5.2 Persistence

Identifiers should be persistent and not change over time. This ensures that references to resources remain valid and accessible.

#### 5.3 Readability

Use human-readable identifiers whenever possible to improve understandability and usability. Avoid using cryptic or meaningless strings.

#### 5.4 Versioning

Consider including version information in identifiers to manage changes and updates to resources over time.

Example:
```
http://example.com/namespace/resource1/v1
```

### 6. Conclusion

Identifiers are a fundamental aspect of knowledge graphs, providing a unique and persistent way to reference resources. Understanding URIs, hash vs. slash conventions, and namespaces is essential for effectively creating and managing identifiers. By following best practices, you can ensure that your identifiers are unique, persistent, and usable, facilitating data integration and interoperability.
