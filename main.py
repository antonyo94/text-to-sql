from train import train_model
from eval import generate_sql

ddl = """
    
    CREATE TABLE ARCA
    (
        CODICEFISCALE VARCHAR(50),
        DATANASCITA DATETIME 
    )
    
    CREATE TABLE UNILAV
    (
        IDCOMUNICAZIONE BIGINT,
        CFLAVORATORE VARCHAR(50),
        CFDATORELAVORO VARCHAR(10),
        DATAINVIO DATETIME,
        DATAINIZIO DATETIME,
        DATAFINE DATETIME,
        FLAGPUBBLICAAMMINISTRAZIONE BOOLEAN
    )
    
     CREATE TABLE UNEX
    (
        CODICEFISCALE VARCHAR(50),
        PERIODO_DAL DATETIME,
        PERIODO_AL DATETIME,
        FONDO VARCHAR(10)
    )
"""

doc = "La tabella ARCA contiene i dati anagrafici dei cittadini. " \
      "L'età può essere calcolata a partire da DATANASCITA di ARCA. " \
      "La tabella UNILAV contiene i rapporti di lavoro. " \
      "I rapporti di lavoro del settore privato hanno FLAGPUBBLICAAMMINISTRAZIONE=0. "

vn = train_model(ddl, doc)

#QUERY 1
#query = "Quali sono i codici fiscali dei lavoratori?"

#QUERY 2
#query = "Quali sono i codici fiscali dei lavoratori UNILAV di età compresa tra i 18 ed i 30 anni?"

#QUERY 3
query = "Quali sono i codici fiscali dei lavoratori UNILAV di età compresa tra i 18 ed i 30 anni appartenenti al settore privato?"

generate_sql(vn, query)