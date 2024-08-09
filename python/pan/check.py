from sympy.ntheory import isprime
from enum import Enum


class CheckResult(Enum):
    NotPAN = 1
    PAN = 2
    PrimePAN = 3


def check(n: int) -> CheckResult:
    if is_prime_candidate(n):
        chk_digit = calculate_mod_10_checksum(n // 10)
        if chk_digit == n % 10:
            if is_prime(n):
                return CheckResult.PrimePAN
        return CheckResult.PAN
    return CheckResult.NotPAN


def is_prime_candidate(n: int) -> bool:
    last = n % 10
    return last == 1 or last == 3 or last == 7 or last == 9


def is_prime(n: int) -> bool:
    return isprime(n)


def calculate_mod_10_checksum(number: int) -> int:
    sum = 0
    for i in range(number):
        digit = number % 10
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
            sum += digit
            number //= 10
    check = sum % 10
    if check != 0:
        check = 10 - check
    return check
