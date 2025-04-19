## Conversor de Moeda ##
Este é um conversor de moeda desenvolvido com Python usando a biblioteca customtkinter para a interface gráfica. 
O aplicativo permite que o usuário selecione a moeda de origem e permite que o usuário converta um valor entre essas moedas.

![image](https://github.com/user-attachments/assets/b4aea255-886f-4397-b2f9-28e4ea50d0a4)

## Funcionalidades ##

   ° Conversão de Moeda: 

   ° Seleção de Moeda de Origem e Destino: 

   ° Visualização da Conversão: 

## Requisitos ##
Para rodar este projeto, você precisará do Python 3.11.2 e das seguintes bibliotecas:

customtkinter: Biblioteca para a interface gráfica.

requests: Usada para fazer requisições HTTP para obter as cotações de moedas.

xmltodict: Usada para ler e parsear arquivos XML de conversões disponíveis.

Você pode instalar as dependências necessárias usando o pip:

$$ pip install customtkinter $$
$$ pip install requests $$
$$ pip install xmltodict $$

## Estrutura do Projeto ##

<pre> ```text Conversor de Moeda/
│
├── main.py               # Arquivo principal do aplicativo
├── pegar_moedas.py       # Funções para carregar as moedas disponíveis
├── pegar_cotacao.py      # Função para obter a conversao da moeda via API
└──  conversoes.xml        # Arquivo XML com as conversões disponíveis
```</pre>

## Como Funciona ## 
1. Inserir um valor:
   O usuário insere um valor para converter.

2. Escolher a moeda:
  O aplicativo usa a API da AwesomeAPI para fazer a conversão atual entre a moeda de origem e a moeda de destino.

3. Converter Valores:
  O usuário pode converter um valor entre as moedas selecionadas. A conversão é realizada com base na cotação exibida e o resultado é mostrado na interface.

## Contribuições ##
Sinta-se à vontade para contribuir com melhorias para este projeto. Se encontrar algum erro ou desejar adicionar funcionalidades extras, basta enviar uma pull request.
