import streamlit as st
from elasticsearch import Elasticsearch

#=================================Cria Conexão com ElasticSearch==============================================
es = Elasticsearch(hosts = ["http://localhost:9200"], 
                   basic_auth=("elastic", "nY5AQz37ZZIfMev9nY5AQz37ZZIfMev9")
                              
                    )
es_status = es

#==========================================Aplicação Streamlit=================================================
st.title("📊 Lista de Índices do Elasticsearch")

# Botão para carregar índices
if st.button("Carregar Índices"):
    try:
        indices = es.cat.indices(format="json")
        st.success(f"Total de índices encontrados: {len(indices)}")

        # Exibir em tabela
        st.write("### Detalhes dos Índices")
        st.dataframe(
            [
                {
                    "Index": idx["index"],
                    "Health": idx["health"],
                    "Docs": idx["docs.count"],
                    "Size": idx["store.size"]
                }
                for idx in indices
            ]
        )
    except Exception as e:
        st.error(f"Erro ao conectar ou listar índices: {e}")
