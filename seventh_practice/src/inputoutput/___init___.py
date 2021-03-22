def write_to_file(data, filename, mode):
    """
    Write data to file

    Keyword arguments:
    data - data to be written
    filename - path to the file where you want to save the result
    mode - mode of file (t for text or b for binary)
    """
    try:
        f = open(filename, "w" + mode)
    except Exception as exc:
        print(exc)
    f.write(data)
    f.close()


def read_from_file(filename, mode):
    """
    Read binary data from file

    Keyword arguments:
    filename - path to the file where you want to save the result
    mode - mode of file (t for text or b for binary)

    Returns:
    data - data from file
    """
    try:
        f = open(filename, "r" + mode)
    except Exception as exc:
        print(exc)
    data = f.read()
    f.close()
    return data
