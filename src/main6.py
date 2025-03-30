#%%
import pandas as pd
#%%
df = pd.DataFrame({"id":['rj-375-abc',
                         'rb-375-def',
                         'rb-375-ghi',
                         'rb-375-jkl',
                         'rb-375-mno',
                         'rb-375-pqr']})
df
# %%
def get_list(x):
    return x.split('-')[-1]

get_list('rj-375-abc')

# %%
df
# %%
df['id'].apply(get_list)
# %%
df['novo_id']=df['id'].apply(get_list)
df