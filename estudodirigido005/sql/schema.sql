PRAGMA foreign_keys = ON;

-- ============================
-- TABELA: loja
-- ============================
CREATE TABLE IF NOT EXISTS loja (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cnpj TEXT UNIQUE NOT NULL CHECK (length(cnpj) = 14),
    endereco TEXT NOT NULL,
    telefone TEXT
);

-- ============================
-- TABELA: equipamento
-- ============================
CREATE TABLE IF NOT EXISTS equipamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    num_serie TEXT UNIQUE NOT NULL,
    valor REAL NOT NULL CHECK (valor >= 0),
    id_loja INTEGER NOT NULL,
    FOREIGN KEY (id_loja) REFERENCES loja(id) ON DELETE RESTRICT
);

-- ============================
-- TABELA: garantia
-- ============================
CREATE TABLE IF NOT EXISTS garantia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_equipamento INTEGER NOT NULL,
    data_inicio TEXT NOT NULL,
    data_fim TEXT NOT NULL,
    tipo TEXT NOT NULL,
    descricao TEXT,
    FOREIGN KEY (id_equipamento) REFERENCES equipamento(id) ON DELETE RESTRICT
);
