import random
import string
from datetime import date

from django.utils import timezone

#  ----------------- FUNCTIONS ----------------------


# Function to generate random string of number having random
def randomString():
    letters = string.digits
    return "".join(
        random.choice(letters) for i in range(int(random.choice(string.digits)))
    )


# Function to define avatar upload location
def avatar_upload_location(instance, filename):
    filename = f"{instance.id}_{filename}"
    return "static/profile_pic/{0}/{1}".format(instance.id, filename)


def store_multi_image(instance, filename):
    filename = f"{str(instance.store.id)}_{str(date.today())}_{filename}"
    return "store/{0}".format(filename)


def product_multi_image(instance, filename):
    filename = f"{str(instance.id)}_{str(date.today())}_{filename}"
    return "static/product/{0}/{1}/{2}".format(
        instance.product.name, instance.id, filename
    )


def convert_to_list(text):
    """
    This function takes multiline text and convert every line text into string & return list of string.
    """
    import json

    lines = text.split("\n")
    result = []
    for line in lines:
        result.append(str(line))
    result = json.dumps(result)
    # print(result)
    return result


def generate_payment_id():
    """
    This function returns the unique payment ID.
    """
    prefix = "PAY"
    timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
    random_part = "".join(random.choices(string.digits, k=6))
    return f"{prefix}-{timestamp}-{random_part}"
