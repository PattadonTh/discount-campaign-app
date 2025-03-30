const cartItems = [
  { name: "T-Shirt", price: 350, category: "Clothing" },
  { name: "Hat", price: 250, category: "Accessories" },
  { name: "Belt", price: 230, category: "Accessories" },
  { name: "Hoodie", price: 700, category: "Clothing" },
  { name: "Watch", price: 850, category: "Accessories" }
];

function renderCart(items) {
  const container = document.getElementById("cart-container");
  const totalBox = document.getElementById("cart-total");
  container.innerHTML = "";
  let total = 0;

  items.forEach(item => {
    container.innerHTML += `
      <div class="cart-item">
        <h3>${item.name}</h3>
        <p>Category: ${item.category}</p>
        <p class="price">฿${item.price}</p>
      </div>
    `;
    total += item.price;
  });

  totalBox.innerHTML = `<h3>Cart Total: ฿${total}</h3>`;
}

renderCart(cartItems);
