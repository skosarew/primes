def get_prime_multipliers(number: int) -> list:
    """
    Generate prime multipliers for input integer n
    :param number: int number
    :return: list of multipliers
    """
    i = 2
    multipliers = []
    while i * i <= number:
        while number % i == 0:
            multipliers.append(i)
            number = number / i
        i = i + 1
    if number > 1:
        multipliers.append(number)
    return list(map(int, multipliers))
