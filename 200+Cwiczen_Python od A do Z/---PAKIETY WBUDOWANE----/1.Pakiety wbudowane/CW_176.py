from posixpath import split
import re


text = 'Programowanie w języku Python - od A do Z'
result = re.split(pattern=r"\s+", string=text)
print(result)
