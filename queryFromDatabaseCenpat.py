from SPARQLWrapper import SPARQLWrapper2
import pandas
from pandas import DataFrame

def queryFromDatabase(aId):
  sparql = SPARQLWrapper2("http://web.cenpat-conicet.gob.ar:7200/repositories/BiGeOnto")
  sparql.setQuery("""SELECT ?attributes ?value
  WHERE { 
    SERVICE<https://bio2rdf.org/sparql>{
    <http://bio2rdf.org/taxonomy:"""+ aId +"""> ?attributes ?value }
    }"""
  )
  
  results = sparql.query().bindings
  columns = sparql.query().variables
  
  if not results:
        data = [['-' for _ in columns]]
        return DataFrame(data=data, columns=columns)
  
  data = [[row[column].value if row.get(column) is not None else None for column in columns] for row in results]
  return DataFrame(data=data, columns=columns)
