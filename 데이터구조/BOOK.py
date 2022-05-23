from numpy import index_exp
import pandas as pd

book_col = ['BOOK_ISBN', 'BOOK_TITLE', 'BOOK_AUTHOR','BOOK_PUB','BOOK_PRICE',
                   'BOOK_LINK','BOOK_IMAGE', 'BOOK_DESCRIPTION', 'BOOK_PRE']
book_table = pd.read_csv('데이터구조\BOOk.csv', names = book_col ,encoding= 'utf-8') #csv파일 

#book_table.to_csv('데이터구조\BOOk.csv',index = False)

print(book_table)