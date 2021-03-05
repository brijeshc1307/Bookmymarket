from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product , cart):
    keys = cart.keys()
    for i in keys:
        if int(i) == product.id:
            return True
    return False;


@register.filter(name='cart_quantity')
def cart_quantity(product , cart):
    keys = cart.keys()
    for i in keys:
        if int(i) == product.id:
            return cart.get(i)
    return 0;


@register.filter(name='price_total')
def price_total(product , cart):
    return product.price * cart_quantity(product, cart)



@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    sum = 0;
    for i in products:
        sum += price_total(i,cart)

    return sum

@register.filter(name='selling_price')
def selling_price(num , num1):
    return num*(100+num1)/100
