x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
print(u'\u2500' * 50)
def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)
print(u'\u2500' * 50)
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
print(u'\u2500' * 50)
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
