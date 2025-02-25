import requests

# Substitua pelo seu token da API
api_token = "e90de56983acf9f206e3fef1412c47033d711f28"

# Lista de cidades a serem pesquisadas
cidades = [
    "São Paulo", "Quebec", "Ontario", "Portugal",
    "Germany", "Greece", "France", "India", "Spain", "Indonesia"
]

dados_qualidade_ar = []

for cidade in cidades:
    url = f"https://api.waqi.info/feed/{cidade}/?token={api_token}"
    response = requests.get(url)
    data = response.json()

    if data.get("status") == "ok":
        aqi = data["data"]["aqi"]

        # Verifica se o AQI é um número válido
        if isinstance(aqi, int):
            print(f"Qualidade do ar em {cidade}: {aqi}")
            dados_qualidade_ar.append((cidade, aqi))
        else:
            print(f"Dados inválidos para {cidade}")
            dados_qualidade_ar.append((cidade, float("inf")))  # Coloca no final do ranking
    else:
        print(f"Erro ao obter dados de {cidade}")
        dados_qualidade_ar.append((cidade, float("inf")))

# Ordena a lista do menor para o maior AQI (melhor para pior qualidade do ar)
dados_qualidade_ar.sort(key=lambda x: x[1])

# Exibe o ranking
print("\nRanking de qualidade do ar:")
for i, (cidade, aqi) in enumerate(dados_qualidade_ar, 1):
    status = "Dado indisponível" if aqi == float("inf") else f"AQI: {aqi}"
    print(f"{i}. {cidade} - {status}")