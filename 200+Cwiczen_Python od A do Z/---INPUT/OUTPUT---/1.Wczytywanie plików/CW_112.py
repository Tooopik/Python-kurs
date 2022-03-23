#%%
try:
    with open('plw_d.csv', 'r') as file:
        content = file.read().splitlines()

    result = {}
    days = []
    close = []
    for idx, data in enumerate(content):
        #print(data.split(','))
        if idx >0:
            days.append(data.split(',')[0])
            close.append(float(data.split(',')[-2]))
    result['Data'] = days
    result['Zamkniecie'] = close
    print(result)
        
except FileNotFoundError:
    print('Nie znaleziono pliku')
# %%
#------------------------------------------------------------------------------
    with open('plw_d.csv', 'r') as file:
        content = file.read().splitlines()
     
    data = [(line.split(',')[0], line.split(',')[4]) for line in content]
    result = {
        data[0][0]: [data[1:][i][0] for i in range(len(data) - 1)],
        data[0][1]: [float(data[1:][i][1]) for i in range(len(data) - 1)]
        }
    print(result)