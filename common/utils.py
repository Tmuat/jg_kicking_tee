import random
import string


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
