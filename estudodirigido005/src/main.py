
from models.loja import Loja
from models.equipamento import Equipamento
from models.garantia import Garantia


loja_model = Loja()
equip_model = Equipamento()
g_model = Garantia()

def menu():
    while True:
        print("\n=== SISTEMA DE GERENCIAMENTO DE GARANTIAS ===")
        print("1 - Cadastrar Loja")
        print("2 - Listar Lojas")
        print("3 - Cadastrar Equipamento")
        print("4 - Listar Equipamentos")
        print("5 - Cadastrar Garantia")
        print("6 - Listar Garantias")
        print("0 - Sair")

        op = input("Opção: ")

        if op == "1":
            nome = input("Nome: ")
            cnpj = input("CNPJ (14 dígitos): ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            loja_model.criar(nome, cnpj, endereco, telefone)

        elif op == "2":
            lojas = loja_model.listar()
            for l in lojas:
                print(l)

        elif op == "3":
            nome = input("Nome do equipamento: ")
            num_serie = input("Número de série: ")
            valor = float(input("Valor: "))
            id_loja = int(input("ID da loja: "))
            equip_model.criar(nome, num_serie, valor, id_loja)

        elif op == "4":
            eqs = equip_model.listar()
            for e in eqs:
                print(e)

        elif op == "5":
            id_eq = int(input("ID do equipamento: "))
            inicio = input("Data início (AAAA-MM-DD): ")
            fim = input("Data fim (AAAA-MM-DD): ")
            tipo = input("Tipo: ")
            desc = input("Descrição: ")
            g_model.criar(id_eq, inicio, fim, tipo, desc)

        elif op == "6":
            garantias = g_model.listar()
            for g in garantias:
                print(e)

        elif op == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":

    from database import inicializar_banco

inicializar_banco()

menu()