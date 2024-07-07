from django.db import models
from django.core.cache import cache

class MyModel(models.Model):
    # Your model fields here

    def cached_method(self):
        # Example usage:
        cache.set('my_key', 'my_value')
        value = cache.get('my_key')

        # Your method logic here
        return value
