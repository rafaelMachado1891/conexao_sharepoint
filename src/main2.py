# %%
import pandas as pd
from main import df

# %%
df = pd.DataFrame(df)

#%%
df.shape  # mostra quantas linhas e colunas eu tenho 

#%%
df.columns  # mostra o nome das colunas

# %%

df.info()

# %%
df.info(memory_usage='deep')

# %%
df.dtypes  # mostra uma serie com o tipo de dados de cada coluna

# %% 
df.dtypes["OrdemProducao"]  # retorna o tipo de uma coluna específica

# %%
df.rename(columns={"OrdemProducao": "ordem"}) # renomeia as colunas mas eu preciso atribuir a um novo df

# %%
df

# %%
rename_columns={"OrdemProducao": "ordem"}

# %%
df.rename(columns=rename_columns,inplace=True) #renomeia a coluna e atribui a alteração no data frame

#%%
df.head()

# %%
df[["ordem"]].head()

# %%
df.head(3)

# %%
colunas = list(df.columns)
colunas

#%%
colunas.sort()
colunas

#%%
df = df[colunas]
df.head(1)