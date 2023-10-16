def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

# To avoid calling the main function all the time and enable importing
# this function to other programs, we will perform the following check

if __name__ == "__main__":
    main()

# Running this program returns hello, world and goodbye, world