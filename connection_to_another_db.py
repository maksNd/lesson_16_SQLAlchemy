"""
DBAPI драйверы:
SQLite - default
PostgreSQL - psycopg2
MS SQL - PyODBC
Oracle - cx-Oracle


data source name (dsn) - строка-подключение к БД
dialect+driver://username:password@host:port/database
dialect - название БД

SQLite в файле
'sqlite:///db_name.db'

MySQL
'mysql+pymysql:///root:pass@localhost/mydb'

PostgreSQL без авторизации
'postgresql+psycopg2://localhost/mydb'

Oracle
'oracle+cx_oracle://root:pass@localhost/mydb'

MSSQL
'mssql+pyodbc://root:pass@localhost/mydb'
"""