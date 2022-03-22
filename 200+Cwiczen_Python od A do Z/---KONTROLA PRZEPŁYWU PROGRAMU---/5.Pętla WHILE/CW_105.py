# %%
max_iters = 10000
iters = 0
w_0 = -1
previous_step_size = 1
learning_rate = 0.01
precision = 0.000001
def derivative(w): return 2 * w - 4


w_prew = w_0


while previous_step_size > precision and iters < max_iters:
    w_0 = w_0 - learning_rate * derivative(w_prew)
    w_prew = w_0
    iters += 1

print(f'Minimum lokalne w punkcie: {w_0:.2f}')

# %%
