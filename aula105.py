import sys

if 'win' in sys.platform:
    import windsound

print(sys.platform)



print(sys.path)


try:
    raise IndexError
except:
    print(sys.exc_info())
