import requests
import pandas as pd

# Escolha o agregado (exemplo: 1419 = Projeção População)
AGREGADO_ID = 1419  

url = f"https://servicodados.ibge.gov.br/api/v3/agregados/{AGREGADO_ID}/periodos/all/variaveis/all?localidades=N1[all]"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Flatten JSON (cada item de data[0]['resultados'] contém variáveis e séries)
    resultados = []
    for resultado in data[0]["resultados"]:
        variavel = resultado["variavel"]
        for serie in resultado["series"]:
            localidade = serie["localidade"]["nome"]
            for periodo, valor in serie["serie"].items():
                resultados.append({
                    "Variavel": variavel,
                    "Localidade": localidade,
                    "Periodo": periodo,
                    "Valor": valor
                })

    df = pd.DataFrame(resultados)
    df.to_csv(f"ibge_agregado_{AGREGADO_ID}.csv", index=False, encoding="utf-8")

    print(f"✅ Data saved to ibge_agregado_{AGREGADO_ID}.csv")
else:
    print("❌ Error:", response.text[:200])
