def palindrome(x):
    texto = str(x)
    #transformei int em string 

    if texto == texto[::-1]:
        #slicing faz eu comparar o texto só que ao contrário
        return True
    else:
        return False