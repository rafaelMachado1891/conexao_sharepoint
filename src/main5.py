# %%
import pandas as pd
# %%
df = pd.DataFrame({"nome": ['Rafael', 'Davi','Sophia','Davi','Miguel'],
                  "Sobrenome":['Machado','Leite', 'Ayres','Leite','Furlan'],
                  "Salario":[7600,5000,500,3000,4000]
                  })

df
# %%
df.drop_duplicates() # removendo duplicatas por padrão exclui o ultimo registro

# %%
df.drop_duplicates(keep='last', subset=['nome','Sobrenome']) # keep mantém o ultimo ou primeiro registro

# %%
df
# %%
df = (df.sort_values('Salario', ascending=False)
        .drop_duplicates(keep='first',subset=['nome', 'Sobrenome']))
df

