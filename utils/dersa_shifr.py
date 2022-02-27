import math
import sympy


def isINT(num):
    if num % 1 == 0:
        return True
    return False


def isPrime(n):
    return sympy.isprime(n)

def format_message(input_string):
    list_ascii = []
    for i in range(len(input_string)):
        list_ascii.append(ord(input_string[i]))
    return list_ascii

def decrypt(private_key, cipher_text):
    d, n = private_key
    # pow(with three arguments) => x**y % z
    p = pow(cipher_text, d, n)
    return p


def decrypt_string(private_key, list_cipher_ascii):
    list_decrypted_ascii = []
    for i in list_cipher_ascii:
        list_decrypted_ascii.append(decrypt(private_key, int(i)))
    return list_decrypted_ascii


def RSA(p, q,d, cipher_message):
    n = p * q
    # publicKey = (e, n)
    # print("Public Key ( e= ", e, ", n= ", n, ")")
    privateKey = (d, n)
    # print("Private Key ( d= ", d, ", n= ", n, ")")
    # print(f"Encrypting (", plain_message, ") ...")
    message = decrypt_string(privateKey, cipher_message)
    # print("Decrypting (", cipher_message, ") ...")
    return message
# print(RSA(3,5,'abdulaziz'))