import random
import math


def generate_prime_number(start, stop, precision):
    """
    Returns number with is suspected to be prime.
    Search between start stop range.
    Number could be a bit greater than stop.
    :param start: the smallest prime number that can occur
    :param stop: the highest prime number that can occur
    :param precision: The highest the higher probability
                      of proper prime numbers to be generated
    :return:
    """
    x = random.randint(start, stop)
    for i in range(0, int(10*math.log(x))):
        if miller_rabin(x, precision):
            return x
        else:
            x += 1
    raise ValueError


def miller_rabin(n, k):
    """
    Miller Rabin pseudo-prime test
    :param n: tested number
    :param k: precision - the higher k the higher probability that number
              is truly prime
    :return: True means likely a prime, (how sure about that, depending on k)
             False means definitely a composite.
    """

    def try_if_not_composite(a):
        """
        Inner function which will inspect whether a given witness
        will reveal the true identity of n.
        :param a: random number between 2 and tested value - 2
        :return: True if number is probably prime.
                 False if number definitely composite.
        """
        x = modular_exp(a, d, n)
        if x == 1 or x == n - 1:
            return True
        else:
            for j in range(1, s):
                if modular_exp(a, 2**j*d, n) == n-1:
                    return True
            return False

    if n == 2:
        return True
    # make sure to return True if n == 2

    if n % 2 == 0:
        return False
    # immediately return False for all the even numbers bigger than 2

    terms = change_form(n - 1)
    s = terms[0]
    d = terms[1]

    for i in range(0, k):
        a = random.randint(2, n - 2)
        if not try_if_not_composite(a):
            return False
    return True


def modular_exp(base, exponent, modulus):
    """
    :param a: number
    :param d: number
    :param n: number
    :return: a ** d (mod n)
    """

    if modulus == 1:
        return 0
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result


def change_form(m):
    """
    A tuple (s, d) of integers is returned.
    It's done by counting zeros at the end of m.
    such that m = (2 ** s) * d.
    :param m: positive integer
    :return: tuple (s, d) of integers
    """
    i = 0
    while m & (2 ** i) == 0:
        i += 1
    return i, m >> i
