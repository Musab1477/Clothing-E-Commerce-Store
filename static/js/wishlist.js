document.addEventListener('DOMContentLoaded', function () {
    document.body.addEventListener('click', function (event) {

        if (event.target.closest('.addToWishlist')) {
            event.preventDefault();
            const productElement = event.target.closest('.product__details__text');
            const productData = {
                productName: productElement.getAttribute('data-product-name'),
                productPrice: productElement.getAttribute('data-product-price'),
                image: productElement.getAttribute('data-product-image')
            };

            console.log(productData);


            const item = {
                name: productData.productName,
                price: productData.productPrice,
                image: productData.image
            };

            console.log(item);
            let wishlishtItems = JSON.parse(localStorage.getItem('wishlist')) || [];
            const existingProductIndex = wishlishtItems.findIndex(item => item.name === productData.productName);
            if (existingProductIndex !== -1) {

                alert("Product Already Exist In Wishlist Babe! ");
            } else {
                wishlishtItems.push(item);
                localStorage.setItem('wishlist', JSON.stringify(wishlishtItems));
                console.log(wishlishtItems);
                alert('Product Added To Wishlist Babe!');
            }
        }
    });

});