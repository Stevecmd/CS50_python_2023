def main():
    name = input("What's your name? ")
    # hello(name)
    print(hello(name))

def hello(to="world"):
    # print("hello,", to) # doesnt work because we are not returning anything
    return f"hello, {to}"

if __name__ == "__main__":
    main()