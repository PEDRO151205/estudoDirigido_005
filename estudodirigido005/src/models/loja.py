from database import Database

class Loja:
    def __init__(self):
        self.db = Database()

    def criar(self, nome, cnpj, endereco, telefone):
        query = """
        INSERT INTO loja (nome, cnpj, endereco, telefone)
        VALUES (?, ?, ?, ?)
        """
        self.db.execute(query, (nome, cnpj, endereco, telefone))
        print("Loja cadastrada!")

    def listar(self):
        query = "SELECT * FROM loja"
        return self.db.fetch_all(query)


