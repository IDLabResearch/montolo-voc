[![DOI](https://zenodo.org/badge/161186859.svg)](https://zenodo.org/badge/latestdoi/161186859)

# Ontology Restriction Types


# LOVCube Vocabulary

This repository contains the RDF/OWL based vocabulary of LOVCube.
The vocabulary is developed according to the UPON-light methodology. Hence, the `requirements` folder contains the documentation.


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

On https://lov.ilabt.imec.be/lovcube/data/relovstats/latest
