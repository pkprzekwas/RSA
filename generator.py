# -*- coding: utf-8 -*-
from primes import PrimeNumberGenerator
import random


class KeyGenerator:
    """
    Class generates keys for RSA algorithm.
    It also has static methods for co-prime test,
    searching for great common divisor and
    """

    def __init__(self, start=8**50, stop=8**51, precision=50):
        """
        :param start: the smallest prime number that can occur
        :param stop: the highest prime number that can occur
        :param precision: The highest the higher probability
                          of proper prime numbers to be generated
        :return:
        """
        self.start = start
        self.stop = stop
        self.precision = precision

    def generate_keys(self):
        """
        Generates key values for our cipher.
        """
        prime_gen = PrimeNumberGenerator(self.start, self.stop, self.precision)
        try:
            p = prime_gen.generate_prime_number()
            while True:
                q = prime_gen.generate_prime_number()
                if q != p:
                    break
        except:
            raise ValueError

        n = p * q
        euler_fcn = (p - 1) * (q - 1)

        while True:
            e = random.randint(1, euler_fcn)
            if self.co_prime(e, euler_fcn):
                break

        d = self.mod_inv(e, euler_fcn)

        return n, e, d

    @staticmethod
    def co_prime(e, m):
        """
        :param e: number
        :param m: number
        :return: 'True' if passed numbers are co-prime
           otherwise, it returns 'False'.
        """
        if KeyGenerator.gcd_euclidian(e, m) != 1:
                return False
        return True

    @staticmethod
    def mod_inv(a, m):
        gcd, x, y = KeyGenerator.extended_euqlidian(a, m)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % m

    @staticmethod
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

    @staticmethod
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
            g, y, x = KeyGenerator.extended_euqlidian(b % a, a)
            return g, x - (b // a) * y, y

    def encrypt(self, message, mod_n, e):
        """
        Takes message and encrypts it.
        :param message: secret message
        :param mod_n: n value of public key
        :param e: e value of public key
        :return: list of encrypted signs
        """
        numList = self.uni2num(message)
        return [PrimeNumberGenerator.modular_exp(letter, e, mod_n) for letter in numList]

    def decrypt(self, cipher, mod_n, d):
        """
        Takes encrypted list of longs and decrypt it
        :param cipher: secret encrypted message
        :param mod_n: n value of private key
        :param d: d value of private key
        :return: unicode message
        """
        message = [PrimeNumberGenerator.modular_exp(letter, d, mod_n) for letter in cipher]
        return self.num2uni(message)

    def uni2num(self, message):
        """
        Changes unicode message into list of integers.
        :param message: secret message passed in unicode
        :return: message converted into list of integers
        """
        return [ord(chars) for chars in list(message)]

    def num2uni(self, message):
        """
        Changes list of integers into unicode message.
        :param message: list od integers
        :return: unicode message
        """
        decrypted_msg = [(unichr(chars)) for chars in list(message)]
        return ''.join(decrypted_msg)

