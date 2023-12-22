# block 8
qualified_pair = pd.DataFrame()
pair = result[result['number of differences'] == 3]
pair_df = pd.DataFrame(pair)
for index,row in pair_df.iterrows():
  if 1 not in row['different items']:
    pair_df = pair_df.drop(index)
pair_df.head()
pair_df.to_csv('pairs_differ_by_var1_differ_3.csv')
number_of_pairs = len(pair_df)
print('number of pairs:',' ',number_of_pairs)