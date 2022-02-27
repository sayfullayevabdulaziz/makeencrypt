import math
import sympy


def isINT(num):
    if num % 1 == 0:
        return True
    return False


def isPrime(n):
    return sympy.isprime(n)


def calc_e(t):
    for e in range(2, t):
        if math.gcd(e, t) == 1:
            return e
    return None


def calc_d(t, e):
    d = 0
    L = 0
    while True:
        d = (t * L + 1) / e
        if isINT(d):
            break
        L += 1
    return int(d)


def encrypt(public_key, message):
    e, n = public_key
    # pow(with three arguments) => x**y % z
    return pow(message, e, n)

def format_message(input_string):
    list_ascii = []
    for i in range(len(input_string)):
        list_ascii.append(ord(input_string[i]))
    return list_ascii

def encrypt_string(public_key, input_string):
    list_ascii_p = format_message(input_string)
    print("list_ascii_numbers(BEFORE ENCRYPTION) : ", list_ascii_p)
    list_cipher_ascii = []
    for i in list_ascii_p:
        list_cipher_ascii.append(encrypt(public_key, i))
    print("list_ascii_numbers(AFTER ENCRYPTION) : ", list_cipher_ascii)
    return list_cipher_ascii


def decrypt(private_key, cipher_text):
    d, n = private_key
    # pow(with three arguments) => x**y % z
    p = pow(cipher_text, d, n)
    return p


def decrypt_string(private_key, list_cipher_ascii):
    list_decrypted_ascii = []
    for i in list_cipher_ascii:
        list_decrypted_ascii.append(decrypt(private_key, i))
    return list_decrypted_ascii


def RSA(p, q, plain_text):
    result = ''
    n = p * q
    t = (p - 1) * (q - 1)
    e = calc_e(t)
    d = calc_d(t, e)
    publicKey = (e, n)
    # print("Public Key ( e= ", e, ", n= ", n, ")")
    privateKey = (d, n)
    plain_message = plain_text
    # print("Private Key ( d= ", d, ", n= ", n, ")")
    # print(f"Encrypting (", plain_message, ") ...")
    cipher_message = encrypt_string(publicKey, plain_message)

    # print("Decrypting (", cipher_message, ") ...")
    return cipher_message
# print(RSA(3,5,'abdulaziz'))