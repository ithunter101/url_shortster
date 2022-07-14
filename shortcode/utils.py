import random
import string

from .models import ShortCode

def generate_shortcode():
    allowed_chars = ''.join((string.ascii_letters, string.digits))
    while True:
        unique_id = ''.join(random.choice(allowed_chars) for _ in range(6))
        if not ShortCode.objects.filter(short_code=unique_id).first():
            return unique_id