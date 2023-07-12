from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}

#  a context processor function that includes the current cart in the request context

# In above context processor, you instantiate the cart using the request object and make it available for 
# the templates as a variable named cart.
