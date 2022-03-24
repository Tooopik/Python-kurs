#%%
evenNubers = [str(number)+'\n' for number in range(2, 19) if number % 2 == 0]
evenNubers[-1] = evenNubers[-1][:-1]
with open('num.txt','w') as file:
    file.writelines(evenNubers)

#%%
