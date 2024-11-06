import psycopg2

# Parâmetros de conexão
dbname   = 'postgres'
user     = 'postgres'
password = '12345'
host     = 'localhost'
port     = '5432'

# Criar uma conexão
conn = psycopg2.connect(dbname=dbname,
                        user=user,
                        password=password,
                        host=host,
                        port=port)


cur = conn.cursor()# Criar um cursor que deixa manipular os dados

#comandos sql transct-sql
create_table_query = ''' CREATE TABLE exemplo ( id SERIAL PRIMARY KEY, nome VARCHAR(100), idade INT, endereco TEXT ) '''
cur.execute(create_table_query)

conn.commit() # validar alterações que fizemos e commitar para o banco de dados

# Fechar o cursor e a conexão
cur.close()
conn.close()