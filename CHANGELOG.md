# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2020-08-19

### Added

- Class `:Repository` as not all RDF input data might come from an ontology repository, e.g. SHACL files from GitHub
- `:OntologyRepository` class now a subclass of the new `:Repository` class
- added several `rdfs:comment` triples to provide further information

### Removed

- Class `:RestrictionTypeDetector` removed as *detection* can only be performed by `:RestrictionTypeExpressionDetector`
- Subclass statement removed: Class `:RestrictionTypeExpressionDetectorVersion` was accidentally a subclass of `qb:MeasureProperty`
- Subclass statement removed: Class `:RestrictionTypeMeasure` was accidentally a subclass of `qb:MeasureProperty`
- Several class and property definitions from other ontologies removed which initially were inserted by Protege
- Definitions of the outdated lovcube ontology, this was supposed to be already rebranded to montolo-voc

### Changed

- Domain of `:detectsRestrictionTypeExpression` was changed from `:RestrictionTypeDetector` to `:RestrictionTypeExpressionDetector`
- File extension of the ontology changed from `.owl` to `.ttl` as it already contained turtle



## [1.0.0] - 2019-07-19

### Added

- First official version

[1.0.0]: https://github.com/IDLabResearch/montolo-voc/releases/tag/v1.0.0
[2.0.0]: https://github.com/IDLabResearch/montolo-voc/compare/v1.0.0...v2.0.0
