# Lista principal para armazenar os pacientes.
# Cada paciente será um DICIONÁRIO dentro desta LISTA.
pacientes = []

def cadastrar_paciente():
    """Função para cadastrar um novo paciente."""
    print("\n--- CADASTRO DE PACIENTE ---")
    nome = input("Nome do paciente: ").strip()
    
    # Tratamento de erro para garantir que a idade seja um número inteiro
    while True:
        try:
            idade = int(input("Idade: "))
            if idade <= 0:
                print("A idade deve ser um número positivo.")
                continue
            break
        except ValueError:
            print("Erro: A idade deve ser um número inteiro válido.")
    
    telefone = input("Telefone: ")
    
    # Criação do dicionário do paciente
    novo_paciente = {
        'nome': nome,
        'idade': idade,
        'telefone': telefone
    }
    
    # Adiciona o dicionário à lista principal
    pacientes.append(novo_paciente)
    print(f"\nPaciente '{nome}' cadastrado com sucesso!")

def ver_estatisticas():
    """Função para calcular e exibir estatísticas básicas."""
    if not pacientes:
        print("\nNão há pacientes cadastrados para gerar estatísticas.")
        return

    total_pacientes = len(pacientes)
    soma_idades = 0
    
    # Inicializa o paciente mais novo/velho com o primeiro da lista
    paciente_mais_novo = pacientes[0]
    paciente_mais_velho = pacientes[0]

    for p in pacientes:
        soma_idades += p['idade']
        
        # Encontra o mais novo
        if p['idade'] < paciente_mais_novo['idade']:
            paciente_mais_novo = p
        
        # Encontra o mais velho
        if p['idade'] > paciente_mais_velho['idade']:
            paciente_mais_velho = p
            
    idade_media = soma_idades / total_pacientes

    print("\n--- ESTATÍSTICAS DA CLÍNICA VIDA+ ---")
    print(f"Número total de pacientes cadastrados: {total_pacientes}")
    print(f"Idade média dos pacientes: {idade_media:.2f} anos")
    print(f"Paciente mais novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos)")

def buscar_paciente():
    """Função para buscar um paciente pelo nome."""
    if not pacientes:
        print("\nNão há pacientes cadastrados.")
        return

    termo_busca = input("\nDigite o nome do paciente que deseja buscar: ").strip().lower()
    encontrados = []
    
    for p in pacientes:
        # Busca case-insensitive
        if termo_busca in p['nome'].lower():
            encontrados.append(p)

    if encontrados:
        print(f"\n--- {len(encontrados)} PACIENTE(S) ENCONTRADO(S) ---")
        for p in encontrados:
            print(f"Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")
    else:
        print(f"\nPaciente com nome '{termo_busca}' não encontrado.")

def listar_todos_pacientes():
    """Função para listar todos os pacientes cadastrados."""
    if not pacientes:
        print("\nNão há pacientes cadastrados para listar.")
        return

    print("\n--- LISTA COMPLETA DE PACIENTES ---")
    for i, p in enumerate(pacientes, 1):
        print(f"{i}. Nome: {p['nome']:<20} | Idade: {p['idade']:>3} | Tel: {p['telefone']}")
    print("-" * 50)


def menu_principal():
    """Menu principal do sistema, rodando em loop."""
    # O loop principal (Requisito: O programa deve funcionar em loop até o usuário escolher sair)
    while True:
        print("\n" + "=" * 25)
        print("=== SISTEMA CLÍNICA VIDA+ ===")
        print("=" * 25)
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")
        
        # Tratamento de erro para a opção do menu
        try:
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                cadastrar_paciente()
            elif opcao == 2:
                ver_estatisticas()
            elif opcao == 3:
                buscar_paciente()
            elif opcao == 4:
                listar_todos_pacientes()
            elif opcao == 5:
                print("\nEncerrando o Sistema Clínica Vida+. Até logo!")
                break # Sai do loop
            else:
                print("\nOpção inválida. Por favor, escolha uma opção entre 1 e 5.")
        
        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número correspondente à opção desejada.")

# Inicia o sistema
if __name__ == "__main__":
    # Popula com dados iniciais para facilitar os testes das estatísticas
    pacientes.append({'nome': 'João Silva', 'idade': 45, 'telefone': '(11) 99999-9999'})
    pacientes.append({'nome': 'Ana Souza', 'idade': 28, 'telefone': '(11) 88888-8888'})
    pacientes.append({'nome': 'Carlos Lima', 'idade': 62, 'telefone': '(21) 77777-7777'})
    
    menu_principal()