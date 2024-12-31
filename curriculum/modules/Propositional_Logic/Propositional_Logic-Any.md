# Propositional Logic

## Introduction

Propositional logic is a fundamental branch of logical reasoning that deals with propositions, which are statements that can be either true or false. This module builds upon the Introduction to Logic module, providing a deeper understanding of logical operations and their applications.

## Basic Concepts

### Propositions

A proposition is a statement that can be assigned a truth value, either true (T) or false (F). For example:
- "The sky is blue." (True)
- "2 + 2 = 5." (False)

### Logical Operators

Logical operators are symbols used to connect propositions and form more complex statements. The primary logical operators in propositional logic are:
- **Negation (NOT)**: Represented by the symbol `¬`. It reverses the truth value of a proposition.
  - If P is true, then ¬P is false.
  - If P is false, then ¬P is true.
- **Conjunction (AND)**: Represented by the symbol `∧`. It combines two propositions, and the resulting proposition is true only if both original propositions are true.
  - P ∧ Q is true if and only if both P and Q are true.
- **Disjunction (OR)**: Represented by the symbol `∨`. It combines two propositions, and the resulting proposition is true if at least one of the original propositions is true.
  - P ∨ Q is true if either P or Q (or both) are true.
- **Implication (IF-THEN)**: Represented by the symbol `→`. It forms a conditional statement where the truth of the second proposition (the consequent) depends on the truth of the first proposition (the antecedent).
  - P → Q is false only if P is true and Q is false.
- **Biconditional (IF AND ONLY IF)**: Represented by the symbol `↔`. It forms a statement that is true if and only if both propositions have the same truth value.
  - P ↔ Q is true if both P and Q are true or both are false.

## Truth Tables

Truth tables are tools used to determine the truth values of complex propositions based on the truth values of their constituent propositions. Each row of a truth table represents a possible combination of truth values for the constituent propositions, and the corresponding truth value for the complex proposition.

### Truth Table for Negation

| P | ¬P |
| --- | --- |
| T | F |
| F | T |

### Truth Table for Conjunction

| P | Q | P ∧ Q |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

### Truth Table for Disjunction

| P | Q | P ∨ Q |
| --- | --- | --- |
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

### Truth Table for Implication

| P | Q | P → Q |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

### Truth Table for Biconditional

| P | Q | P ↔ Q |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

## Logical Equivalences

Logical equivalences are statements that have the same truth value regardless of the truth values of their constituent propositions. Some important logical equivalences include:

- **Double Negation**: P ↔ ¬(¬P)
- **De Morgan's Laws**:
  - ¬(P ∧ Q) ↔ (¬P ∨ ¬Q)
  - ¬(P ∨ Q) ↔ (¬P ∧ ¬Q)
- **Distributive Laws**:
  - P ∧ (Q ∨ R) ↔ (P ∧ Q) ∨ (P ∧ R)
  - P ∨ (Q ∧ R) ↔ (P ∨ Q) ∧ (P ∨ R)
- **Absorption Laws**:
  - P ∨ (P ∧ Q) ↔ P
  - P ∧ (P ∨ Q) ↔ P

## Applications of Propositional Logic

Propositional logic has numerous applications in various fields, including:

- **Computer Science**: Propositional logic is used in the design and analysis of digital circuits, algorithms, and programming languages.
- **Mathematics**: It is used in formal proofs, set theory, and other branches of mathematics.
- **Philosophy**: Propositional logic is used in the study of arguments, reasoning, and the nature of truth.
- **Artificial Intelligence**: It is used in the development of expert systems, knowledge representation, and reasoning.

## Exercises

1. Construct truth tables for the following propositions:
   - (P ∧ Q) → R
   - (P ∨ Q) ↔ R
   - ¬(P ∧ Q) ∨ R

2. Determine the logical equivalence of the following propositions:
   - P ∧ (Q ∨ R) and (P ∧ Q) ∨ (P ∧ R)
   - ¬(P ∨ Q) and (¬P ∧ ¬Q)

3. Use propositional logic to analyze the validity of the following arguments:
   - If it is raining, then the ground is wet. It is raining. Therefore, the ground is wet.
   - If it is sunny, then it is not raining. It is not sunny. Therefore, it is raining.

## Conclusion

Propositional logic provides a formal system for analyzing and understanding logical reasoning. By mastering the basic concepts, truth tables, logical equivalences, and applications of propositional logic, you will be well-equipped to tackle more advanced topics in logic and related fields. This foundational knowledge is essential for further studies in computer science, mathematics, philosophy, and artificial intelligence.