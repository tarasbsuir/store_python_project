''' Main module for internet store. '''


from internet_store import App


def main():
    App().Run()

if __name__ == '__main__':
    print("main.py - run as a standalone program.\n")
    main()
else:
    print("main.py - run as a built-in module.")
