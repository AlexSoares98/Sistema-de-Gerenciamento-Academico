import time # Biblioteca para adicionar pequenas pausas entre as opções do Menu 
import json # Biblioteca para trabalhar e salvar com arquivos em JSON 

# Listas para armazenar os dados 
estudantes = []
professores = []
disciplinas = []
turmas = []
matriculas = []

# Função para carregar dados de arquivos JSON
def carregar_arquivos(sistema):
    try:
        with open(sistema, 'r', encoding='utf-8') as arquivo:
            cadastro_pronto = json.load(arquivo)
        return cadastro_pronto
    except FileNotFoundError:
        return None

# Função para salvar dados em arquivos JSON
def salvar_arquivo(lista, sistema):
    with open(sistema, 'w', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False)

# Estrutura do Menu Principal 
def menu_principal():
    print("----- MENU PRINCIPAL -----\n")
    print("(1) Gerenciar Estudantes")
    print("(2) Gerenciar Professores")
    print("(3) Gerenciar Disciplinas")
    print("(4) Gerenciar Turmas")
    print("(5) Gerenciar Matrículas")
    print("(0) Sair\n")
    # Coletando a opção desejada pelo usuário.
    try:
        opcao_principal = int(input("Digite o número da opção desejada: "))
    except ValueError:
        # Mostrando "opção inválida" caso o valor digitado não seja um número 
        print("\nVocê digitou uma opção INVÁLIDA, digite novamente!\n")
        time.sleep(0.5)
        return None
    return opcao_principal

# Estrutura do Menu de Operações 
def menu_de_operacoes(opcao_desejada):
    print(f"\n----- MENU DE OPERAÇÕES -----\nGerenciar {opcao_desejada}:\n")
    print("(1) Incluir")
    print("(2) Listar")
    print("(3) Atualizar")
    print("(4) Excluir")
    print("(5) Voltar ao menu principal\n")
    try:
        opcao_operacoes = int(input("Digite o número da opção desejada: "))
    except ValueError:
        print("\nVocê digitou uma opção INVÁLIDA, digite novamente!\n")
        time.sleep(0.5)
        return None
    return opcao_operacoes

# Estrutura da Opção Incluir um cadastro de Professor ou Estudante 
def incluir_prof_e_estudantes(lista, sistema, grupo):
    lista = carregar_arquivos(sistema) or []
    print("\n----- Incluir -----\n")
    # Coletando as informações de cadastro do professor e estudante 
    while True:
        try:
            codigo = int(input(f"Digite o código do {grupo}: "))
            nome = input(f"Digite o nome do {grupo}: ")
            cpf = input(f"Digite o CPF do {grupo}: ")
        except ValueError:
        # Mostrando "opção inválida" caso o valor digitado não seja um número 
            print("\nVocê digitou uma opção INVÁLIDA, digite novamente!\n")
            time.sleep(0.5)
            continue
        cadastro_grupo = {
            "codigo": codigo,
            "nome": nome,
            "cpf": cpf
        }
        lista.append(cadastro_grupo) # Adicionando o nome do estudante à lista  
        salvar_arquivo(lista, sistema)
        print(f"{grupo} {nome.strip()} (Código: {codigo}), adicionado com sucesso!")
        break

# Estrutura de listagem das informações cadastradas 
def listar(lista, sistema, grupo):
    lista = carregar_arquivos(sistema)
    time.sleep(0.5)
    if not lista:
        print(f"\n----- Lista de {grupo} -----\nNão há {grupo} cadastrados!")
    # Apresentando a lista de cadastrados 
    else:
        print(f"\n----- Lista de {grupo} -----\n")
        for dados in lista:
            if grupo == "Turmas":
                print(f"- Código: {dados['turma']} - Professor (Código): {dados['professor']} - Disciplina (Código): {dados['disciplina']}")
            elif grupo == "Estudantes" or grupo == "Professores":
                print(f"- Código: {dados['codigo']} - Nome: {dados['nome'].strip()}")
            elif grupo == "Disciplinas":
                print(f"- Código: {dados['codigo']} - Nome: {dados['nome'].strip()}")
            elif grupo == "Matrículas":
                print(f"- Matrícula: {dados['matricula']} - Turma: {dados['turma']} - Estudante: {dados['estudante']}") 

# Estrutura da Opção atualização de cadastro de professores e alunos 
def atualizar_prof_e_estudantes(lista, sistema, grupo):
    time.sleep(0.5)
    lista = carregar_arquivos(sistema) or []
    # Mensagem caso ainda não tenha estudantes cadastrados 
    if not lista:
        print(f"\n----- Atualizar {grupo} -----\nNão há {grupo} cadastrados!")
    # Apresentando os estudante e professores cadastrados
    else:
        print(f"\n----- Atualizar {grupo} -----\n")
        for dados in lista:
            print(f"- Código: {dados['codigo']} - Nome: {dados['nome'].strip()} - CPF: {dados['cpf'].strip()}")
        print("\n------------------------------")
        while True:
            # Armazenando o código referente ao estudante ou professor para atualizar as informações 
            try:
                codigo_atualizado = int(input(f"\nDigite o código do {grupo} que deseja atualizar (0 para retornar ao Menu): "))
            except ValueError:
                # Mostrando "opção inválida" caso o valor digitado não seja um número 
                print("\nVocê digitou uma opção INVÁLIDA, digite novamente!\n")
                time.sleep(0.5)
                continue
            grupo_atualizado = None # Nova lista para armazenar os dados do estudante ou professor 
            for dados in lista:
                if dados['codigo'] == codigo_atualizado:
                    grupo_atualizado = dados
                    break
            if codigo_atualizado == 0: # Opção para retornar ao Menu de Operações  
                break 
            # Coletando os dados atualizados do estudante ou professor e armazenando na lista 
            elif grupo_atualizado:
                try:
                    novo_codigo = int(input(f"\nDigite o novo código do {grupo}: "))
                except ValueError:
                    print("\nVocê digitou uma opção INVÁLIDA, digite novamente!\n")
                    time.sleep(0.5)
                    continue
                novo_nome = input(f"Digite o novo nome do {grupo}: ").strip()
                novo_cpf = input(f"Digite o novo CPF do {grupo}: ").strip()
                grupo_atualizado["codigo"] = novo_codigo
                grupo_atualizado["nome"] = novo_nome
                grupo_atualizado["cpf"] = novo_cpf
                salvar_arquivo(lista, sistema)
                print(f"\n{grupo} {novo_nome.strip()} (Código: {novo_codigo}), atualizado com sucesso!")
                break
            else:
                print(f"\n{grupo} não encontrado, digite novamente!") # Mensagem caso não seja encontrada o cadastro 
                continue

# Estrutura da Opção exclusão de cadastro 
def excluir(lista, sistema, grupo):
    time.sleep(0.5)
    lista = carregar_arquivos(sistema) or []
    # Mensagem caso ainda não tenha cadastros 
    if not lista:
        print(f"\n----- Excluir {grupo} -----\nNão há {grupo} cadastrados!")
    # Mostrando ao usuário as opções de cadastros para iniciar a exclusão  
    else:
        print(f"\n----- Excluir {grupo} -----\n")
        for dados in lista:
            if grupo == "Estudantes" or grupo == "Professores":
                print(f"- Código: {dados['codigo']} - Nome: {dados['nome'].strip()}")
            elif grupo == "Disciplinas":
                print(f"- Código: {dados['codigo']} - Nome: {dados['nome'].strip()}")
            elif grupo == "Turmas":
                print(f"- Código: {dados['turma']} - Professor: {dados['professor']} - Disciplina: {dados['disciplina']}")
            elif grupo == "Matrículas":
                print(f"- Matrícula: {dados['matricula']} - Turma: {dados['turma']} - Estudante: {dados['estudante']}")
        print("\n------------------------------")
        while True: 
             # Coletando o código que o usuário deseja excluir 
            try:
                if grupo == "Matrículas":
                    codigo_excluido = int(input(f"\nDigite o código da matrícula que deseja excluir (0 para retornar ao Menu): "))
                elif grupo == "Turmas":
                    codigo_excluido = int(input(f"\nDigite o código da turma que deseja excluir (0 para retornar ao Menu): "))
                else:
                    codigo_excluido = int(input(f"\nDigite o código do {grupo} que deseja excluir (0 para retornar ao Menu): "))
            except ValueError:
                print("\nVocê digitou uma opção INVÁLIDA, digite novamente!\n") # Mostrando "opção inválida" caso o valor digitado não seja um número  
                time.sleep(0.5)
                continue

            grupo_excluido = None # Armazenando os dados digitados na lista do grupo de excluídos 
            for dados in lista:
                if grupo == "Estudantes" or grupo == "Professores":
                    if dados['codigo'] == codigo_excluido:
                        grupo_excluido = dados
                        break
                elif grupo == "Disciplinas":
                    if dados['codigo'] == codigo_excluido:
                        grupo_excluido = dados
                        break
                elif grupo == "Turmas":
                    if dados['turma'] == codigo_excluido:
                        grupo_excluido = dados
                        break
                elif grupo == "Matrículas":
                    if dados['matricula'] == codigo_excluido:
                        grupo_excluido = dados
                        break

            if codigo_excluido == 0:
                break
            elif grupo_excluido:
                lista.remove(grupo_excluido) # Removendo o estudante excluído da lista de estudantes 
                salvar_arquivo(lista, sistema)
                if grupo == "Turmas":
                    print(f"\nTurma {grupo_excluido['turma']} excluída com sucesso!")
                elif grupo == "Matrículas":
                    print(f"\n{grupo[:-1]} {grupo_excluido['matricula']} (Turma: {grupo_excluido['turma']}), excluída com sucesso!")
                else:
                    print(f"\n{grupo} {grupo_excluido['nome'].strip()} (Código: {grupo_excluido['codigo']}), excluído com sucesso!")
                break
            else:
                print(f"\n{grupo} não encontrada, digite novamente!")
                continue

# Estrutura para Incluir Disciplina 
def incluir_disciplina(lista, sistema):
    time.sleep(0.5)
    lista = carregar_arquivos(sistema) or []
    print("\n----- Incluir Disciplinas -----\n")
    # Armazenando o código referente a disciplina para atualizar as informações 
    while True: 
        try:
            codigo_novo = int(input("Digite o código da disciplina que deseja adicionar: "))
        except ValueError:
            # Mostrando "opção inválida" caso o valor digitado não seja um número 
            print("\nVocê digitou um código INVÁLIDO, digite novamente!\n")
            time.sleep(0.5)
            continue
        codigo_existente = False
        for disciplina in lista:
            if disciplina['codigo'] == codigo_novo:
                codigo_existente = True
                break
        if codigo_existente:
            print(f"Disciplina com código {codigo_novo} já existe.") # Mensagem apresentada para um código existente 
            continue
        disciplina = input("Informe o nome da Disciplina: ")
        dicionario_disciplina = {
            "codigo": codigo_novo,
            "nome": disciplina
        }
        lista.append(dicionario_disciplina) # Salvando o dicionário em Lista 
        salvar_arquivo(lista, sistema)
        print(f"\nDisciplina {disciplina.strip()} adicionada com sucesso!\n")
        break

# Estrutura para Atualizar Disciplina
def atualizar_disciplina(lista, sistema):
    time.sleep(0.5)
    lista = carregar_arquivos(sistema) or []
    if not lista:
        # Mensagem caso ainda não tenha disciplinas cadastradas 
        print("\n----- Atualizar Disciplinas -----\nNão há Disciplinas cadastradas!")
    else:
        # Apresentando as disciplinas cadastrados 
        print(f"\n----- Atualizar Disciplinas -----\n")
        for disciplinas in lista:
            print(f"- Código: {disciplinas['codigo']} - Nome: {disciplinas['nome'].strip()}")
        print("\n------------------------------")
        while True:
            try:
                codigo_atualizado = int(input(f"\nDigite o código da disciplina que deseja atualizar (0 para retornar ao Menu): "))
            except ValueError:
                print("\nVocê digitou um código INVÁLIDO, digite novamente!\n")
                time.sleep(0.5)
                continue
            disciplina_atualizada = None
            for disciplina in lista:
                if disciplina['codigo'] == codigo_atualizado:
                    disciplina_atualizada = disciplina
                    break
            if codigo_atualizado == 0: # Opção para retornar ao Menu de Operações 
                break
            elif disciplina_atualizada:
                try:
                    novo_codigo = int(input("\nDigite o novo código da disciplina: ")) # Coletando o novo código para atualização da disciplina 
                except ValueError:
                    print("\nVocê digitou um código INVÁLIDO, digite novamente!\n") # Mensagem para valor digitado incorreto 
                    time.sleep(0.5)
                    continue
                novo_nome = input("Digite o novo nome da disciplina: ").strip()
                disciplina_atualizada["codigo"] = novo_codigo
                disciplina_atualizada["nome"] = novo_nome
                salvar_arquivo(lista, sistema)
                print(f"Disciplina {novo_nome.strip()} (Código: {codigo_atualizado}), atualizada com sucesso!")
                break
            else:
                print("Disciplina não encontrada, digite novamente!") # Mensagem caso o código digitado não for encontrado 
                continue

# Estrutura para Incluir Matrícula 
def incluir_matricula(lista, sistema):
    time.sleep(0.5)
    lista = carregar_arquivos(sistema) or []
    print("\n----- Incluir Matrículas -----\n")
    # Armazenando o código referente a inclusão da nova matrícula 
    while True:
        try:
            nova_matricula = int(input("Digite o código da matrícula que deseja adicionar: "))
        except ValueError:
            print("\nVocê digitou um código INVÁLIDO, digite novamente!\n") # Mensagem caso o código digitado seja incorreto 
            time.sleep(0.5)
            continue
        matricula_existente = False
        for matricula in lista:
            if matricula['matricula'] == nova_matricula:
                matricula_existente = True
                break
        if matricula_existente:
            print(f"Matricula com código {nova_matricula} já existe.") # Mensagem caso o código digitado já exista 
            continue
        try:
            turma = int(input("Informe o código da turma: "))
            estudante = int(input("Informe o código do estudante: "))
        except ValueError:
            print("\nVocê digitou um código INVÁLIDO, digite novamente!\n") # Mensagem caso o código digitado seja incorreto 
            time.sleep(0.5)
            continue
        dicionario_matricula = {
            "matricula": nova_matricula,
            "turma": turma,
            "estudante": estudante
        }
        lista.append(dicionario_matricula) # Adicionando a nova matrícula na Lista 
        salvar_arquivo(lista, sistema)
        print(f"\nMatrícula {nova_matricula} adicionada com sucesso!\n")
        break

# Estrutra para Atualizar Matrícula
def atualizar_matricula(lista, sistema):
    time.sleep(0.5)
    lista = carregar_arquivos(sistema) or []
    if not lista:
        print(f"\n----- Atualizar Matrículas -----\nNão há Matrículas cadastradas!") # Mensagem caso ainda não tenho cadastro de matrículas 
    else:
        print(f"\n----- Atualizar Matrículas -----\n")
        for matricula in lista:
            print(f"- Matrícula: {matricula['matricula']} - Turma: {matricula['turma']}") # Apresentando as matrículas cadastradas para opção de atualização 
        print("\n------------------------------") 
        # Coletando o código referente a matrícula que o usuário deseja cadastrar 
        while True:
            try:
                matricula_atualizada = int(input(f"\nDigite o código da matrícula que deseja atualizar (0 para retornar ao Menu): "))
            except ValueError:
                print("\nVocê digitou um código INVÁLIDO, digite novamente!\n") # Mensagem caso o código digitado seja incorreto 
                time.sleep(0.5)
                continue
            matricula_atualizada_lista = None
            for matricula in lista:
                if matricula['matricula'] == matricula_atualizada:
                    matricula_atualizada_lista = matricula
                    break
            if matricula_atualizada == 0:
                break
            elif matricula_atualizada_lista:
                # Coletando as informação para atualização de matrícula 
                try:
                    matricula_atualizada_lista["matricula"] = int(input("Digite o novo código de matrícula: "))
                    matricula_atualizada_lista["turma"] = int(input("Digite o novo código de turma: "))
                    matricula_atualizada_lista["estudante"] = int(input("Digite o novo código de estudante: "))
                except ValueError:
                    print("\nVocê digitou um código INVÁLIDO, digite novamente!\n") # Mensagem caso o código digitado seja incorreto 
                    time.sleep(0.5)
                    continue
                salvar_arquivo(lista, sistema)
                print(f"\nMatrícula: ({matricula_atualizada}), atualizada com sucesso!")
                break
            else:
                print(f"\nMatrícula não encontrada, digite novamente!") # Mensagem caso a matrícula não tenha sido encontrada 
                continue

# Estrutura para Incluir Turmas
def incluir_turmas(lista, sistema):
    time.sleep(0.5)
    lista = carregar_arquivos(sistema) or []
    print("\n----- Incluir Turmas -----\n") 
    # Coletando o código para inclusão de novas turmas 
    while True:
        try:
            nova_turma = int(input("Digite o código da turma que deseja adicionar: "))
        except ValueError:
            print("\nVocê digitou um código INVÁLIDO, digite novamente!\n") # Mensagem caso o código digitado seja incorreto  
            time.sleep(0.5)
            continue
        turma_existente = False
        for turma in lista:
            if turma['turma'] == nova_turma:
                turma_existente = True
                break
        if turma_existente:
            print(f"Turma {nova_turma} já existe.") # Mensagem caso o código da turma já esteja cadastrado 
            continue
        # Coletando as informação para inclusão de uma nova turma 
        try:
            professor = int(input("Informe o código do professor: "))
            disciplina = int(input("Informe o código da disciplina: "))
        except ValueError:
            print("\nVocê digitou um código INVÁLIDO, digite novamente!\n") # Mensagem caso o código digitado seja incorreto   
            time.sleep(0.5)
            continue
        dicionario_grupo = {
            "turma": nova_turma,
            "professor": professor,
            "disciplina": disciplina
        }
        print(f"\nTurma {nova_turma} adicionada com sucesso!\n")
        lista.append(dicionario_grupo) # Adicionando a nova turma na Lista  
        salvar_arquivo(lista, sistema)
        break

# Estrutura para Atualizar Turmas
def atualizar_turmas(lista, sistema):
    time.sleep(0.5)
    lista = carregar_arquivos(sistema) or []
    if not lista:
        print(f"\n----- Atualizar Turmas -----\nNão há Turmas cadastradas!") # Mensagem caso ainda não tenho cadastro de turmas 
    else:
        print(f"\n----- Atualizar Turmas -----\n")
        for nova_turma in lista:
            print(f"- Código da Turma: {nova_turma['turma']}") # Apresentando as opção de turmas cadastradas para atualização 
        print("\n------------------------------")
        # Coletando o código para atualização de novas turmas 
        while True:
            try:
                turma_atualizada = int(input(f"\nDigite o código da turma que deseja atualizar (0 para retornar ao Menu): "))
            except ValueError:
                print("\nVocê digitou um código INVÁLIDO, digite novamente!\n") # Mensagem caso o código digitado seja incorreto   
                time.sleep(0.5)
                continue
            turma_atualizada_lista = None
            for turma in lista:
                if turma['turma'] == turma_atualizada:
                    turma_atualizada_lista = turma
                    break
            if turma_atualizada == 0:
                break
            elif turma_atualizada_lista:
                # Coletando as novas informações / códigos da turma a ser atualizada 
                try:
                    turma_atualizada_lista["turma"] = int(input("Digite o novo código de turma: "))
                    turma_atualizada_lista["professor"] = int(input("Digite o novo código do professor da turma: "))
                    turma_atualizada_lista["disciplina"] = int(input("Digite o novo código da disciplina: "))
                except ValueError:
                    print("\nVocê digitou um código INVÁLIDO, digite novamente!\n") # Mensagem caso o código digitado seja incorreto   
                    time.sleep(0.5)
                    continue
                salvar_arquivo(lista, sistema)
                print(f"Turma {turma_atualizada_lista['turma']} atualizada com sucesso!")
                break
            else:
                print(f"Turma não encontrada, digite novamente!") # Mensagem caso o código digitado não esteja cadastrado 
                continue

# Execução do sistema partindo do Menu Principal
while True:
    opcao_principal = menu_principal()
    if opcao_principal == 1: 
        opcao_desejada = "Estudantes" 
        # Apresentando as opções escolhidas pelo usuário no menu de Operações para Estudante 
        while True:
            opcao_estudante = menu_de_operacoes(opcao_desejada)
            if opcao_estudante == 1:
                incluir_prof_e_estudantes(estudantes, "estudantes.json", "Estudantes")
            elif opcao_estudante == 2:
                listar(estudantes, "estudantes.json", "Estudantes")
            elif opcao_estudante == 3:
                atualizar_prof_e_estudantes(estudantes, "estudantes.json", "Estudantes")
            elif opcao_estudante == 4:
                excluir(estudantes, "estudantes.json", "Estudantes")
            elif opcao_estudante == 5:
                print("\nRetornando ao menu principal...\n")
                time.sleep(0.5)
                break
            else:
                print("\nVocê digitou uma opção INVÁLIDA, digite novamente!") # Mensagem caso o valor digitado seja incorreto 
                time.sleep(0.5)

    elif opcao_principal == 2:
        opcao_desejada = "Professores" 
        # Apresentando as opções escolhidas pelo usuário no menu de Operações para Professores 
        while True:
            opcao_professores = menu_de_operacoes(opcao_desejada)
            if opcao_professores == 1:
                incluir_prof_e_estudantes(professores, "professores.json", "Professores")
            elif opcao_professores == 2:
                listar(professores, "professores.json", "Professores")
            elif opcao_professores == 3:
                atualizar_prof_e_estudantes(professores, "professores.json", "Professores")
            elif opcao_professores == 4:
                excluir(professores, "professores.json", "Professores")
            elif opcao_professores == 5:
                print("\nRetornando ao menu principal...\n")
                time.sleep(0.5)
                break
            else:
                print("\nVocê digitou uma opção INVÁLIDA, digite novamente!") # Mensagem caso o valor digitado seja incorreto  
                time.sleep(0.5)

    elif opcao_principal == 3:
        opcao_desejada = "Disciplinas" 
        # Apresentando as opções escolhidas pelo usuário no menu de Operações para Disciplinas  
        while True:
            opcao_disciplinas = menu_de_operacoes(opcao_desejada)
            if opcao_disciplinas == 1:
                incluir_disciplina(disciplinas, "disciplinas.json")
            elif opcao_disciplinas == 2:
                listar(disciplinas, "disciplinas.json", "Disciplinas")
            elif opcao_disciplinas == 3:
                atualizar_disciplina(disciplinas, "disciplinas.json")
            elif opcao_disciplinas == 4:
                excluir(disciplinas, "disciplinas.json", "Disciplinas")
            elif opcao_disciplinas == 5:
                print("\nRetornando ao menu principal...\n")
                time.sleep(0.5)
                break
            else:
                print("\nVocê digitou uma opção INVÁLIDA, digite novamente!") # Mensagem caso o valor digitado seja incorreto 
                time.sleep(0.5)

    elif opcao_principal == 4:
        opcao_desejada = "Turmas" 
        # Apresentando as opções escolhidas pelo usuário no menu de Operações para Turmas  
        while True:
            opcao_turmas = menu_de_operacoes(opcao_desejada)
            if opcao_turmas == 1:
                incluir_turmas(turmas, "turmas.json")
            elif opcao_turmas == 2:
                listar(turmas, "turmas.json", "Turmas")
            elif opcao_turmas == 3:
                atualizar_turmas(turmas, "turmas.json")
            elif opcao_turmas == 4:
                excluir(turmas, "turmas.json", "Turmas")
            elif opcao_turmas == 5:
                print("\nRetornando ao menu principal...\n")
                time.sleep(0.5)
                break
            else:
                print("\nVocê digitou uma opção INVÁLIDA, digite novamente!") # Mensagem caso o valor digitado seja incorreto  
                time.sleep(0.5)

    elif opcao_principal == 5:
        opcao_desejada = "Matrículas" 
        # Apresentando as opções escolhidas pelo usuário no menu de Operações para Matrículas  
        while True:
            opcao_matricula = menu_de_operacoes(opcao_desejada)
            if opcao_matricula == 1:
                incluir_matricula(matriculas, "matriculas.json")
            elif opcao_matricula == 2:
                listar(matriculas, "matriculas.json", "Matrículas")
            elif opcao_matricula == 3:
                atualizar_matricula(matriculas, "matriculas.json")
            elif opcao_matricula == 4:
                excluir(matriculas, "matriculas.json", "Matrículas")
            elif opcao_matricula == 5:
                print("\nRetornando ao menu principal...\n")
                time.sleep(0.5)
                break
            else:
                print("\nVocê digitou uma opção INVÁLIDA, digite novamente!") # Mensagem caso o valor digitado seja incorreto 
                time.sleep(0.5)

    elif opcao_principal == 0: # Opção para encerramento do sistema 
        break
    else:
        print("\nVocê digitou uma opção INVÁLIDA, digite novamente!\n") # Mensagem caso o valor digitado seja incorreto 
        time.sleep(0.5)
        continue
print("\nEncerrando o sistema...\n")
time.sleep(0.5)
print("Obrigado, volte sempre!") # Mensagem de encerramento 


