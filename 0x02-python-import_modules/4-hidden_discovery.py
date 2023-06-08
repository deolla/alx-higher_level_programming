#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    tags = dir(hidden_4)
    for n in tags:
        if n[:2] != "__":
            print(n)
