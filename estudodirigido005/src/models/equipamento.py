from database import Database

class Equipamento:
    def __init__(self):
        self.db = Database()

    def criar(self, nome, num_serie, valor, id_loja):
        query = """
        INSERT INTO equipamento (nome, numero_serie, valor, loja_id)
        VALUES (?, ?, ?, ?)
        """
        self.db.execute(query, (nome, num_serie, valor, id_loja))
        print("Equipamento cadastrado!")

    def listar(self):
        query = """
        SELECT e.id,
               e.nome,
               e.num_serie,
               e.valor,
               l.nome AS loja
        FROM equipamento e
        JOIN loja l ON l.id = e.id_loja
        """
        return self.db.fetch_all(query)
    


