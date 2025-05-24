import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from .db_config import DATABASE_URL
from .modelos import Base, Cultura


import os
caminho = os.path.join(os.getcwd(), "fase1dados.csv")

def importar_dados_fase1():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)  # cria tabelas se não existirem

    Session = sessionmaker(bind=engine)
    session = Session()

    df = pd.read_csv(caminho) 

    for _, row in df.iterrows():
        cultura = Cultura(
            nome_cultura=row["cultura"],
            data_plantio=datetime.utcnow(),
            area_plantio=row["area"]
        )
        session.add(cultura)

    session.commit()
    session.close()
    print("✔️ Dados importados com sucesso!")
