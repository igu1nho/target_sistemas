import json
import os

# Construindo o caminho para o arquivo JSON na direto da pasta 'dados'
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo_json = os.path.join(diretorio_atual, '..', 'dados', 'dados.json')

# Carregando o arquivo dos dados do JSON
with open(caminho_arquivo_json, 'r') as f:
    data = json.load(f)

# Filtrando os valores válidos
valores = [item['valor'] for item in data if item['valor'] > 0]

# Calculando os resultados
menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)

# Verificando quais dias possuem valores acima da média
dias_acima_da_media = [item['dia'] for item in data if item['valor'] > media_mensal]

# Exibindo os resultados encontrados
print(f"Menor valor: {menor_valor:.2f}")
print(f"Maior valor: {maior_valor:.2f}")
print(f"Dias acima da média: {dias_acima_da_media}")
