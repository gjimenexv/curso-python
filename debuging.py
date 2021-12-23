def divisors(num):
    divisors = []
    try:
        if num >= 0:
            for i in range(1, num + 1):
                if num % i == 0:
                    divisors.append(i)
            return divisors
        else:
            raise ValueError ("No se pueden utilizar numero vacios")
    except ValueError as ve:
        print("Solo se permiten numeros positivos")

def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un número")

if __name__ == '__main__':
    run()