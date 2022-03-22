# %%
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 3
start = 0
end = len(numbers) - 1
flag = None

while start <= end:
    mid = int((start + end) / 2)
    if numbers[mid] == target:
        flag = True
        break
    else:
        if numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

if flag == True:
    print('Znaleziono')
else:
    print('Nie znaleziono')

# %%
