# %%
def file_gen(fileList):
    return [file for file in fileList if file.endswith('.txt')]


print(file_gen(['test.txt', 'test.jpg']))

# %%
