from SPARQLWrapper import SPARQLWrapper2, JSON
import pandas
from pandas import DataFrame

def queryListOfSpecies():
  sparql = SPARQLWrapper2("http://web.cenpat-conicet.gob.ar:7200/repositories/BiGeOnto")
  sparql.setQuery("""
      PREFIX dwc: <http://rs.tdwg.org/dwc/terms/>
      PREFIX foaf: <http://xmlns.com/foaf/0.1/>
      PREFIX bigeonto: <http://www.w3id.org/cenpat-gilia/bigeonto/>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX p: <http://www.wikidata.org/prop/>
  
      SELECT ?taxon ?name ?wikidataID ?NCBIID
      WHERE {
          ?s a dwc:Occurrence.
          ?s dwc:basisOfRecord ?basis.
          ?s bigeonto:associated ?organism.
	        ?organism bigeonto:belongsTo ?taxon.
	        ?taxon dwc:scientificName ?name.
    	    ?taxon owl:sameAs ?wikidataID.
     	    ?taxon p:P685 ?NCBIID
      }
      GROUP BY ?name ?wikidataID ?taxon ?NCBIID
      ORDER BY ?name
  """)
  
  results = sparql.query().bindings
  columns = sparql.query().variables
  
  data = [[row[column].value if row.get(column) is not None else None for column in columns] for row in results]
  return DataFrame(data=data, columns=columns)
