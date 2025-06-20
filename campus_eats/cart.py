from items.models import items
class Cart():
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('session_key')
        if not self.cart:
            self.cart = self.session['session_key'] = {}
        else:
            self.cart = self.session['session_key']

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'quantity': quantity, 'price': str(product.item_price)}

        self.save()

    def update_quantity(self, product_id, quantity):
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
        self.save()

    def save(self):
        self.session.modified = True

    def get_products(self):
        product_ids = self.cart.keys()
        products = items.objects.filter(id__in=product_ids)
        return products

    def get_total(self):
        total = 0
        for item in self.cart.values():
            total += int(item['quantity']) * float(item['price'])
        return total

