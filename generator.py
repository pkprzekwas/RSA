# -*- coding: utf-8 -*-
import primes
import random


def generate_keys(start, stop, precision):
    """
    Generates key values for our cipher.
    :param start: the smallest prime number that can occur
    :param stop: the highest prime number that can occur
    :param precision: The highest the higher probability
                      of proper prime numbers to be generated
    :return:
    """
    try:
        p = primes.generate_prime_number(start, stop, precision)
        while True:
            q = primes.generate_prime_number(start, stop, precision)
            if q != p:
                break
    except:
        raise ValueError

    n = p * q
    euler_fcn = (p - 1) * (q - 1)

    while True:
        e = random.randint(1, euler_fcn)
        if co_prime(e, euler_fcn):
            break

    if co_prime(e, euler_fcn):
        factors = extended_euqlidian(e, euler_fcn)
        d = factors[1] % euler_fcn

    return n, e, d


def extended_euqlidian(a, b):
    """
    :param a: number
    :param b: number
    :return: tuple of three values: x, y and z, such that x is
    the GCD of a and b, and x = y * a + z * b
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_euqlidian(b % a, a)
        return g, x - (b // a) * y, y


def co_prime(e, m):
    """
    :param e: number
    :param m: number
    :return: 'True' if passed numbers are co-prime
       otherwise, it returns 'False'.
    """
    if gcd_euclidian(e, m) != 1:
            return False
    return True


def gcd_euclidian(a, b):
    """
    :param a: number
    :param b: number
    :return: Greatest Common Divisor of a and b
    """
    a = abs(a)
    b = abs(b)
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def encrypt(message, mod_n, e):
    """
    Takes message and encrypts it.
    :param message: secret message
    :param mod_n: n value of public key
    :param e: e value of public key
    :return: list of encrypted signs
    """
    numList = uni2num(message)
    return [primes.modular_exp(letter, e, mod_n) for letter in numList]


def decrypt(cipher, mod_n, d):
    """
    Takes encrypted list of longs and decrypt it
    :param cipher: secret encrypted message
    :param mod_n: n value of private key
    :param d: d value of private key
    :return: unicode message
    """
    message = [primes.modular_exp(letter, d, mod_n) for letter in cipher]
    return num2uni(message)


def uni2num(message):
    """
    Changes unicode message into list of integers.
    :param message: secret message passed in unicode
    :return: message converted into list of integers
    """
    return [ord(chars) for chars in list(message)]


def num2uni(message):
    """
    Changes list of integers into unicode message.
    :param message: list od integers
    :return: unicode message
    """
    decrypted_msg = [(unichr(chars)) for chars in list(message)]
    return ''.join(decrypted_msg)

