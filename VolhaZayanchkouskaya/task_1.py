import threading
from time import sleep

count_philosophers = 5
count_forks = 5

forks = [threading.Lock() for i in range(count_forks)]
philosophers = [i for i in range(count_philosophers)]


def eating(index):
    print(f"Philosopher {philosophers[index]} start to eat!")
    sleep(2)
    print(f"Philosopher {philosophers[index]} finished!")


def dinning_philosophers():
    while True:
        for i in range(len(forks)):
            fork1 = forks[i]
            fork2 = forks[(i + 1) % count_forks]
            fork1.acquire()
            fork2.acquire()
            eating(i)
            fork2.release()
            fork1.release()
            sleep(2)


if __name__ == "__main__":
    dinning_philosophers()





