# %%
import pandas as pd
from main import df

#%%
df= pd.DataFrame(df)
df.head()

#%%
df['Quantidade'].astype(float).astype(int)


#%%
df['Data'].sample(10)
df["OrdemProducao"].head()

#%%
# replace
df['OrdemProducao'] = df['OrdemProducao'].astype(str)
replace = df['OrdemProducao'].replace("O","").replace("#1#1","")
df["OrdemProducao"]

#%%
df["OrdemProducao"] = df["OrdemProducao"].astype(str).str.replace('O','').str.replace("#1#1","")
df['OrdemProducao']  # o metodo replace faz a mudança de toda uma str enquanto que str.replace muda parte da string dentro da str

#%%
df.rename(columns={"OrdemProducao":"Ordem"},inplace=True)
df.head(2)

#%%
df

# %%
colunas = ['OrdemProducao', 'Data', 'Quantidade']

df = df[colunas]
df
# %%
def get_ordem(ord):
    i= ord.split('#')
    i=i[0]
    i=i.split('O')
    i=i[-1]
    return i

# %%
get_ordem('O1425880#1#1O')

# %%
df
# %%
df['ordem']=df['OrdemProducao'].apply(get_ordem)
df