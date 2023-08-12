#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hide_name = dir(hidden_4)
    for i in hide_name:
        if '__' in i:
            continue
        print("{}".format(i))
