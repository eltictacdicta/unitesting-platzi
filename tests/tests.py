def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total


def test_calculate_total_without_products():
    assert calculate_total([]) == 0

def test_calculate_total_with_one_product():
    products = [{"name": "keyboard", "price": 150}]
    assert calculate_total(products) == 150

def test_calculate_total_with_multiples_products():
    products = [{"name": "keyboard", "price": 150}, {"name": "mouse", "price": 80}]
    assert calculate_total(products) == 230

if __name__ == "__main__":
    test_calculate_total_with_multiples_products()
    test_calculate_total_without_products()
    test_calculate_total_with_one_product()




