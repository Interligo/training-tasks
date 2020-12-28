def fibonacci_list(number: int) -> list:
    """Возвращает всю последовательность чисел Фибоначчи."""
    list_of_elements_fib = [1, 1]
    fib1, fib2 = 1, 1
    number = int(number)
    number -= 2
    while number > 0:
        fib1, fib2 = fib2, fib1 + fib2
        list_of_elements_fib.append(fib2)
        number -= 1
    return list_of_elements_fib


def fibonacci_recursion(number: int):
    """Возвращает n-ый элемент последовательности чисел Фибоначчи."""
    number = int(number)
    if number <= 1:
        return 1
    return fibonacci_recursion(number - 1) + fibonacci_recursion(number - 2)


def fibonacci_generator(number: int):
    """Последовательно генерирует элементы последовательности чисел Фибоначчи до n-ого элемента."""    
    fib1 = fib2 = 1
    for _ in range(int(number)):
        yield fib1
        fib1, fib2 = fib2, fib1+fib2    
    
