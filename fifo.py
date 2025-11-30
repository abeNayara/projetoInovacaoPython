def simular_fila_atendimento_interativo():
    """
    Simula a gestão interativa de uma fila de atendimento (FIFO) da Clínica Vida+, 
    permitindo ao usuário inserir os dados dos pacientes.
    """
    
    # Lista Python para simular a fila (Fila = Lista de Dicionários)
    fila_de_pacientes = []
    
    print("\n" + "=" * 40)
    print("=== GESTÃO DE FILA (FIFO) - CLÍNICA VIDA+ ===")
    print("=" * 40)

    # 1. Permite inserir 3 pacientes na fila (Operação: ENFILEIRAR / ENQUEUE)
    print("\n1. INSERINDO 3 PACIENTES NA FILA (Ordem de Chegada):")
    
    for i in range(3):
        print(f"\n--- Cadastro do {i+1}º Paciente ---")
        nome = input("   Nome: ").strip()
        cpf = input("   CPF: ").strip()
        
        # Criação do dicionário do paciente e inserção no final da fila (append)
        novo_paciente = {"nome": nome, "cpf": cpf}
        fila_de_pacientes.append(novo_paciente)
        print(f"   [SUCESSO] Paciente '{nome}' inserido na fila.")
    
    print("-" * 40)

    # 2. Remova o primeiro paciente da fila para atendimento (Operação: DESENFILEIRAR / DEQUEUE)
    print("2. REMOVENDO O PRIMEIRO PACIENTE (FIFO):")
    
    if fila_de_pacientes:
        # Remove o primeiro elemento da lista (índice 0)
        paciente_atendido = fila_de_pacientes.pop(0) 
        print(f"   [ATENDIDO] O paciente '{paciente_atendido['nome']}' foi o primeiro a ser atendido.")
    else:
        print("   A fila está vazia. Nenhum paciente para atender.")
    
    print("-" * 40)

    # 3. Mostre quem ainda está na fila após o primeiro atendimento
    print("3. PACIENTES RESTANTES NA FILA:")
    
    if fila_de_pacientes:
        for i, paciente in enumerate(fila_de_pacientes, 1):
            print(f"   {i}. Nome: {paciente['nome']:<20} | CPF: {paciente['cpf']}")
    else:
        print("   A fila foi esvaziada.")
        
    print("\n--- SIMULAÇÃO CONCLUÍDA ---")

# Executa a simulação
if __name__ == "__main__":
    simular_fila_atendimento_interativo()