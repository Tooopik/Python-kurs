#%%
def fill_value(height=1, width=1, value=1):
    array = [[value for i in range(width)] for ii in range(height)]
    return array

print(fill_value(3,3,100))
#-----------------------------------------------------------------------
# %%
    def fill_value(height, width, value):
        return [[value] * width for i in range(height)]