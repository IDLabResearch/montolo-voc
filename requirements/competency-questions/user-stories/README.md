This file contains different user stories, describing the motivation for the vocabulary.
First concepts (last column) are derived, and concrete competency questions arise (table in separate folder).


| ID  | Name                                        | User Story                                                       | Extracted concepts                      |
|-----|---------------------------------------------|------------------------------------------------------------------|-----------------------------------------|
| US1 | Different types of restrictions             | Concepts in an ontology can be arranged in a taxonomy, but also or additionally are put in relation to each other. These relations can have additional restrictions. | Restriction Type                          |
| US2 | Similar expressions in different languages  | The modeling of a hierarchy of concepts can be done using e.g. *rdfs:subclassOf* or via *skos:narrower*, or *skos:broader*. Similarly also other restriction types can be expressed using different vocabularies. | Restriction Type Expression           | 
| US3 | Equivalent expressions in the same language | Ontology languages might offer different, semantically equivalent, ways to express a restriction. E.g. in owl a class *A* can be defined as disjoint to another class using *owl:disjointWith*, but to avoid defining this relationship with *every* class, *A* is disjoint with, the class *owl:AllDisjointClasses* can be used.                                                           |                                         |
| US4 | Detecting expressions                       | As seen in US2 and US3, restriction types can be expressed differently. Thus if someone wants to check if an ontology contains restrictions of a certain type, each Restriction Type Expression needs to be taken into account.            | *Detector* used to detect Restriction Type Expressions         |
| US5 | Different statistical metrics               | Different statistical metrics per Restriction Type can provide insights. E.g. previous work used amounts, but also measures like average, minimum and maximum.     | Restriction Type Metrics    |
| US6 | Extendibility                               | It is not possible to foreseen every way a Restriction Type is expressed, as new vocabularies to define restrictions being created. Similarly the community might identify new Restriction Types, or new Restriction Types Statistics | |
| US7 | Clear definitions                           | Each Restriction [Type, Expression, Statistic] needs to be understandable by humans and thus needs a definition | |
| US8 | | | |
