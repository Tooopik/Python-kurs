# %%
import os
# %%
print(dir(os))
# %%
os.getcwd()
# %%
os.listdir()
# %%
for item in os.listdir():
    if item.endswith('.py'):
        print(item)

# %%
for root, dirs, files in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    print(files)

# %%
os.path.join(r'home\user\bin', 'python')

# %%
