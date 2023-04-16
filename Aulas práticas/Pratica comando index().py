#-------------------------------------==================================-----------------------------------------------#
                                        #Como usar o comando index()


# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

# index of 'i' in alphabets
index = alphabets.index('e')   # output = 1

print('The index of e:', index)

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # output = 6

print('The index of i:', index)

# 'i' between 3rd and 5th index is searched
#index = alphabets.index('i', 3, 5)   # Da um erro! Isso porque não tem nenhum 'i' entre 3 'o' e 5 'l'

#print('The index of i:', index)