is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}

result = is_clicked.intersection(is_bought)

print(f'ID klientów: {result}')
