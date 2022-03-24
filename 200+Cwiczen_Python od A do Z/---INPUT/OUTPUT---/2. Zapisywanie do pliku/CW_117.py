#%%
headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]
users.insert(0,headers)
with open('users.csv', 'w') as file:
    for record in users:
        file.write(record[0]+','+record[1]+'\n')

#--------------------------------------------
# %%
    headers = ['user_id', 'amount']
    users = [['001', '1400'], ['004', '1300'], ['007', '900']]
     
    with open('users.csv', 'w') as file:
        file.write(','.join(headers) + '\n')
        for user in users:
            file.write(','.join(user) + '\n')