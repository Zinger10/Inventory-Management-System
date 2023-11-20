document.addEventListener("DOMContentLoaded", function() {
    const addButtons = document.querySelectorAll(".add-button");
    const subtractButtons = document.querySelectorAll(".subtract-button");
    const qtyplusButtons = document.querySelectorAll(".qtyplus");
    const qtyminusButtons = document.querySelectorAll(".qtyminus");
    const qtyFields = document.querySelectorAll(".quantity");

    // Add button click event
    addButtons.forEach(button => {
        button.addEventListener("click", () => {
            const productId = button.getAttribute("data-product-id");
            // Send an AJAX request to add one to the product quantity for the given product ID
            fetch(`/add_product/${productId}`, { method: "POST" })
                .then(response => response.json())
                .then(data => {
                    // Update the quantity and total price on the page
                    const quantityInput = document.querySelector(`[data-product-id="${productId}"] .qty`);
                    quantityInput.value = parseInt(quantityInput.value) + 1;
                });
        });
    });

    // Subtract button click event
    subtractButtons.forEach(button => {
        button.addEventListener("click", () => {
            const productId = button.getAttribute("data-product-id");
            // Send an AJAX request to subtract one from the product quantity for the given product ID
            fetch(`/subtract_product/${productId}`, { method: "POST" })
                .then(response => response.json())
                .then(data => {
                    // Update the quantity and total price on the page
                    const quantityInput = document.querySelector(`[data-product-id="${productId}"].qty`);
                    const quantity = parseInt(quantityInput.value);
                    if (quantity > 0) {
                        quantityInput.value = quantity - 1;
                    }
                });
        });
    });

    // Quantity increment and decrement buttons
    qtyplusButtons.forEach(button => {
        button.addEventListener("click", () => {
            const quantityField = button.getAttribute("field");
            const quantityInput = button.parentElement.querySelector(`[name='${quantityField}']`);
            quantityInput.value = parseInt(quantityInput.value) + 1;
        });
    });

    qtyminusButtons.forEach(button => {
        button.addEventListener("click", () => {
            const quantityField = button.getAttribute("field");
            const quantityInput = button.parentElement.querySelector(`[name='${quantityField}']`);
            const quantity = parseInt(quantityInput.value);
            if (quantity > 0) {
                quantityInput.value = quantity - 1;
            }
        });
    });
});

//modal pop out

// scripts.js
function openEditModal(productId) {
    var modal = document.getElementById('editModal');
    modal.style.display = 'block';

    // Fill in the form fields with product data
    var product = getProductById(productId); // Implement this function to retrieve the product data
    if (product) {
        document.getElementById('editProductId').value = productId;
        document.getElementById('editName').value = product.name;
        document.getElementById('editPrice').value = product.price;
        document.getElementById('editQuantity').value = product.quantity;
    }
}

function closeEditModal() {
    document.getElementById('editModal').style.display = 'none';
}

// Function to retrieve product data by product ID (You need to implement this function)
function getProductById(productId) {
    // Implement your logic to retrieve product data from the server or data source
    // Replace this with actual code to fetch product data
    return {
        name: 'Product Name',
        price: 10.00,
        quantity: 100
    };
}

