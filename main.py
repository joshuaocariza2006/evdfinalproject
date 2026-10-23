from pyscript import document
from pyodide.ffi import create_proxy

# Price of each carrot lumpia
prices = {
    "Original Carrot Lumpia": 5,
    "Spicy Carrot Lumpia": 7,
    "Cheesy Carrot Lumpia": 8,
    "Special Carrot Lumpia": 10
}

cart = {}


def update_cart():
    cart_box = document.querySelector("#cart-items")
    cart_box.innerHTML = ""
    total = 0

    if not cart:
        cart_box.innerHTML = '<p class="empty-cart">Your cart is empty. Add a lumpia to get started!</p>'

    for name, quantity in cart.items():
        price = prices[name]
        item_total = price * quantity
        total += item_total

        row = document.createElement("div")
        row.className = "cart-item"
        row.innerHTML = f"<span>{name} x {quantity}</span><strong>₱{item_total}</strong>"
        cart_box.appendChild(row)

    document.querySelector("#cart-total").textContent = f"₱{total}"
    document.querySelector("#cart-count").textContent = str(sum(cart.values()))


def add_product(event):
    name = event.currentTarget.getAttribute("data-product")
    cart[name] = cart.get(name, 0) + 1
    update_cart()
    document.querySelector("#cart-message").textContent = name + " added to cart."


def add_selected_product(event=None):
    name = document.querySelector("#product").value
    quantity = int(document.querySelector("#quantity").value)

    if quantity < 1:
        quantity = 1
    if quantity > 99:
        quantity = 99

    cart[name] = cart.get(name, 0) + quantity
    update_cart()
    document.querySelector("#cart-message").textContent = "Added to your cart."


def plus_quantity(event=None):
    field = document.querySelector("#quantity")
    field.value = str(int(field.value) + 1)


def minus_quantity(event=None):
    field = document.querySelector("#quantity")
    if int(field.value) > 1:
        field.value = str(int(field.value) - 1)


def clear_cart(event=None):
    cart.clear()
    update_cart()
    document.querySelector("#cart-message").textContent = "Cart cleared."
    document.querySelector("#order-result").textContent = ""


def checkout(event):
    event.preventDefault()

    if not cart:
        document.querySelector("#order-result").textContent = "Please add a product first."
        return

    name = document.querySelector("#customer-name").value.strip()
    contact = document.querySelector("#customer-contact").value.strip()

    if name == "" or contact == "":
        document.querySelector("#order-result").textContent = "Please enter your name and contact details."
        return

    order_list = []
    total = 0

    for product, quantity in cart.items():
        order_list.append(product + " x " + str(quantity))
        total += prices[product] * quantity

    result = (
        "Order Summary\n"
        + "Name: " + name + "\n"
        + "Contact: " + contact + "\n"
        + "Items: " + ", ".join(order_list) + "\n"
        + "Total: ₱" + str(total) + "\n\n"
        + "This is a demo. Your order was not sent."
    )
    document.querySelector("#order-result").textContent = result


# Connect the buttons to the Python functions
for button in document.querySelectorAll(".add-product"):
    button.addEventListener("click", create_proxy(add_product))

document.querySelector("#add-to-cart").addEventListener("click", create_proxy(add_selected_product))
document.querySelector("#plus").addEventListener("click", create_proxy(plus_quantity))
document.querySelector("#minus").addEventListener("click", create_proxy(minus_quantity))
document.querySelector("#clear-cart").addEventListener("click", create_proxy(clear_cart))
document.querySelector("#checkout-form").addEventListener("submit", create_proxy(checkout))

update_cart()
