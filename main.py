import customtkinter
from pegar_moedas import conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

customtkinter.set_appearance_mode("dark") # cor de fundo
customtkinter.set_default_color_theme("dark-blue") # tons personalizados conforme a cor de fundo, padrão do tkinter

app = customtkinter.CTk() # abre a janela do programa 
app.geometry("300x500") # definir o pixels, largura e altura

dic_conversoes_disponiveis = conversoes_disponiveis() # dicionario recebendo a função

# Texto 
title = customtkinter.CTkLabel(app, text="Conversor de Moeda", font=("Gotham Bold",20)) 
texto_moeda_origem = customtkinter.CTkLabel(app, text="Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(app, text="Selecione a moeda de destino")

texto_valor = customtkinter.CTkLabel(app, text="Digite o valor a converter")
entrada_valor = customtkinter.CTkEntry(app)

texto_cotacao_moeda = customtkinter.CTkLabel(app, text="")

# Função para carregar as conversões disponiveis
def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(app, values=list(dic_conversoes_disponiveis.keys()), command=carregar_moedas_destino)
campo_moeda_destino = customtkinter.CTkOptionMenu(app, values=["Selecione uma moeda de origem"])

# Função para converter os valores digitado pelo usuário
def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    valor = entrada_valor.get()

    if moeda_origem and moeda_destino and valor:
        try:
            valor = float(valor)
            cotacao = float(pegar_cotacao_moeda(moeda_origem, moeda_destino))
            valor_convertido = valor * cotacao
            texto_cotacao_moeda.configure(
                text=f"{valor:.2f} {moeda_origem} = {valor_convertido:.2f} {moeda_destino}"
            )
        except ValueError:
            texto_cotacao_moeda.configure(text="Digite um valor numérico válido.")
    else:
        texto_cotacao_moeda.configure(text="Preencha todos os campos.")

button_converter = customtkinter.CTkButton(app, text="Converter",command=converter_moeda)

# organizar os elementos na interface
title.pack(padx=10, pady=10)
texto_valor.pack(padx=10, pady=10)
entrada_valor.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10, pady=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10, pady=10)
button_converter.pack(padx=10,pady=10)
texto_cotacao_moeda.pack(padx=10, pady=10)

app.mainloop() # Rodar o app
