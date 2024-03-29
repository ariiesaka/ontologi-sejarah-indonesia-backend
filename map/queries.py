prefix = """
prefix :      <http://127.0.0.1:3333/> 
prefix foaf:  <http://xmlns.com/foaf/0.1/> 
prefix geo:   <http://www.opengis.net/ont/geosparql#> 
prefix owl:   <http://www.w3.org/2002/07/owl#> 
prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> 
prefix sem:   <http://semanticweb.cs.vu.nl/2009/11/sem/> 
prefix time:  <http://www.w3.org/2006/time#> 
prefix vcard: <http://www.w3.org/2006/vcard/ns#> 
prefix xsd:   <http://www.w3.org/2001/XMLSchema#> 
"""

get_types = """
select DISTINCT 
(GROUP_CONCAT(distinct ?typeLabel; SEPARATOR=",") as ?typeLabels)
where {{
    :{0} rdf:type ?type .
    ?type rdfs:label ?typeLabel .
}}
"""

event = """
select DISTINCT ?label ?dateStart ?dateEnd ?location ?feature ?featureLabel

where {{
    :{0} rdfs:label ?label ;
        :location ?feature .
        
    :{0} time:hasTime ?tempEntity .
    ?tempEntity time:hasBeginning ?inst1 ;
    	time:hasEnd ?inst2 .
    
    ?inst1 time:inXSDDate ?dateStart .
    ?inst2 time:inXSDDate ?dateEnd .
    
    ?feature rdfs:label ?featureLabel
    
    OPTIONAL {{ 
        ?feature geo:hasGeometry ?geometry .
    
        ?geometry geo:asWKT ?location .
    }}
}}
"""


military_conflict = """
select DISTINCT ?result 
(GROUP_CONCAT(DISTINCT ?combatant1; SEPARATOR=",") AS ?combatants1)
(GROUP_CONCAT(DISTINCT ?combatant1Label; SEPARATOR=",") AS ?combatants1Label)
(GROUP_CONCAT(DISTINCT ?combatant2; SEPARATOR=",") AS ?combatants2)
(GROUP_CONCAT(DISTINCT ?combatant2Label; SEPARATOR=",") AS ?combatants2Label)
(GROUP_CONCAT(DISTINCT ?commander1; SEPARATOR=",") AS ?commanders1)
(GROUP_CONCAT(DISTINCT ?commander1Label; SEPARATOR=",") AS ?commanders1Label)
(GROUP_CONCAT(DISTINCT ?commander2; SEPARATOR=",") AS ?commanders2)
(GROUP_CONCAT(DISTINCT ?commander2Label; SEPARATOR=",") AS ?commanders2Label)
?strength1 ?strength2 ?casualties1 ?casualties2 ?causes where {{    
    OPTIONAL {{
        :{0} :result ?result
    }}
    
    OPTIONAL {{
        :{0} :combatant1 ?combatant1 .
        ?combatant1 rdfs:label ?combatant1Label
    }}
    
    OPTIONAL {{
        :{0} :combatant2 ?combatant2 .
        ?combatant2 rdfs:label ?combatant2Label
    }}
    
    OPTIONAL {{
        :{0} :commander1 ?commander1 .
        ?commander1 rdfs:label ?commander1Label
    }}
    
    OPTIONAL {{
        :{0} :commander2 ?commander2 .
        ?commander2 rdfs:label ?commander2Label
    }}
    
    OPTIONAL {{
        :{0} :strength1 ?strength1
    }}
    
    OPTIONAL {{
        :{0} :strength2 ?strength2
    }}
    
    OPTIONAL {{
        :{0} :casualties1 ?casualties1
    }}
    
    OPTIONAL {{
        :{0} :casualties2 ?casualties2
    }}
    
}} GROUP BY ?result ?strength1 ?strength2 ?casualties1 ?casualties2 ?causes
"""