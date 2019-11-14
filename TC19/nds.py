def nds(df):
  print(df)
  df['Non Discounted Sales'] = df['Sales'] / (1-df['Discount'])
  return(df)

def get_output_schema():
  return pd.DataFrame({
      'Row ID': prep_int(),
      'Non Discounted Sales': prep_decimal()
  })