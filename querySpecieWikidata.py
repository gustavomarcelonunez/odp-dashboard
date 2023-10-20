from SPARQLWrapper import SPARQLWrapper2
import pandas
from pandas import DataFrame

def querySpecie(aSpecie):
 
  sparql = SPARQLWrapper2("https://query.wikidata.org/bigdata/namespace/wdq/sparql")
  sparql.setQuery("""
    SELECT DISTINCT ?item ?scientific_name ?common_name ?status ?rangemap ?length ?life_expectency ?height ?mass 
    WHERE {
      ?item wdt:P225 ?scientific_name;
      wdt:P1843 ?common_name.
    
      OPTIONAL { ?item wdt:P2043 ?length. }
      OPTIONAL { ?item wdt:P2250 ?life_expectency }
      OPTIONAL { ?item wdt:P2048 ?height. }
      OPTIONAL { ?item wdt:P141 ?status.}
      OPTIONAL { ?item wdt:P181 ?rangemap.}
  
      OPTIONAL {
        ?item p:P2067 ?mass_statement_node.
        ?mass_statement_node pq:P642 wd:Q78101716;
        ps:P2067 ?mass.
      }
    FILTER(LANGMATCHES(LANG(?common_name), \"en\"))
    FILTER(lcase(str(?scientific_name)) IN (lcase(str(\""""+ aSpecie +"""\"))))

    SERVICE wikibase:label { bd:serviceParam wikibase:language \"[AUTO_LANGUAGE],en\". }

  
    } """
  )
  
  results = sparql.query().bindings
  columns = sparql.query().variables
  
  if not results:
        data = [['-' for _ in columns]]
        return DataFrame(data=data, columns=columns)
  
  data = [[row[column].value if row.get(column) is not None else None for column in columns] for row in results]
  return DataFrame(data=data, columns=columns)

