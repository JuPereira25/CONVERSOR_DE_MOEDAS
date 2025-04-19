import xmltodict

# Função para tratar o XML
def conversoes_disponiveis():
    with open("Projetos/Conversor de moedas/conversoes.xml", "rb") as arquivo_conversoes:
        dic_conversoes = xmltodict.parse(arquivo_conversoes)

    conversoes = dic_conversoes["xml"]
    dic_conversoes_disponiveis = {}
    for par_conversao in conversoes:
        moeda_origem, moeda_destino = par_conversao.split("-")
        if moeda_origem in dic_conversoes_disponiveis:
            dic_conversoes_disponiveis[moeda_origem].append(moeda_destino)
        else:
            dic_conversoes_disponiveis[moeda_origem] = [moeda_destino]
    return dic_conversoes_disponiveis