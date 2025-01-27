# -*- coding: utf-8 -*-
"""Flight analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nCuyLWZs-aOgkB_1VuT22nC9E60E0R8m
"""

# importação do pandas
import pandas as pd

# url de leitura dos dados
url_dados = 'https://rukbat.eic.cefet-rj.br/data/flights/raw/VRA2019.CSV'

# carga do dataset através do csv
data = pd.read_csv(url_dados, delimiter=';', quotechar='"')

# exibe as primeiras linhas do dataset
data.head()

# importação matplot
import matplotlib.pyplot as plt

# Converte a coluna de datas de string para o formato de data
data['dt_partida_prevista'] = pd.to_datetime(data['dt_partida_prevista'])
data['dt_partida_real'] = pd.to_datetime(data['dt_partida_real'])
data['dt_chegada_prevista'] = pd.to_datetime(data['dt_chegada_prevista'])
data['dt_chegada_real'] = pd.to_datetime(data['dt_chegada_real'])

# Extrai o mês de cada data
data['mes_partida'] = data['dt_partida_prevista'].dt.month
data['mes_chegada'] = data['dt_chegada_prevista'].dt.month

# Verifica se há o atrazo (data prevista for diferente de data real) em uma variável booleana (true ou false)
data['atrazo_partida'] = data['dt_partida_prevista'] != data['dt_partida_real']
data['atrazo_chegada'] = data['dt_chegada_prevista'] != data['dt_chegada_real']

# Calcula a média de atrasos por mês
media_atrasos_chegada_por_mes = data.groupby('mes_partida')['atrazo_partida'].mean()
media_atrasos_partida_por_mes = data.groupby('mes_chegada')['atrazo_chegada'].mean()

# Cria um gráfico de barras para visualizar a média de atrasos de partida por mês
plt.bar(media_atrasos_partida_por_mes.index, media_atrasos_partida_por_mes.values)
plt.xlabel('Mês')
plt.ylabel('Média de Atrasos')
plt.title('Média de Atrasos de Partidas de Voos por Mês em 2019')
plt.xticks(range(1, 13), ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.show()

# Cria um gráfico de barras para visualizar a média de atrasos de chegada por mês
plt.bar(media_atrasos_chegada_por_mes.index, media_atrasos_chegada_por_mes.values)
plt.xlabel('Mês')
plt.ylabel('Média de Atrasos')
plt.title('Média de Atrasos de Chegadas de Voos por Mês em 2019')
plt.xticks(range(1, 13), ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.show()

# Calcula o número total de atrasos de partida e chegada no ano todo
total_atrasos_partida = data['atrazo_partida'].sum()
total_atrasos_chegada = data['atrazo_chegada'].sum()

# Exibe os resultados
print(f"Total de Atrasos de Partida em 2019: {total_atrasos_partida}")
print(f"Total de Atrasos de Chegada em 2019: {total_atrasos_chegada}")

# Filtra os voos que saíram no horário correto
voos_horario_correto = data[(data['atrazo_partida'] == False) & (data['atrazo_chegada'] == False)]

# Calcula a contagem de voos no horário correto por mês
contagem_horario_correto_por_mes = voos_horario_correto.groupby('mes_partida').size()

# Cria o gráfico de barras para visualizar a contagem de voos no horário correto por mês
plt.bar(contagem_horario_correto_por_mes.index, contagem_horario_correto_por_mes.values)
plt.xlabel('Mês')
plt.ylabel('Número de Voos no Horário Correto')
plt.title('Número de Voos no Horário Correto por Mês em 2019')
plt.xticks(range(1, 13), ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.show()

# Filtra os voos que saíram no horário correto
voos_horario_correto = data[(data['atrazo_partida'] == False) & (data['atrazo_chegada'] == False)]

# Calcula o número de voos que saíram no horário correto
numero_voos_horario_correto = len(voos_horario_correto)

print(f"Número de Voos no Horário Correto: {numero_voos_horario_correto}")

# Calcula o número de voos que saíram no horário correto
numero_voos_horario_correto = len(voos_horario_correto)

# Calcula o número total de voos com atraso
numero_voos_atraso = total_atrasos_partida + total_atrasos_chegada

# Rótulos e tamanhos para o gráfico de pizza
labels = ['No Horário Correto', 'Com Atraso']
sizes = [numero_voos_horario_correto, numero_voos_atraso]
colors = ['green', 'red']

# Cria o gráfico de pizza
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Proporção entre Voos no Horário Correto e Voos com Atraso em 2019')
plt.show()

#cria um gráfico de barras para definir atrasos versus justicativas

import pandas as pd
import matplotlib.pyplot as plt

# Dados fictícios de exemplo para demonstração
data = pd.DataFrame({
    'justification_description': ['RA', 'AT', 'WO', 'XN', 'RA', 'AT', 'AT', 'WO', 'TD', 'MX', 'N/A', 'N/A', 'AT', 'AT', 'HD', 'HD', 'MX']
})

# Interpretar as siglas com base nas suposições
interpretations = {
    'RA': 'Rampa / Atividades na Rampa',
    'AT': 'Problemas Técnicos / Manutenção',
    'WO': 'Meteorologia / Condições Climáticas',
    'XN': 'Cancelamento de Voo',
    'TD': 'Atraso de Tráfego Aéreo',
    'MX': 'Manutenção / Problemas Técnicos',
    'HD': 'Problemas com Tripulação / Equipe',
    'N/A': 'Não Aplicável / Não Disponível'
}

# Contar as ocorrências de cada justificativa
justification_counts = data['justification_description'].value_counts()

# Ordenar as justificativas de acordo com as suposições
justification_counts = justification_counts.reindex(list(interpretations.keys()))

# Plotar o gráfico de barras
plt.figure(figsize=(10, 6))
plt.barh(justification_counts.index, justification_counts.values, color='skyblue')
plt.xlabel('Número de Ocorrências')
plt.ylabel('Justificativa para Atraso')
plt.title('Número de Ocorrências de Justificativas para Atrasos de Voos')
plt.yticks(list(interpretations.keys()), [interpretations[justification] for justification in list(interpretations.keys())])
plt.show()

"""# Nova seção"""



