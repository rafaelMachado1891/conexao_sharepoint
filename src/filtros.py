# %%
import pandas as pd
from main import df

# %%
df = pd.DataFrame(df).head()
df

# %%
filtro = df['Quantidade'] == 300
df[filtro]

#%%
df
# %%
filtro2 = (df['Quantidade'] > 200) & (df['Quantidade'] <= 300)
df[filtro2]


#%%
df['novaquantidade'] = df["Quantidade"] * 100  # adicionando novas coluanas
df 
# %%
# ordenação
df.sort_values(['Quantidade'])

# %%
df.sort_values(by='Quantidade',ascending=False)

# %%
type(df.sort_values('Quantidade'))

