import pandas as pd 
from partial_var import partial_var as pv

final_df1 = pd.DataFrame()
final_df1 = pd.concat([final_df1, pv.df], ignore_index=True)
final_df = final_df1.copy()
