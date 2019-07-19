[![DOI](https://zenodo.org/badge/161186859.svg)](http://doi.org/10.5281/zenodo.2638002)

# Ontology Restriction Types

Ontologies created with [OWL](https://www.w3.org/TR/owl2-overview/), 
or in general using the [RDF](https://www.w3.org/TR/rdf11-concepts/) framework, might contain restrictions (axioms) to machine-understandably describe knowledge.

Several types of such restrictions exist, and so far it is not known which restriction types are used to which extent in practice. 
This repository contains a vocabulary to describe restriction types, and corresponding restriction type expressions and measures ([MontoloVoc](montolo-voc.owl)).

Tools creating statistics about the use of restriction types in ontologies can use the *MontoloVoc* vocabulary to describe the statistics and refer to their structure.

# MontoloVoc Vocabulary

This repository contains the RDF/OWL based *MontoloVoc* vocabulary..
It is developed according to the UPON-light methodology. 
Hence, the `requirements` folder contains information regarding the development process the documentation (ongoing work).


# Montolo Restriction Types

The vocabulary is used to describe concepts in [Montolo](https://github.com/IDLabResearch/Montolo),
such as *restriction types*, their *expressions* and RDF DataCube-based *measurements* and *dimensions*.

Statistics based on these *Montolo* descriptions are available in the [MontoloStats](https://w3id.org/montolo/data/montolo-stats) dataset,
which covers 98% of [LOV](http://lov.linkeddata.es) and 97% [BioPortal](https://bioportal.bioontology.org) ontologies.

