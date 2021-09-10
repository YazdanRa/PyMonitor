from pymonitor import monitor


@monitor("time")
def time_example():
    from time import sleep

    sleep(7)


@monitor("time")
@monitor("cpu")
def cpu_example():
    import random
    from time import sleep

    random_list = list()
    for _ in range(10000000):
        random_list.append(random.randint(0, 1000000000))
    sorted(random_list)

    sleep(30)

    random_list = list()
    for _ in range(10000000):
        random_list.append(random.randint(0, 1000000000))
    sorted(random_list)


if __name__ == "__main__":
    # time_example()
    cpu_example()
