import re


raw_text = "Wyślij email na adres: info@template.com lub sales-info@template.it"
emails = re.findall(pattern=r'[\w\.-]+@[\w\.-]+', string=raw_text)
print(emails)
