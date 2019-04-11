[![DOI](https://zenodo.org/badge/161186859.svg)](https://zenodo.org/badge/latestdoi/161186859)

# Ontology Restriction Types

Ontologies created with [OWL](https://www.w3.org/TR/owl2-overview/), 
or in general using the [RDF](https://www.w3.org/TR/rdf11-concepts/) framework, might contain restrictions (axioms) to machine-understandably describe knowledge.

Several types of such restrictions exist, and so far it is not known which restriction types are used to which extent in practice. 
This repository contains a vocabulary to describe restriction types, and corresponding restriction type expressions and measures ([LOVCube](lovcube.owl)).
Additionally it contains RDF-based descriptions of several abstract restriction types and their concrete RDF-based expressions ([relovstats.ttl](relovstats.ttl)).

Tools creating statistics about the use of restriction types in ontologies can use the LOVCube vocabulary to describe the statistics and refer to their structure.

# LOVCube Vocabulary

This repository contains the RDF/OWL based vocabulary of LOVCube.
The vocabulary is developed according to the UPON-light methodology. Hence, the `requirements` folder contains information regarding the development process the documentation (ongoing work).


# ReLOVStats Restriction Types

The [relovstats](relovstats.ttl) file contains the descriptions of several restriction types, restriction type expressions and restriction type measures.
Statistical observations made based on LOVCube, should link to a corresponding `data structure definition` as defined by RDF Data Cube (see following listing).
We also provide several such data structures in the [relovstats](relovstats.ttl) file.

```turtle
@prefix lovc: <https://w3id.org/lovcube/ns/lovcube#> .
@prefix rls: <https://w3id.org/lovcube/ns/relovstats#> .

# Created statistics, described using the RDF Data Cube compliant LOVCube vocabulary
# The observation links to a corresponding RDF Data Cube dataset (described below)
[] a qb:Observation, prov:Entity, lovc:RestrictionTypeStatistic ;
    lrd:detectorDimension lrd:maximumUnqualifiedCardinalityDetector ;
    lrd:detectorVersionDimension lrd:maximumUnqualifiedCardinalityLODStatsDetectorOwl-v1 ;
    lrd:executionTimeDimension "2019-04-05T11:48:21.845150"^^xsd:dateTime ;
    lrd:ontologyVersionDimension prov: ;
    lrd:restrictionTypeDimension lrd:maximumUnqualifiedCardinality ;
    lrd:restrictionTypeOccurrence 1 ;
    qb:dataSet _:N740f60a3437f4b46869218f604ee20e4 ;
    prov:qualifiedGeneration _:Nd459003b47e54c04ae84a21707a1460b .

_:Nd92c84d33f9144549dd1fdfc1b98b620 a prov:Activity .

_:Nd459003b47e54c04ae84a21707a1460b a prov:Generation,
        prov:InstantaneousEvent ;
    prov:activity _:Nd92c84d33f9144549dd1fdfc1b98b620 ;
    prov:atTime "2019-04-05T11:48:21.845150"^^xsd:dateTime .

# A RDF Data Cube dataset which refers to a data structure definition, defined in this repository (relovstats.ttl)
_:N740f60a3437f4b46869218f604ee20e4 a qb:DataSet,
        prov:Entity,
        lovc:Dataset ;
    qb:structure lrd:restrictionTypesAmount ;
    prov:qualifiedGeneration _:Nd459003b47e54c04ae84a21707a1460b ;
    prov:wasGeneratedBy _:Nd92c84d33f9144549dd1fdfc1b98b620 .

```

# How to use?

On https://lov.ilabt.imec.be/lovcube/data/relovstats/latest (alternatively [here](https://figshare.com/articles/ReLOVStats/7981718/1]) an existing dataset can be queried.
It was created based on 98% of [LOV](http://lov.linkeddata.es) ontologies.

Example SPARQL query to get restriction types and correpsonding occurrence measure
```sparql
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.com/lovrestrictiondata#>

SELECT ((strafter(str(?type), "#")) as ?typeName) (SUM(?occurrence) as ?total) ?ontology
WHERE {
  ?obs a qb:Observation ;
    lovstats:restrictionTypeOccurrence ?occurrence ;
    lovstats:restrictionTypeDimension ?type ;
    lovstats:detectorVersionDimension ?detector ;
    lovstats:ontologyVersionDimension ?ontology .


}
GROUP BY ?type ?ontology
ORDER BY ?type ASC(?total) ?ontology

```
