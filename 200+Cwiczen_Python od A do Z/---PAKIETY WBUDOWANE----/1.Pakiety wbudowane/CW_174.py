import re


string = '!@#$%^&45wc'
alpha = re.findall(pattern=r'\w', string=string)
print(alpha)
