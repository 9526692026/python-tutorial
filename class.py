class NagativeNumberError(Exception):
    pass
def check_number(num):
    if num < 0 :
        raise NagativeNumberError("negativenumber are not allowesd")
    else:
        print(f"result is {num}")
try:
        check_number(10)
except NagativeNumberError as a:
        print(a)

  
  