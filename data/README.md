Original data:  
train.csv

Dataset number 1  
File name:  
Only english samples

Three column:  
name_1, name_2, bool_match

Format parquet, compression="brotli"
df.to_parquet()

Libs: pandas, vaex polars, etc  
Quotes should be removed in the names, commas should be left