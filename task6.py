def maximum(x,y,z):
    if(x >= y) & (x >= z):
      return x
    elif(y >= x) & (y >= z):
        return y
    else:
        return z
