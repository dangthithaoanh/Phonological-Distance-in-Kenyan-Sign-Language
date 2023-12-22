#block 9
qualified_pair_2 = pd.DataFrame()
pair_2 = result[result['number of differences'] == 3]
pair_df_2 = pd.DataFrame(pair)
pair_df_2.head()

for index,row in pair_df_2.iterrows():
  if 1 not in row['different items']:
    pair_df_2 = pair_df_2.drop(index)

pair_df_2_copy = pair_df_2.copy(deep=True)

for index2,row in pair_df_2.iterrows():
    gloss1_name = pair_df_2['gloss1'].loc[index2]
    gloss2_name = pair_df_2['gloss2'].loc[index2]
    indices_gloss1 = df[df['Gloss 1'] == gloss1_name].index
    indices_gloss2 = df[df['Gloss 1'] == gloss2_name].index
    result_list_gloss1 = data.iloc[indices_gloss1, 2:].values.tolist()
    result_list_gloss2 = data.iloc[indices_gloss2, 2:].values.tolist()
    if result_list_gloss1[0][0] != "B" and result_list_gloss2[0][0] != "B":
      pair_df_2 = pair_df_2.drop(index2)
pair_df_2_copy.head()
pair_df_2_copy.to_csv('pairs_differ_by_var1_differ_3e.csv')
number_of_pairs = len(pair_df_2_copy)
print('number of pairs:',' ',number_of_pairs)
