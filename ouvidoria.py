from operacoesbd import *
from biblioouvidoria import *

conn = criarConexao("localhost","root","12345","universidade_xyz")

opcao = 0

while opcao != 7:

    print("\n1. Listar manifestações\n2. Listar manifestações por tipo\n3. Criar manifestação\n4. Exibir quantiade de manifestações\n5. Visualizar manifestação pelo código\n6. Excluir manifestação por código\n7. Sair ")

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:

        print(f"\n{"="*80} Manifestações {"="*80}\n")

        #Reclamações
        reclamacoes = listarReclamacoes(conn)

        #Sugestoes
        sugestoes = listarSugestoes(conn)

        #Elogios
        elogios = listarElogios(conn)

        #SE o tamanho de todas as listas for 0 então não tem manifestações
        if len(reclamacoes) == 0 and len(sugestoes) == 0 and len(elogios) == 0:
            print("Sem manifestações.")


        else:
            #SE o tamanho de reclamacoes for 0
            if len(reclamacoes) == 0:
                print("Sem reclamações.")

            #SE tiver informação
            else:
                for manifestacoes in reclamacoes:
                    print(f"- {manifestacoes[0]} - Nome: {manifestacoes[1]} - Assunto: {manifestacoes[2]}")

            print("="*100)

            #SE o tamanho de sugestões for 0
            if len(sugestoes) == 0:
                print("Sem sugestões.")

            #SE tiver informação
            else:
                for manifestacoes in sugestoes:
                    print(f"- {manifestacoes[0]} - Nome: {manifestacoes[1]} - Assunto: {manifestacoes[2]}")

            print("="*100)

            #SE o tamanho de elogios for 0
            if len(elogios) == 0:
                print("Sem elogios.")

            #SE tiver informação
            else:
                for manifestacoes in elogios:
                    print(f"- {manifestacoes[0]} - Nome: {manifestacoes[1]} - Assunto: {manifestacoes[2]}")

    #Listando por tipo
    elif opcao == 2:
        while True:
            print(f"\n{"=" * 80} Manifestações por tipo {"=" * 80}")

            print("\n1. Reclamações\n2. Sugestões\n3. Elogios\n4. Sair")

            #Variável para adentrar no menu requerido
            acaoNecessaria = int(input("Digite sua opção: "))

            #SE for 1 ele lista reclamações
            if acaoNecessaria == 1:
                print(f"\n{"=" * 80} Reclamações {"=" * 80}\n")

                # Reclamações
                reclamacoes = listarReclamacoes(conn)

                if len(reclamacoes) == 0:
                    print("Sem reclamações.")

                else:
                    # Listando reclamações
                    for manifestacoes in reclamacoes:
                        print(f"- {manifestacoes[0]} - Nome: {manifestacoes[1]} - Assunto: {manifestacoes[2]}")

            #SE for 2 ele lista sugestões
            elif acaoNecessaria == 2:
                print(f"\n{"=" * 80} Sugestões {"=" * 80}\n")

                # Sugestoes
                sugestoes = listarSugestoes(conn)

                if len(sugestoes) == 0:
                    print("Sem sugestões.")

                else:
                    for manifestacoes in sugestoes:
                        print(f"- {manifestacoes[0]} - Nome: {manifestacoes[1]} - Assunto: {manifestacoes[2]}")

            #SE for 3 ele lista elogios
            elif acaoNecessaria == 3:
                print(f"\n{"=" * 80} Elogios {"=" * 80}\n")

                # Elogios
                elogios = listarElogios(conn)

                if len(elogios) == 0:
                    print("Sem elogios.")

                else:
                    for manifestacoes in elogios:
                        print(f"- {manifestacoes[0]} - Nome: {manifestacoes[1]} - Assunto: {manifestacoes[2]}")

            #SE for 4 sai
            elif acaoNecessaria == 4:
                break

            #SE for uma ação inválida
            else:
                print("Ação inválida.")

    #SE for 3 lista manifestações
    elif opcao == 3:

        while True:
            print(f"\n{"=" * 80} Adicionar manifestação {"=" * 80}")

            print("\n1. Reclamações\n2. Sugestões\n3. Elogios\n4. Sair")

            #Variável para ação
            acaoNecessaria = int(input("Digite sua opção: "))

            #SE for 1 adiciona reclamação
            if acaoNecessaria == 1:
                print(f"\n{"=" * 80} Adicionar reclamação {"=" * 80}\n")

                nome = input("Digite seu nome: ")
                assunto = input("Digite o assunto: ")
                reclamacao = input("Digite sua reclamação: ")

                inserindoReclamacoes = inserirReclamacoes(conn,nome,assunto,reclamacao)

                print(f"\nReclamação registrada com o código: {inserindoReclamacoes}.\n")

            #SE for 2 adiciona sugestão
            elif acaoNecessaria == 2:
                print(f"\n{"=" * 80} Adicionar sugestão {"=" * 80}\n")

                nome = input("Digite seu nome: ")
                assunto = input("Digite o assunto: ")
                sugestao = input("Digite sua sugestão: ")

                inserindoSugestoes = inserirSugestoes(conn,nome,assunto,sugestao)

                print(f"\nSugestão registrada com o código: {inserindoSugestoes}.")

            #SE for 3 adiciona elogio
            elif acaoNecessaria == 3:
                print(f"\n{"=" * 80} Adicionar elogio {"=" * 80}\n")

                nome = input("Digite seu nome: ")
                assunto = input("Digite o assunto: ")
                elogio = input("Digite seu elogio: ")

                inserindoElogios = inserirElogios(conn,nome,assunto,elogio)

                print(f"\nElogio registrado com o código: {inserindoElogios}.")

            #Saindo
            elif acaoNecessaria == 4:
                break

            else:
                print("Ação inválida.")

    #SE for igual a 4 mostra a quantidade das manifestações
    elif opcao == 4:
        print(f"\n{"=" * 80} Quantidade de manifestações {"=" * 80}\n")

        #Verificando tamanhos das manifestações
        tamanhoReclamacoes = len(listarReclamacoes(conn))
        tamanhoSugestoes = len(listarSugestoes(conn))
        tamanhoElogios = len(listarElogios(conn))
        #Fazendo soma das manifestações
        totalManifestacoes = tamanhoReclamacoes +tamanhoSugestoes + tamanhoElogios

        print(f"Atualmente temos {tamanhoReclamacoes} reclamação(ões).")

        print("="*100)

        print(f"Atualmente temos {tamanhoSugestoes} sugestão(ões).")

        print("=" * 100)

        print(f"Atualmente temos {tamanhoElogios} elogio(s).")

        print("=" * 100)

        print(f"No total temos {totalManifestacoes} manifestação(ões).")

    #SE for igual a 5 pesquisa-se pelo código
    elif opcao == 5:

        while True:
            print(f"\n{"=" * 80} Pesquisar manifestações {"=" * 80}")

            print("\n1. Reclamações\n2. Sugestões\n3. Elogios\n4. Sair")
            #Variável para ação
            acaoNecessaria = int(input("Digite sua opção: "))

            #SE for 1 adiciona reclamação
            if acaoNecessaria == 1:
                codigo = int(input("Digite o código de sua reclamação: "))

                listarReclamacao = listarCodigoReclamacoes(conn, codigo)

                #SE o tamanho da lista for 0
                if len(listarReclamacao) == 0:
                    print("Código inválido.")

                #SE tiver informações ele mostra
                else:
                    print(f"\n{"=" * 80} Reclamação de {listarReclamacao[0][1]} {"=" * 80}\n")

                    print(f"Nome: {listarReclamacao[0][1]}\nAssunto: {listarReclamacao[0][2]}\nReclamação: {listarReclamacao[0][3]}")

            elif acaoNecessaria == 2:
                codigo = int(input("Digite o código de sua sugestão: "))

                listarSugestao = listarCodigoSugestoes(conn, codigo)

                #SE não tiver informações
                if len(listarSugestao) == 0:
                    print("Código inválido.")

                #SE tiver
                else:
                    print(f"\n{"=" * 80} Sugestão de {listarSugestao[0][1]} {"=" * 80}\n")

                    print(f"Nome: {listarSugestao[0][1]}\nAssunto: {listarSugestao[0][2]}\nReclamação: {listarSugestao[0][3]}")

            elif acaoNecessaria == 3:
                codigo = int(input("Digite o código de seu elogio: "))

                listarElogio = listarCodigoElogios(conn,codigo)

                #SE não tiver informação
                if len(listarElogio) == 0:
                    print("\nCódigo inválido.")

                #SE tiver
                else:
                    print(f"\n{"=" * 80} Elogio de {listarElogio[0][1]} {"=" * 80}\n")

                    print(f"Nome: {listarElogio[0][1]}\nAssunto: {listarElogio[0][2]}\nReclamação: {listarElogio[0][3]}")

            #Saindo
            elif acaoNecessaria == 4:
                break

           #Ação inválida
            else:
                print("\nAção inválida.")

    #SE a opção for 6 vai excluir por código
    elif opcao == 6:
        while True:

            print(f"\n{"=" * 80} Excluir manifestações {"=" * 80}")

            print("\n1. Reclamações\n2. Sugestões\n3. Elogios\n4. Sair")

            acaoNecessaria = int(input("Digite sua opção: "))

            #SE for 1 vai excluir reclamações
            if acaoNecessaria == 1:
                codigo = int(input("Digite o código da reclamação que deseja excluir: "))

                excluirReclamacao = excluirReclamacoes(conn,codigo)

                #SE não tiver uma reclamação com o codigo
                if excluirReclamacao == 0:
                    print("\nExclusão malsucedida. Código inválido.")

                else:
                    print(f"\nExclusão da reclamação {codigo} realizada com sucesso.")

            #SE for 2 exclui sugestões
            elif acaoNecessaria == 2:
                codigo = int(input("Digite o código da sugestão que deseja excluir: "))

                excluirSugestao = excluirSugestoes(conn,codigo)

                #SE não tiver sugestão com o código
                if excluirSugestoes == 0:
                    print("\nExclusão malsucedida. Código inválido.")

                else:
                    print(f"\nExclusão da sugestão {codigo} realizada com sucesso.")

            #SE for 3 exclui elogios
            elif acaoNecessaria == 3:
                codigo = int(input("Digite o código da sugestão que deseja excluir: "))

                excluirElogio = excluirElogios(conn,codigo)

                #SE não tiver elogio com o código
                if excluirElogio == 0:
                    print("\nExclusão malsucedida. Código inválido.")

                else:
                    print(f"\nExclusão da sugestão {codigo} realizada com sucesso.")

            #Saindo
            elif acaoNecessaria == 4:
                break

            else:
                print("\nAção inválida.")

    else:
        print("\nOpção inválida.")

print("\nObrigado por utilizar nossa ouvidoria!")

encerrarConexao(conn)
