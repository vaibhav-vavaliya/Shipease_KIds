document.addEventListener('DOMContentLoaded', function() {
    let cartCount = localStorage.getItem('cart_count') || 0;
    document.getElementById('cart-count').textContent = cartCount;
    const addToCartLinks = document.querySelectorAll('.product-card .cart-icon');
    addToCartLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            cartCount = parseInt(localStorage.getItem('cart_count') || '0', 10) + 1;
            localStorage.setItem('cart_count', cartCount);
            document.getElementById('cart-count').textContent = cartCount;
            showAddToCartModal(link);
        });
    });

    function showAddToCartModal(link) {
        const modal = document.getElementById('add-to-cart-modal');
        if (!modal) return;
        modal.style.display = 'block';
        const productCard = link.closest('.product-card');
        const imgSrc = productCard.querySelector('img.product-img').src;
        const title = productCard.querySelector('.card-title').textContent;
        document.getElementById('add-to-cart-modal-img').src = imgSrc;
        document.getElementById('add-to-cart-modal-title').textContent = title;
        const closeBtn = document.getElementById('close-modal-btn');
        closeBtn.onclick = function(e) {
            e.stopPropagation();
            modal.style.display = 'none';
        };
        const modalContent = modal.querySelector('.add-to-cart-modal-content');
        if (modalContent) {
            modalContent.onclick = function(e) { e.stopPropagation(); };
        }
        modal.querySelector('.add-to-cart-modal-overlay').onclick = function(e) {
        };
    }

    const checkoutLinks = document.querySelectorAll('a[href="checkout"]');
    checkoutLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            localStorage.setItem('cart_count', 0);
            document.getElementById('cart-count').textContent = 0;
        });
    });
});
