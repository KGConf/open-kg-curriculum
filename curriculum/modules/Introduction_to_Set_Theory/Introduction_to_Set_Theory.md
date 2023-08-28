# Introduction to Set Theory
## Details
* Category: [Foundational](../categories/Foundational.md)
* Module Prerequisites: [Introduction to Logic](../modules/Introduction_to_Logic.md)
* Audience: [Student](../audiences/Student.md)
* Level: [Beginner](../levels/Beginner.md)

## Content

### Definitions
* A `set` is a collection of distinct things. These things may be other sets, symbols, or mathematical objects. These are called the _elements_ of a set. 
  * Sets do not have a concept of order, unless otherwise denoted.
  * Sets contain only unique elements, that is, there are no exact duplicates in any set.
* An `_n_-tuple` is an ordered set of $n$ elements.

#### Syntax
* Sets are generally denoted by capital letters, e.g., $`X, Y, Z`$. Curly Bracess `{}` are used to denote the contents of a set. There are a couple ways of specifying which elements belong in a set.
  * Set Roster Notation -- exhaustively listing out every element within a set
    * Finite: $`X = \{1, 5, .4, a, Y \}`$
    * Infinite: $` X = \{a_1, a_2, a_3, ..., a_10\}`$ or $`Y = \{1, 2, 3, 4, ...\}`$ 
  * Set Builder Notation -- create a ``rule'' by which membership to the set is defined. This has the form $`\{x|P(x)\}`$, where $P(\cdot)$ is defined as some proposition, qualification, or conditional which returns true for a given argument $x$.
    * Example: The set of all even integers is defined as $`\mathbb{Z}^{\text{even}} = \{2i|i\in\mathbb{Z}\}`$.
  * A set which is empty is denoted by $\emptyset$.
* Tuples are also generally denoted using capital letters, e.g., $X,Y,Z$. Parentheses `()` are used to denote the contents of a tuple e.g., $(1,2)$ or $(x,y)$.

#### Operations Over Sets
* Set Membership -- for an element $a$ and set $A$, membership is denoted as $a \in A$, meaning that the element $a$ is in the set $A$.
* Subset & Superset -- for sets $X,Y$, $X \subseteq Y$ iff $\forall x\in X, x\in Y$.
  * $X$ would be a subset of $Y$, and $Y$ would be a superset of $X$.
  * A set $X$ is said to be a _proper subset_ of $Y$, denoted $X \subset Y$ iff $\forall x \in X, x \in Y$ and $X \not= Y$.  
* Set Intersection -- for sets $X,Y$, intersection defined as by $`X \cap Y = \{a|a \in X \text{~and~} a \in Y\}`$.
* Set Union -- for sets $X,Y$, intersection defined as by $`X \cup Y = \{a|a \in X \text{~or~} a \in Y\}`$.
* Set Cardinality -- for a set $X$, denoted as $|X|$, meaning the number of distinct elements in $X$.
* Cartesian Product -- for sets $X,Y$, the Cartesian product is defined as $`X \times Y = \{(x,y)|\forall x \in X \text{~and~} \forall y \in Y\}`$.

#### Some Common Sets
* $\mathbb{Z}$ -- the set of all integers
  * $`\mathbb{Z}^+`$ -- the set of positive integers
  * $`\mathbb{Z}^-`$ -- the set of negative integers
  * $`\mathbb{Z}^{\text{nneg}}`$ -- the set of non-negative integers
* $\mathbb{Q}$ -- the set of rational numbers
* $\mathbb{R}$ -- the set of real numbers
* $\mathbb{C}$ -- the set of complex numbers

#### Operations Over Tuples
* Cardinality holds over tuples
* Cartesian product holds over tuples

## Related KGC Media
* No related media

## References
[1] [Set (Mathematics) - Wikipedia](https://en.wikipedia.org/wiki/Set_(mathematics))https://en.wikipedia.org/wiki/Set_(mathematics)

## Contributors
* Cogan Shimizu
