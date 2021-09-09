from pymonitor import monitor


@monitor()
def example_function():

    pass


if __name__ == "__main__":
    example_function()
