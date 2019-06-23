def division(a, b):
    try:
        return a / float(b)
    except ZeroDivisionError:
        return 1