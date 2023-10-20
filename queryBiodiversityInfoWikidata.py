from SPARQLWrapper import SPARQLWrapper2
import pandas
from pandas import DataFrame

def queryBiodiversityInfo(aSpecieId):
  sparql = SPARQLWrapper2("https://query.wikidata.org/bigdata/namespace/wdq/sparql")
  sparql.setQuery("""SELECT DISTINCT ?propertyLabel  ?link
    WHERE { 
      wd:Q"""+ aSpecieId +""" ?propertyclaim ?_value .     
      ?property wikibase:propertyType wikibase:ExternalId .    
      ?property wikibase:directClaim ?propertyclaim .   
      OPTIONAL {?property wdt:P1630 ?formatterURL .}    
      BIND(IF(BOUND(?formatterURL), IRI(REPLACE(?formatterURL, \"\\\\$1\", ?_value)) , ?_value) AS ?link)
      SERVICE wikibase:label { bd:serviceParam wikibase:language \"en\". }                                     
    }"""
  )
  results = sparql.query().bindings
  columns = sparql.query().variables
  
  if not results:
        data = [['-' for _ in columns]]
        return DataFrame(data=data, columns=columns)
  
  data = [[row[column].value if row.get(column) is not None else None for column in columns] for row in results]
  return DataFrame(data=data, columns=columns)
