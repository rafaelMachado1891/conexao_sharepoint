# %%
import pandas as pd
from main import df

# %%
df = pd.DataFrame(df)

#%%
df.head(3)
df
#%%
df['Quantidade'].sort_values()

#%%
df.sort_values('Quantidade')

#%%
df.sort_values(by="Quantidade",ascending=False).head(1)

#%%

colunas = ['OrdemProducao', 'Data', 'Hora', 'TipoMovimento', 'TipoSaida',
                  'Quantidade', 'DataSaida', 'HoraSaida', 'Celula']

#%%
df = df[colunas]
df.head()



