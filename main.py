def main():
    #вводим число, до котрого будем искать простые
    n = input("Введите число: ")
    n = int(n)

    #создаем список из значений от 0 до n включительно
    primes = [i for i in range(n + 1)]

    #2 элемент списка - это 1 (не считается простым), поэтому на ее место записываем 0
    primes[1] = 0

    #начинаем цикл с 3 элемента
    i = 2
    while i <= n:
        #если элемент списка не 0, значит это простое число
        if primes[i] != 0:
            #заменяем нулями все числа, кратные ему (до конца списка)
            j = i + i
            while j <= n:
                primes[j] = 0
                j = j + i
        i += 1

    #убираем из списка все 0
    primes = [i for i in primes if i != 0]
    print('Простые числа до', n, ':')
    print(primes)

if __name__ == '__main__':
    main()