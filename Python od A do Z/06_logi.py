# %%
import datetime
import time


def log(message, dt=datetime.datetime.utcnow()):
    print(dt, message)


def logi(*args):
    for comand in args:
        log(comand)
        time.sleep(1)


logi('Uruchomienie sytemu', 'Logowanie', 'Restart', 'Wylogowanie')

# %%
