This table contains the lexicon (outcome of step 1) and glossary (outcome of step 2) of the UPON-light methodology.

| Term                                     | Synonyms                         | Kind        | Description                        | Source                          | Suggested By | Updated by |
|------------------------------------------|----------------------------------|-------------|------------------------------------|---------------------------------|--------------|------------|
| Restriction Type                         | rdfcv:SimpleConstraint, prov:Entity | | Restrictions can be divided into different types, e.g. cardinality or subsumption. The [RDF-CV](https://github.com/boschthomas/RDF-Constraints-Vocabulary) vocabulary defines restriction types in a generic way. | LOVCube paper, related work by Hartmann [xx] | @slieber | @slieber | 
| Restriction Type Expression              | qb:DimensionProperty| | A restriction type can be expressed differently, e.g. disjointness can be modeled using *owl:disjointWith* or *owl:AllDisjointClasses*. Which Restriction Type Expression was used to gather a result, is also important provenance information, thus it should also be a statistical dimension of the result dataset. | LOVCube paper | @slieber | @slieber |
| Restriction Type Metric                  | qb:MeasureProperty | | | | | |
| Restriction Type Detector                | frbr:Work, prov:Entity | | One detector is responsible to gather information of one Restriction Type Expression. | | | |
| Restriction Type Detector Version        | frbr:Expression, prov:Entity | | A detector can be subject of changes. For correctness, an older result should not be linked to a newer version of a detector. Thus provenance is important and different versions need to be explicit. | | @slieber | @slieber |
| Restriction Type Detector Implementation | | | | | | | |
