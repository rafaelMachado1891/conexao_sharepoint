#%%
import pandas as pd
#%%

df1 = pd.DataFrame({'transacao': [1,2,3,4,5],
                    'idcliente': [1,2,3,2,2],
                    'valor':[10,45,32,117,87]
                    })

df2= pd.DataFrame({'id':[1,2,3,4],
                   'nome':['Rafael', 'Davi','Sophia','Igor']
                   })

df1
#%%
df2



# %%
df1.merge(df2,left_on=['idcliente'],right_on=['id'],how='inner')