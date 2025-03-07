def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for val in range(2, (n // 2) + 1):
        if n % val == 0:
            return False

    return True


def get_prime_factors(n: int) -> list[int]:
    # repeatedly divide by smallest prime number that divides evenly
    # until you reach 1
    _n = n
    local_array = []
    while _n != 1:
        for val in range(2, _n + 1):
            if is_prime(val):
                if _n % val == 0:
                    local_array.append(val)
                    _n = _n // val
                    break

    return local_array


def main() -> None:
    print(get_prime_factors(17))


if __name__ == '__main__':
    main()
