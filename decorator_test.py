
from decorators.admin import admin_required

@admin_required
def my_function():
    print("hi")
    return "Hello, world!"

my_function()
