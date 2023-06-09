import pandas as pd

# Dados de exemplo
comentarios = [
    "Adorei o atendimento! Muito profissionais.",
    "Não gostei do produto. Qualidade muito ruim.",
    "O serviço foi excelente. Recomendo!",
    "Demoraram muito para entregar. Péssimo serviço.",
    "Ótimo atendimento ao cliente. Voltarei a comprar.",
]

sentimentos = [
    "positivo",
    "negativo",
    "positivo",
    "negativo",
    "positivo",
]

# Criar DataFrame
dados = pd.DataFrame({"comentario": comentarios, "sentimento": sentimentos})

# Salvar em um arquivo CSV
dados.to_csv("dados_clientes.csv", index=False)