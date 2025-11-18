INSERT INTO loja (nome, cnpj, endereco, telefone) VALUES
('Loja Central', '12345678901234', 'Rua A, 100', '11999999999'),
('TechStore', '98765432109876', 'Av. B, 200', '11888888888'),
('InfoHouse', '55555555555555', 'Rua C, 300', '11777777777');

INSERT INTO equipamento (nome, num_serie, valor, id_loja) VALUES
('Notebook Lenovo', 'NS001', 3500.00, 1),
('Impressora HP', 'NS002', 850.00, 2),
('Monitor Dell', 'NS003', 1200.00, 3);

INSERT INTO garantia (id_equipamento, data_inicio, data_fim, tipo, descricao) VALUES
(1, '2024-01-01', '2026-01-01', 'Fabricante', 'Garantia padrão de fábrica'),
(2, '2023-05-10', '2025-05-10', 'Estendida', 'Proteção total'),
(3, '2024-03-20', '2025-03-20', 'Fabricante', 'Garantia básica');




