import getopt, sys

try:
    nb_1 = int(sys.argv[1])
    nb_2 = int(sys.argv[2])
except ValueError:
    print("InputError: Only numbers\n\nUsage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
    sys.exit()
except IndexError:
    print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
    sys.exit()

if len(sys.argv) > 3:
    print("InputError: Too many arguments\n\nUsage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
    sys.exit()
    
sum = nb_1 + nb_2
diff = nb_1 - nb_2
prod = nb_1 * nb_2
if nb_2 != 0:
    quot = nb_1 / nb_2
else:
    quot = "ERROR (div by zero)"
if nb_2 != 0:
    mod = nb_1 % nb_2
else:
    mod = "ERROR (modulo by zero)"

table = {'Sum:' : sum, 'Difference:' : diff, 'Product:': prod, 'Quotient:': quot, 'Remainder:': mod}
for operation, value in table.items():
    print(f'{operation:12} {value}')
