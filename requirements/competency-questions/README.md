This file contains a list of competency questions, the vocabulary aims to answer.

* The *ID* column should identify each question with a numerical ID prefixed by the letters *CQ*
* The *Question* column should state the question
* The *Expected Answer* column should state the expected answer
* The *Motivating Scenario* column should state the name of the user story, located in the `user-stories` folder
* The *SPARQL query* column should state the name of the SPARQL query file, located in the `sparql-queries` folder

| ID   | Question                           | Expected Answer                   | Motivating Scenario | SPARQL query          |
|------|------------------------------------|-----------------------------------|---------------------|-----------------------|
| CQ1  | Which restriction-types do exist?
| CQ2  | How many restriction-types do exist?
| CQ3  | Which Restriction Type Expressions for a given restriction-type exist?
| CQ4  | How many Restriction Type Expressions for a given restriction-type exist?
| CQ5  | How is a restriction-type defined in a logical expression?
| CQ6  | What is the unit of the result attribute? (e.g. integer, boolean)
| CQ7  | Who created a Restriction Type Expression?
| CQ8  | How many versions of a Restriction Type Expression exist?
| CQ9  | How many implementations of a restriction-type detector exist? (E.g. SPARQL-query and LODStats module)
| CQ10 | Which implementations of a Restriction Type Expression Detector exist?
| CQ11 | What is the human-understandable reason for a change in Restriction Type Expression Detector version?
| CQ12 | When was the result generated?
| CQ13 | Which version of the vocabulary/ontology was analyzed?
| CQ14 | Which Restriction Type Expressions Detectors were used to generate the result?
| CQ15 | Which implementation of the Restriction Type Expression Detector was used to create the result? (e.g. SPARQL or LODStats module)
| CQ16 | Which version of a Restriction Type Expression Detector was used to generate the result?
| CQ17 | What are the Restriction Type Expression Detector-related constituents of a Restriction Type-related result?
| CQ18 | What is the result of a Restriction Type-related result?
| CQ19 | What attribute units are part of the result? (e.g. integer boolean)

## SPARQL queries

### CQ1

```
PREFIX lovc:     <http://example.com/lovcube#>

select distinct ?type where {
  ?type a lovc:RestrictionType .
}
```

### CQ2

```
PREFIX lovc:     <http://example.com/lovcube#>

select (count(distinct ?type) as ?typeCount) where {
  ?type a lovc:RestrictionType .
}
```

### CQ3

???

### CQ4

???

### CQ5

???

### CQ6

```
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.org/lovstats#>


select distinct ?range where {
  ?p a qb:MeasureProperty ;
    rdfs:range ?range .
}
```

### CQ7

???

### CQ8

???

### CQ9

```
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.org/lovstats#>
PREFIX lovc:     <http://example.com/lovcube#>


select (count(distinct ?impl) as ?implementationCount) where {
  ?impl a lovc:Implementation .
}
```

### CQ10

```
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.org/lovstats#>
PREFIX lovc:     <http://example.com/lovcube#>


select distinct ?impl where {
  ?impl a lovc:Implementation .
}
```

### CQ11

Not available yet

### CQ12

```
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.org/lovstats#>


select distinct ?Concept ?time where {
  ?Concept a qb:Observation ;
    lovstats:execution-time ?time.
}
```

### CQ13

```
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.org/lovstats#>


select distinct ?Concept ?version where {
  ?Concept a qb:Observation ;
    lovstats:ontology-version ?version.
}
```

### CQ14

```
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.org/lovstats#>

select distinct ?dataset ?detector where {
  ?Concept a qb:Observation ;
    qb:dataSet ?dataset ;
    lovstats:detector ?detector .
}
```


### CQ15

```
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.org/lovstats#>


select distinct ?dataset ?detector ?implementation where {
  ?Concept a qb:Observation ;
    qb:dataSet ?dataset ;
    lovstats:detector ?detector ;
    lovstats:implementation ?implementation .
}
```

### CQ16

Hmm, that's weird, detector is already the version?

### CQ17

```
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.org/lovstats#>

select distinct ?measurePredicate where {
  lovstats:lovstats2018datastructure a qb:DataStructureDefinition ;
    qb:component [
      qb:measure ?measurePredicate
    ] .
}
```

### CQ18

```
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.org/lovstats#>


select distinct ?dataset ?detector ?measurePredicate ?output where {
  ?Concept a qb:Observation ;
    lovstats:detector ?detector ;
    ?measurePredicate ?output .
  {
    select distinct ?measurePredicate where {
      lovstats:lovstats2018datastructure a qb:DataStructureDefinition ;
        qb:component [
          qb:measure ?measurePredicate
        ] .
    }
  }
}
```

### CQ19

```
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.org/lovstats#>


select distinct ?dataset (datatype(?output) as ?datatype) where {
  ?Concept a qb:Observation ;
    lovstats:detector ?detector ;
    ?measurePredicate ?output .
  {
    select distinct ?measurePredicate where {
      lovstats:lovstats2018datastructure a qb:DataStructureDefinition ;
        qb:component [
          qb:measure ?measurePredicate
        ] .
    }
  }
}
```

---

So, I invented these: results larger than 0. might be what you expected before, but didn't specify

### CQ20

```
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.org/lovstats#>


select distinct ?type where {
  ?Concept a qb:Observation ; 
    lovstats:restriction-type ?type;
    lovstats:amount ?amount .
  FILTER (?amount > 0)
}
```

### CQ21

```
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.org/lovstats#>


select (count(distinct ?type) as ?tcount) where {
  ?Concept a qb:Observation ; 
    lovstats:restriction-type ?type;
    lovstats:amount ?amount .
  FILTER (?amount > 0)
}
```

### CQ22

```
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.org/lovstats#>


select distinct ?type ?detector where {
  ?Concept a qb:Observation ; 
    lovstats:restriction-type ?type;
    lovstats:detector ?detector ;
    lovstats:amount ?amount .
  FILTER (?amount > 0)
}
```

### CQ23

```
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX lovstats: <http://example.org/lovstats#>


select distinct ?type ?detector (count(?detector) as ?detectorCount) where {
  ?Concept a qb:Observation ; 
    lovstats:restriction-type ?type;
    lovstats:detector ?detector ;
    lovstats:amount ?amount .
  FILTER (?amount > 0)
} group by ?type ?detector
```
