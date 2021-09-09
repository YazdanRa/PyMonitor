from pymonitor import monitor


@monitor("time")
def example_function():
    from time import sleep

    sleep(7)

    pass


if __name__ == "__main__":
    example_function()
