class ValueLargerThanExpected(Exception):
    pass

while True:
    try:
        num=int(input())
        if num>200:
            raise ValueLargerThanExpected
    except ValueError:
        print("Please enter an integer.")
    except ValueLargerThanExpected:
        print("Value larger than expected.")

