import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

df=pd.read_csv('primeiro-semestre-2021.csv', encoding = 'utf-8')

#transformando todas as linhas em listas
lista = df.values.tolist()

#criando uma nova lista pegando só as colunas que queremos e adicionando à lista "casos"
casos = []
for item in lista:
  conjunto = [item[61], item [7]]
  casos.append(conjunto)

#zerando os contadores
est = 0
sp, mg, rj, ba, rs, pr, ce, pe, sc, go, df, pa, rn, es, am, pb, ma, ms, pi, al, se, mt, ro, to, ac, ap, rr = [0 for x in range(27)]

#atribuindo casos de estupro por estado
for crime in casos:
  if crime[0] ==  'LIBERDADE>SEXUAL>FÍSICA>ESTUPRO':
    est += 1
    if crime[1] == 'SP':
      sp += 1
    if crime[1] == 'RJ':
      rj += 1
    if crime[1] == 'MG':
      mg += 1
    if crime[1] == 'BA':
      ba += 1
    if crime[1] == 'RS':
      rs += 1
    if crime[1] == 'PR':
      pr += 1
    if crime[1] == 'CE':
      ce += 1
    if crime[1] == 'SC':
      sc += 1
    if crime[1] == 'GO':
      go += 1
    if crime[1] == 'DF':
      df += 1
    if crime[1] == 'PA':
      pa += 1
    if crime[1] == 'RN':
      rn += 1
    if crime[1] == 'ES':
      es += 1
    if crime[1] == 'AM':
      am += 1
    if crime[1] == 'PB':
      pb += 1
    if crime[1] == 'MA':
      ma += 1
    if crime[1] == 'MS':
      ms += 1
    if crime[1] == 'AL':
      al += 1
    if crime[1] == 'SE':
      se += 1
    if crime[1] == 'MT':
      mt += 1
    if crime[1] == 'RO':
      ro += 1
    if crime[1] == 'TO':
      to += 1
    if crime[1] == 'AC':
      ac += 1
    if crime[1] == 'AP':
      ap += 1
    if crime[1] == 'RR':
      rr += 1
    if crime[1] == 'PE':
      pe += 1
    if crime[1] == 'PI':
      pi += 1

# Colocando o nº de casos de estupro por estado na lista "resultado"
resultado = [sp, mg, rj, ba, rs, pr, ce, pe, sc, go, df, pa, rn, es, am, pb, ma, ms, pi, al, se, mt, ro, to, ac, ap, rr]

#=============================================================================================================#

app = Dash(__name__)

# Criando conteúdo para o gráfico - lista com 27 strings = "Denúncias por estado"
string = 'Denúncias por estado'
legenda = []
for i in range(27):
  legenda.append(string)

df = pd.DataFrame({
  "Estado": ['SP', 'MG', 'RJ', 'BA', 'RS', 'PR', 'CE', 'PE', 'SC', 'GO', 'DF', 'PA', 'RN', 'ES', 'AM', 'PB', 'MA', 'MS', 'PI', 'AL', 'SE', 'MT', 'RO', 'TO', 'AC', 'AP', 'RR'],
  "Legenda": legenda,
  "Casos de Estupro": resultado,
})



fig = px.bar(df, x="Estado", y="Casos de Estupro", color="Legenda", barmode="group")
fig.show()

#==========================================================================================================#

app.layout = html.Div(children=[
    html.H1(children='Violência contra a mulher no Brasil'),

    html.Div(children='''
        Casos de estupro por UF e região.
    '''),

    dcc.Dropdown(['Norte', 'Nordeste', 'Sul', 'Sudeste', 'Centro-Oeste', 'Todas as UFs'], value='Todas as UFs', id='demo-dropdown'),

    dcc.Graph(
        id='grafico',
        figure = fig
    )
])

@app.callback(
    Output('grafico', 'figure'),
    Input('demo-dropdown', 'value')
)

def update_output(value):
  if value == "Todas as UFs":
    string = 'Denúncias por estado'
    legenda = []
    for i in range(27):
      legenda.append(string)

    df = pd.DataFrame({
          "Estado": ['SP', 'MG', 'RJ', 'BA', 'RS', 'PR', 'CE', 'PE', 'SC', 'GO', 'DF', 'PA', 'RN', 'ES', 'AM', 'PB', 'MA', 'MS', 'PI', 'AL', 'SE', 'MT', 'RO', 'TO', 'AC', 'AP', 'RR'],
          "Legenda": legenda,
          "Casos de Estupro": resultado,
        })

    fig = px.bar(df, x="Estado", y="Casos de Estupro", color="Legenda", barmode="group")

  elif value == 'Norte':
    string = 'Denúncias por estado'
    legenda = []
    for i in range(7):
      legenda.append(string)
    df = pd.DataFrame({
  "Estado": ['AC', 'AM', 'RO', 'TO', 'PA', 'RR', 'AP'],
  "Legenda": legenda,
  "Casos de Estupro": [ac,am,ro,to,pa,rr,ap],
  })
    fig = px.bar(df, x="Estado", y="Casos de Estupro", color="Legenda", barmode="group")

  elif value == 'Sul':
    string = 'Denúncias por estado'
    legenda = []
    for i in range(3):
      legenda.append(string)
    df = pd.DataFrame({
  "Estado": ['RS', 'PR', 'SC'],
  "Legenda": legenda,
  "Casos de Estupro": [rs, pr, sc],
  })
    fig = px.bar(df, x="Estado", y="Casos de Estupro", color="Legenda", barmode="group")

  elif value == 'Centro-Oeste':
    string = 'Denúncias por estado'
    legenda = []
    for i in range(4):
      legenda.append(string)
    df = pd.DataFrame({
  "Estado": ['MT', 'MS', 'GO', 'DF'],
  "Legenda": legenda,
  "Casos de Estupro": [mt, ms, go, resultado[10]],
  })
    fig = px.bar(df, x="Estado", y="Casos de Estupro", color="Legenda", barmode="group")
  
  elif value == 'Sudeste':
    string = 'Denúncias por estado'
    legenda = []
    for i in range(4):
      legenda.append(string)
    df = pd.DataFrame({
  "Estado": ['MG', 'SP', 'ES', 'RJ'],
  "Legenda": legenda,
  "Casos de Estupro": [mg, sp, es, rj],
  })
    fig = px.bar(df, x="Estado", y="Casos de Estupro", color="Legenda", barmode="group")
    
  elif value == 'Nordeste':
    string = 'Denúncias por estado'
    legenda = []
    for i in range(9):
      legenda.append(string)
    df = pd.DataFrame({
  "Estado": ['MA', 'PI', 'BA', 'SE', 'AL', 'PE', 'PB', 'RN', 'CE'],
  "Legenda": legenda,
  "Casos de Estupro": [ma, pi, ba, se, al, pe, pb, rn, ce],
  })
    fig = px.bar(df, x="Estado", y="Casos de Estupro", color="Legenda", barmode="group")

  return fig
  
if __name__ == '__main__':
    app.run_server(debug=True)