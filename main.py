from internet_store import App


''' Main module for internet store. '''


def main():
    App().Run()

if __name__ == '__main__':
    print("main.py - run as a standalone program.\n")
    main()
else:
    print("main.py - run as a built-in module.")
