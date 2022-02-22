# %%
from re import X


empty_tuple = tuple()

print(empty_tuple)

# %%
amazon = ('Amazon', 'USA', 'Technology', 1)
google = ('Google', 'USA', 'Technology', 2)
# %%
name_google = google[0]

# %%
google[0] = 'Google Company'

# %%
data = (amazon, google)

# %%
print(data)

# %%
a = ('Adrian', 'Wójcik')
print(a)
# %%
imie = 'Adrian'
nazwisko = 'Wójcik'
# %%
imie, nazwisko, id_user = ('Adrian', 'Wójcik', '001')
# %%
amazon_name, country, sector, rank = amazon
# %%
stocks = 'Amazon', 'Apple', 'IBM'
print(type(stocks))

# %%
nested = 'Europa', 'Polska', ('Warszawa', 'Krakow', 'Wroclaw')
print(nested)

# %%
a = 12
b = 14

c = b
b = a
a = c

print(a, b)

# %%
x, y = 10, 15

x, y = y, x

print(x, y)

# %%
