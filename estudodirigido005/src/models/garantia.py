from database import Database

class Garantia:
    def __init__(self):
        self.db = Database()

    def criar(self, id_equipamento, data_inicio, data_fim, tipo, descricao):
        query = """
        INSERT INTO garantia (id_equipamento, data_inicio, data_fim, tipo, descricao)
        VALUES (?, ?, ?, ?, ?)
        """
        self.db.execute(query, (id_equipamento, data_inicio, data_fim, tipo, descricao))
        print("Garantia cadastrada!")

    def listar(self):
        query = """
        SELECT 
            g.id,
            e.nome AS equipamento,
            g.data_inicio,
            g.data_fim,
            g.tipo,
            g.descricao
        FROM garantia g
        JOIN equipamento e ON e.id = g.id_equipamento
        """
        return self.db.fetch_all(query)
