# %%
import pandas as pd

# %%
df = pd.DataFrame({"nome":["Davi","Rafael","Sophia",
                           "Joao","Maria","Davi","Rafael",
                           "Rafael","Sophia","Joao","Maria"],
                    "gastos":[15,20,30,15,2,7,90,25,13,1,14],
                    "receita":[30,15,35,20,8,13,100,40,33,8,50]})
# %%
df
# %%
df.groupby(by=["nome"]).sum()
# %%
df.groupby(by=["nome"],as_index=False)["gastos"].max()
# %%
df
# %%
#Calculando mais de uma estatítica
df.groupby(by=["nome"],as_index=False).agg(["sum","min","max"])

# %%
df

# %%
df.groupby(by=["nome"],as_index=False)['gastos'].agg(["sum","min","max"])
# %%

# %%
df.groupby(by=["nome"],as_index=False).agg({"gastos": ["sum","min","max"],
                                            "receita":["mean"]})

# %%
summary = df.groupby(by=["nome"],as_index=False).agg({"gastos": ["sum","min","max"],
                                            })
summary
# %%
summary.columns = ['nome','soma_gastos','minimo_gastos','max_pontos'] # definindo o  nome das colunas e modificando o tipo de data frame para não multi index
# %%
summary