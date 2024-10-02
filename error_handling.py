import random

number_list = [random.randint(-2, 2) for _ in range(3)]
# przeiterować po liczbach w zakresie 50-60 ze skokiem 1

# for number in range(50, 61):
#     print(number)

# kazda z rangea podzielić przez kazda z number_list


class CustomError(Exception):
    pass


for number in range(50, 61):
    for listed_number in number_list:
        try:
            # print("byle co"/7)
            raise CustomError("zepsulo sie","i nie działa")
            print(f'{number}:{listed_number}={number/listed_number}')
        except ZeroDivisionError:
            print("Division by zero")
        except CustomError as e:
            print(e.args)
        finally:
            print("finally here")
