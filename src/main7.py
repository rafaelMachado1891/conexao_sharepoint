#Agregações
# %%
import pandas as pd

df = pd.DataFrame({"nome": ["Rafael", "Davi","Sophia","Ismael","Tiago"],
                   "Idade":[36,12,2,40,38],
                   "Salario":[7600,1200,400,5000,5000]})

# %%
colunas = ['Idade', 'Salario']

df[colunas].mean()


# %%
df
# %%
df['Idade'].mean()
# %%
df['Idade'].mean()

# %%
df
# %%
#df.dtypes[~(df.dtypes=="object")].index.to_list()
colunas = df.dtypes[df.dtypes!="object"].index.tolist() #selecionando as colunas numericas

# %%
df[colunas].sum()
df[colunas].describe()