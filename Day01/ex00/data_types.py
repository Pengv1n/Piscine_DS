def data_types():
    print("[{}, {}, {}, {}, {}, {}, {}, {}]".format(type(21).__name__, type("21").__name__, type(21.42).__name__, type(True).__name__, type(list()).__name__, type(dict()).__name__, type(tuple()).__name__, type(set()).__name__))

if __name__ == '__main__':
    data_types()
