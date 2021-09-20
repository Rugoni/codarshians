
import pandas as pd
import sqlalchemy
from sqlalchemy.orm import sessionmaker

print(" -------- START -------- ")

# data = pd.read_csv(
#     "./data_csv/K3241.K03200Y1.D10814.EMPRECSV",
#     sep=';',
#     encoding_errors='replace',
#     names=['coluna1', 'coluna2', 'coluna3', 'coluna4', 'coluna5', 'coluna6', 'coluna7'],
#     #error_bad_lines=False
# )

df_simples = pd.read_csv(
    "./data_csv/export_simples.csv"
)

print(df_simples)
# engine = sqlalchemy.create_engine("postgresql://admin:root@postgres_container:5432/cnpj_base")
# con = engine.connect()

# # Verify that there are no existing tables
# print(engine.table_names())

# # Session = sessionmaker(bind=engine) 
# # with Session() as session:
# data_head = data.head()
# print(data_head)

# data_head.to_sql('empresas', con=engine, if_exists='replace',index=False)

# engine.execute("SELECT * FROM empresas").fetchall()

# print(engine.table_names())
print(" -------- END -------- ")