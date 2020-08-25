
a = input("Please enter the Numerator:")
b = input("Please enter the Denominator:")
try:
    r = int(a) / int(b)
    print('result:', r)
except ValueError as e:
    print('except:', e)
except ZeroDivisionError as e:
    print('except:', e)
else:
    print("No exception!")
finally:
    print('The End')
    
# Please enter the Numerator:2
# Please enter the Denominator:4
# result: 0.5
# No exception!
# The End