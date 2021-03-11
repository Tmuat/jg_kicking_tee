import random
import string

from datetime import datetime


def random_string_generator(size=5,
                            chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_sku_generator(instance):
    new_sku = random_string_generator()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(
                    sku=new_sku).exists()
    if qs_exists:
        return unique_sku_generator(instance)
    return new_sku


def random_string_generator_orders(size=6,
                                   chars=string.digits):
    alphabet = {'1': 'a',
                '2': 'b',
                '3': 'c',
                '4': 'd',
                '5': 'e',
                '6': 'f',
                '7': 'g',
                '8': 'h',
                '9': 'i',
                '10': 'j',
                '11': 'k',
                '12': 'l'}
    current_month = str(datetime.now().month)

    letter = alphabet[current_month].upper()

    order = str(
        letter + '-' + ''.join(random.choice(chars) for _ in range(size))
    )

    return order


def unique_order_generator(instance):
    new_order = random_string_generator_orders()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(
                    order_number=new_order).exists()
    if qs_exists:
        return unique_order_generator(instance)
    return new_order
