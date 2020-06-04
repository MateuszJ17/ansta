from decimal import *


def post_code_generator(first_code='79-900', second_code='80-155'):
    """
    Generate post codes in between first and last specified code
    """
    first_code_parsed = int(first_code.replace('-', ''))
    second_code_parsed = int(second_code.replace('-', ''))

    for code in range(first_code_parsed + 1, second_code_parsed):
        formatted_code = str(code)
        print(f'{formatted_code[:2]}-{formatted_code[2:]}')


def generate_missing_nums(values=[2,3,7,4,9], length=10):
    """
    Generate numbers missing from input list to the specified end
    """
    start = 1
    full_list = [x for x in range(start, length + 1)]
    missing = [x for x in full_list if x not in values]

    print(missing)


def generate_with_jump():
    """
    Generate list of Decimals from 2 to 5.5 with 0.5 step
    """
    start = 2
    values = []

    while Decimal(start) <= Decimal(5.5):
        values.append(Decimal(start))
        start = Decimal(start) + Decimal(0.5)

    print(values)


if __name__ == '__main__':
    """
    Please uncomment to run
    """
    # post_code_generator()
    # generate_missing_nums()
    # generate_with_jump()
