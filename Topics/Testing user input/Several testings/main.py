def check(x):
    try:
        x = int(x)
        assert x >= 202
    except ValueError:
        print('It is not a number!')
    except AssertionError:
        print('There are less than 202 apples! You cheated me!')
    else:
        print(x)


# def check(x):
#     if x.isdigit():
#         x = int(x)
#         if x >= 202:
#             print(x)
#         else:
#             print("There are less than 202 apples! You cheated me!")
#     else:
#         print("It is not a number!")