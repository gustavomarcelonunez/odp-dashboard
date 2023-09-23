from SPARQLWrapper import SPARQLWrapper2, JSON

def queryListOfSpecies():
  sparql = SPARQLWrapper2("http://web.cenpat-conicet.gob.ar:7200/repositories/BiGeOnto")
  sparql.setQuery("""
      PREFIX dwc: <http://rs.tdwg.org/dwc/terms/>
      PREFIX foaf: <http://xmlns.com/foaf/0.1/>
      PREFIX bigeonto: <http://www.w3id.org/cenpat-gilia/bigeonto/>
  
      SELECT ?name
      WHERE {
          ?s a dwc:Occurrence.
          ?s dwc:basisOfRecord ?basis.
          ?s bigeonto:associated ?organism.
          ?organism bigeonto:belongsTo ?taxon.
          ?taxon dwc:scientificName ?name.
       FILTER regex(STR(?basis), \"HumanObservation\")
      }
      GROUP BY ?name
      ORDER BY ?name
  """)
  
  species = [result.get('name').value for result in sparql.query().bindings]
  
  return species
