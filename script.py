#!usr/bin/env python3

def gogo():
  print("Hello World!")
  return True

def avg(values:list):
  return sum(values) / len(values)

if __name__=="__main__":
  gogo()
  print(avg([3, 4, 5, 6])
