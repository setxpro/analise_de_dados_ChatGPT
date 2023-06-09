import pandas as pd
import openai
from openai_api_key import openai_api_key

# Carregar o conjunto de dados
dados = pd.read_csv('dados_clientes.csv')

# Inicializar o ChatGPT
openai.api_key = openai_api_key
chatGPT = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Você é um analista de sentimentos."},
        {"role": "system", "content": "Comentário: [comentário] Sentimento: [sentimento]"},
    ]
)

# Função para analisar o sentimento do comentário
def analisar_sentimento(comentario):
    # Definir o contexto com o comentário
    chatGPT['messages'][1]['content'] = f"Comentário: {comentario} Sentimento: "
    
    # Gerar a resposta do modelo
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chatGPT['messages']
    )
    
    # Obter o sentimento da resposta do modelo
    sentimento = resposta.choices[0]['message']['content'].strip().lower()
    
    return sentimento

# Analisar os sentimentos dos comentários
dados['sentimento_analisado'] = dados['comentario'].apply(analisar_sentimento)

# Exibir os resultados
print(dados)