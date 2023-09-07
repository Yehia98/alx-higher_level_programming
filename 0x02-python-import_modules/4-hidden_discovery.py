#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    nnames = dir(hidden_4)
    for name in nnames:
        if name[:2] != "__":
            print(name)
