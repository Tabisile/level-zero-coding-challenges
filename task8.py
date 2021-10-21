def conv_to_hours_and_min(x):
    x_as_integer = int(x)
    x_as_string = str(x_as_integer)
    x_as_integer1 = int(x//60)
    x_as_string1 =  str(x_as_integer1)
    x_as_integer2 = int(x % 60)
    x_as_string2 = str(x_as_integer2)
    if x == 1:
      print(x_as_string + " minute")
    elif(x > 1) & (x < 60):
      print(x_as_string + "minutes")
    elif x / 60 == 1:
      print("1 hour")
    elif x % 60 == 0:
      x_as_int = int(x/60)
      x_as_str = str(x_as_int)
      print(x_as_str + " hours")
    elif(x // 60 == 1) & (x % 60 == 1):
      print(x_as_string1 + " hour," + x_as_string2 + " minute")
    elif x // 60 == 1
      print(x_as_string1 + " hour," + x_as_string2 + " minutes")
    elif(x // 60 > 1) & (x % 60 ==1):
      print(x_as_string1 + " hours," + x_as_string2 + " minute")
    elif(x // 60 > 1) & (x % 60 > 1):
      print(x_as_string1 = " hours," + x_as_string2 + " minutes")
