##Original data:  
train.csv

##Dataset number 1  
File name:  train.parquet
Only english samples

Three column:  
name_1, name_2, bool_match

Format parquet, compression="brotli"

Libs: pandas, csv, langdetect, spacy, numpy, etc
Quotes removed in the names, commas left


##Dataset number 2 
File name:  all_lang_train.parquet
All samples

Three column:  
name_1, name_2, bool_match

Format parquet, compression="brotli"

Libs: pandas, csv, langdetect, spacy, numpy, etc
Quotes removed in the names, commas left

##Dataset number 3
File name:  languages.parquet
Append company names from column 'name_2' to column 'name_1' and detecting the language of each name

Two column:  
names, languages_langdetect

Format parquet, compression="brotli"

Libs: pandas, csv, langdetect, spacy, numpy, etc
Quotes removed in the names, commas left
