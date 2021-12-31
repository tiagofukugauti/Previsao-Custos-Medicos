# Projeto - Data App - Previsão do Preço de Convênio Médico

# Imports
import pandas as pd
import numpy as np
import streamlit as st
import pickle
from PIL import Image
#import SessionState
import warnings
warnings.filterwarnings("ignore")


# Inicia a Sessão
#sessao = SessionState.get(run_id=0)
#slider_element = st.empty()


# Define o título do Dashboard
st.title("PROJETO - DATA APP")
st.title("Previsão do Preço de Convênio Médico")

st.sidebar.title('Dados do Cliente')

# Nome do usuário
usuario = st.sidebar.text_input("Digite seu nome")

# Escrevendo o nome do usuário
st.write("Cliente:", usuario)

# Variaveis de entrada
Idade = st.sidebar.slider("Informe a sua idade",16, 90, 16)
Diabetes = st.sidebar.slider('Possui Diabetes? (0= Não    1= Sim)', 0, 1, 0)
Problema_Pressao = st.sidebar.slider('Tem Problema de Pressão? (0= Não    1= Sim)', 0, 1, 0)
Transplantes = st.sidebar.slider("Fez algum tipo de transplante? (0= Não    1= Sim)", 0, 1, 0)
Doencas_Cronicas = st.sidebar.slider('Possui Doenças Crônicas? (0= Não    1= Sim)', 0, 1, 0)
Altura = st.sidebar.slider("Informe sua altura (cm)", 120, 220, 120)
Peso = st.sidebar.slider("Informe seu peso (kg)", 30, 150, 30)
Alergias = st.sidebar.slider ("Possui Alergias? (0= Não    1= Sim)", 0, 1, 0)
Historico_Cancer_Familia = st.sidebar.slider ("Possui histórico de câncer na família? (0= Não    1= Sim)", 0, 1, 0)
Qtd_Cirurgias = st.sidebar.slider ("Quantidade de cirurgias realizadas", 0, 10, 0)

# Dicionário para receber informações
dados_usuario = {'Idade': Idade,

				'Diabetes': Diabetes,

				'Problema_Pressao': Problema_Pressao,

				'Transplantes': Transplantes,

				'Doencas_Cronicas': Doencas_Cronicas,

				'Altura': Altura,

				'Peso': Peso,

				'Alergias': Alergias,

				'Historico_Cancer_Familia': Historico_Cancer_Familia,

				'Qtd_Cirurgias': Qtd_Cirurgias

				}

variaveis = pd.DataFrame(dados_usuario, index=['>'])

linha1 = ['Idade', 'Diabetes', 'Problema_Pressao', 'Transplantes', 'Doencas_Cronicas', 'Altura']
linha2 = ['Peso', 'Alergias', 'Historico_Cancer_Familia', 'Qtd_Cirurgias']

df_linha1 = variaveis[linha1]
df_linha2 = variaveis[linha2]


st.subheader('Visualização dos Dados')
st.write(df_linha1)
st.write(df_linha2)


# Prepara os dados para as previsões
dados_novo_cliente = [Idade, Diabetes, Problema_Pressao, Transplantes, Doencas_Cronicas, Altura, Peso, Alergias, Historico_Cancer_Familia, Qtd_Cirurgias]

# Reshape
novo_cliente = np.array(dados_novo_cliente).reshape(1, -1)


# Faz as previsões (botão)
if st.button('Calcular o Preço'):


# Carrega o modelo
	modelo_v10_final = pickle.load(open('PREVISAO_FINAL.sav', 'rb')) 
	st.write("Preço previsto para o Convênio: R$ %.2f" % (modelo_v10_final.predict(novo_cliente)))
	
	
	st.button("Nova Consulta")
  	#sessao.run_id += 1
	#slider_element.slider("Slide me!", 0, 100, key=session.run_id)

    







