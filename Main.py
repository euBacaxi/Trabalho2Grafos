from TableFunction import TableFunction

arquivo = ''
while arquivo != '0':
    print("\nOpções: ( TOY.csv, SJM.csv, QUI.csv, CJM.csv)")
    arquivo = input("Informe o arquivo (0 para sair ): ")
    if arquivo == "0":
        break
    
    g1 = TableFunction(adj_list=[], node_list=[])
    g1.le_arquivo("Anexo/"+arquivo)
    g1.adiciona_aresta()
    tabela = g1.exibe_csv("Anexo/"+arquivo)
    aux = g1.caminho_critico()
    print("\n",tabela)

    print("\nProcessando...")

    print("\nCaminho Crítico:")
    for i in range(len(aux[2])):
        print('-',aux[2][i])
    print("\nTempo Mínimo: ", end="")
    print(aux[0])

