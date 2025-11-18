import sqlite3

class Database:
    def __init__(self, db_name="app_garantia.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def execute(self, query, params=()):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor

    def fetch_all(self, query, params=()):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def fetch_one(self, query, params=()):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()

def inicializar_banco():
    db = Database()
    db.execute("""
        CREATE TABLE IF NOT EXISTS loja (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cnpj TEXT UNIQUE NOT NULL CHECK (length(cnpj) = 14),
            endereco TEXT NOT NULL,
            telefone TEXT
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS equipamento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            num_serie TEXT UNIQUE NOT NULL,
            valor REAL NOT NULL CHECK (valor >= 0),
            id_loja INTEGER NOT NULL,
            FOREIGN KEY(id_loja) REFERENCES loja(id) ON DELETE RESTRICT
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS garantia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_equipamento INTEGER NOT NULL,
            data_inicio TEXT NOT NULL,
            data_fim TEXT NOT NULL,
            tipo TEXT NOT NULL,
            descricao TEXT,
            FOREIGN KEY(id_equipamento) REFERENCES equipamento(id) ON DELETE RESTRICT
        )
    """)

    print("Banco inicializado!")

inicializar_banco()

    
     