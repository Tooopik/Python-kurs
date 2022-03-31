y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]


def mse(y_true, y_pred):
    return round(sum([(i[1] - i[0])**2 for i in zip(y_true, y_pred)]) / len(y_true), 3)
