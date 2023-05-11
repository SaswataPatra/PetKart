
from decorators import admin_required

@admin_required
def my_function():
    return "Hello, world!"
