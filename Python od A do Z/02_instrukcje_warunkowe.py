# %%
from xml.dom.pulldom import default_bufsize


version = 3.7
print(version)

# %%
version > 3
# %%
version <= 3

# %%
number = 1200
number > 1000

# %%
number == 1200

# %%
number == 1000

# %%
number != 1200

# %%
# if [warunek]:
#    [instrukcje]
# %%
if 8 < 10:
    print('tak ;)')

else:
    print('nie')

# %%
default_flag = True

if not default_flag:
    print('Nie doszło')
else:
    print('Doszło')

# %%
