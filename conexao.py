# -*- coding: utf-8 -*-

#Importando a biblioteca Elasticsearch

from elasticsearch import Elasticsearch as es 

es_status = es(hosts = ["http://localhost:9200"], 
                   basic_auth=("elastic", "nY5AQz37ZZIfMev9nY5AQz37ZZIfMev9")
                   
                   
                    )

print(es_status.info())

#===================================Listar todos os índices===================================================
indices = es_status.cat.indices(format="json")  # retorna em formato JSON
 
# Exibindo os índices
for idx in indices:
    print(f"Index: {idx['index']}, Health: {idx['health']}, Docs: {idx['docs.count']}, Size: {idx['store.size']}")

#curl -XGET "localhost:9200/_cluster/health?pretty"

#curl -XGET "localhost:9200/_cat/indices?v" 

#curl -XGET "localhost:9200/nome_do_indice/_search?pretty" -H 'Content-Type: application/json' -d'



