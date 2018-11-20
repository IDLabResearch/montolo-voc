This table contains the taxonomy (outcome of step 3) of the UPON-light methodology.
According to UPON-light, one taxonomy is made per kind (so we have one table for *Objects*, one for *Processes* and one for *Properties*).

# Objects
| Concept                 | 1st Specialization     | 2nd Specialization        | 3rd Specialization         | 4th Specialization         | Suggested By | Updated by |
|-------------------------|------------------------|---------------------------|----------------------------|----------------------------|--------------|------------|
| rdfcv:SimpleConstraint  | RestrictionDefinition  | | | | @slieber | @slieber |
| prov:Entity             | RestrictionType        | | | | @slieber | @slieber |
| qb:DimensionProperty, prov:Entity | RestrictionTypeExpression | | | @slieber | @slieber |
| qb:MeasureProperty, prov:Entity | RestrictionTypeMetric | | | @slieber | @slieber |
| frbr:Work, prov:Entity | RestrictionTypeDetector | | | | @slieber | @slieber |
| frbr:Expression, qb:MeasureProperty, prov:Entity | RestrictionTypeDetectorVersion | | | | @slieber | @slieber |
| qb:MeasureProperty, prov:Entity | RestrictionTypeDetectorImplementation | | | | @slieber | @slieber |
| qb:Observation, prov:Entity | RestrictionTypeStatistic | | | | @slieber | @slieber |
| qb:DataSet, prov:Entity | Dataset | | | | @slieber | @slieber |
| qb:DataStructureDefinition | DataStructureDefinition | | | | @slieber | @slieber |

# Processes
| Concept                 | 1st Specialization     | 2nd Specialization        | 3rd Specialization         | 4th Specialization         | Suggested By | Updated by |
|-------------------------|------------------------|---------------------------|----------------------------|----------------------------|--------------|------------|
| prov:Activity           | DatasetCreation        | | | | @slieber | @slieber |

# Properties
| Concept                 | 1st Specialization     | 2nd Specialization        | 3rd Specialization         | 4th Specialization         | Suggested By | Updated by |
|-------------------------|------------------------|---------------------------|----------------------------|----------------------------|--------------|------------|
| hasRestrictionTypeDefinition | | | | | @slieber | @slieber |
