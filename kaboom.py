from threading import Thread
import time
import os

answer = None


def ask():
    global start_time, answer
    start_time = time.time()
    answer = input("Tienes 10 segundos para desactivar la bomba, frente a ti ves 3 cables, uno azul, uno rojo y uno verde, que cable cortas:\n")
    time.sleep(0.001)

def timing():
    time_limit = 8
    while True:
        time_taken = time.time() - start_time
        if answer == "rojo":
            print(f"has logrado desactivar la bomba!! te demoraste", {time_taken}, "segundos")
            os._exit(1)
        if time_taken > time_limit:
            print("kaboom !!! \n"
                  f"te demoraste {time_taken} segundos.")
            os._exit(1)
        time.sleep(0.001)


t1 = Thread(target=ask)
t2 = Thread(target=timing)
t1.start()
t2.start()