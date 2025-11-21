## 📌 Descrição Geral Este projeto tem como objetivo modelar e implementar um **sistema de controle de garantias de equipamentos** vendidos por lojas. O trabalho aborda as etapas de **modelagem de dados (conceitual, lógico e físico)**, além da execução dos scripts SQL em ambiente de banco de dados.

---

# 🧩 Estrutura do Projeto


flowchart TD

A[ed005_garantia_nomeAluno/] --> B[sql/]
A --> C[src/]
A --> H[prints/]
A --> R[README.md]

%% SQL
B --> B1[schema.sql]
B --> B2[inserts.sql]

%% SRC
C --> C1[main.py]
C --> C2[database.py]
C --> D[models/]

%% Models
D --> D1[equipamento.py]
D --> D2[garantia.py]
D --> D3[loja.py]
D --> D4[documentos.py]
D --> D5[usuarios.py]

%% Prints
H --> H1[modelo_logico.png]
H --> H2[consultas_dbeaver.png]
H --> H3[execucao_terminal.png]
                 






## 🧠 Modelo de Dados

# 📌 Entidades Principais

| Entidade        | Descrição                                | Atributos principais                                               |
| --------------- | ---------------------------------------- | ------------------------------------------------------------------ |
| **Loja**        | Representa uma loja de vendas            | `id_loja`, `nome`, `cnpj`, `endereco`, `telefone`                  |
| **Equipamento** | Produto vendido por uma loja             | `id_equipamento`, `nome`, `preco`, `data_venda`, `id_loja`         |
| **Garantia**    | Informações da garantia do equipamento   | `id_garantia`, `data_inicio`, `data_fim`, `tipo`, `id_equipamento` |
| **Documentos**  | Nota fiscal ou comprovantes relacionados | `id_doc`, `numero_nota`                                            |
| **Usuários**    | Clientes ou responsáveis pelo cadastro   | `id_usuario`, `cpf_usuario`                                        |

🔗 Relacionamentos

**Loja** → Equipamento: 1:N
- Uma loja pode vender vários equipamentos.

**Equipamento** → Garantia: 1:1
- Cada equipamento possui exatamente uma garantia.

Documentos e Usuários são independentes por enquanto (isolados para evoluções futuras).

## 🧮 Modelo Lógico (Resumo)
**Loja** (id_loja PK, nome, cnpj, endereco, telefone)

**Equipamento** (id_equipamento PK, nome, preco, data_venda)
            
**Garantia** (id_garantia PK, data_inicio, data_fim, tipo)
          
**Documentos** (id_doc PK, numero_nota)

**Usuários** (id_usuario PK, cpf_usuario)

## O diagrama lógico está salvo em:

📍 prints/modelo_logico.png

---

# ⚙️ Execução dos Scripts SQL

**1. Criar o banco (se necessário)**

- CREATE DATABASE app_garantia;

**2. Executar o script de criação**

- sql/schema.sql

**3. Inserir registros de teste**

- sql/inserts.sql

**4. Consultas sugeridas**

- SELECT * FROM ***loja;***
- SELECT * FROM ***equipamento;***
- SELECT * FROM ***garantia;***

## 📌 O resultado das consultas deve ser salvo em:

prints/consultas_dbeaver.png

---

# 🐍 Execução do Código Python

**Com o banco configurado corretamente, rode:**

  * python src/main.py


**Capture a tela do terminal e salve como:**

📍 prints/execucao_terminal.png

---

## 🔍 Diferença entre os Modelos
| Modelo         | O que representa                                     |
| -------------- | ---------------------------------------------------- |
| **Conceitual** | Estrutura macro (entidades + relacionamentos)        |
| **Lógico**     | Tabelas, colunas, PKs, FKs, mas sem detalhes do SGBD |
| **Físico**     | Implementação real no SGBD (tipos, constraints, SQL) |


---

## 🧠 Conclusão

O projeto demonstrou o processo completo de construção de um sistema de banco de dados, desde a definição das entidades até sua implementação no SGBD. Foram aplicados conceitos fundamentais como chaves primárias, chaves estrangeiras, restrições de integridade, modelagem de dados e execução prática em ambiente SQL.

A organização do projeto permite fácil expansão, podendo futuramente integrar funcionalidades como gerenciamento de usuários, histórico de garantias, emissão de notas e integração com APIs externas.

Assim, o sistema implementado representa uma base sólida e escalável para aplicações de controle de garantias em ambientes reais.

## 🧾 Créditos

* **Autor:** Pedro Henrique Medeiros
* **Disciplina:** Engenharia de Dados / Banco de Dados
* **Instituição:** Curso_BFD_polo_itaipuaçu_maricá
* **Ferramentas:** DBeaver, PostgreSQL/MySQL, Draw.io, Python

---
