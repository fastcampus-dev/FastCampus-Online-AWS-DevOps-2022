
function openModal(data){
    var orderModal = new bootstrap.Modal('#exampleModal')
    $('#orderTitle').text(data.product_name)
    $('#btnOrder').click(function(){
        var obj = {"product_id":data.product_id, "user_id":100}

        $.ajax({
            url: "/order",
            method: "POST",
            contentType: 'application/json',
            data: JSON.stringify(obj)
        }).done(function(res){
            orderModal.hide();
        })

    })

    orderModal.show();
    
}

$(document).ready(function () {
    
    $.ajax({
        url: "/products",
        method: "GET",
        dataType: "json"
    })
    .done(function(porducts){
        for (var product of porducts) {
            $('#content').append('\
            <div class="col">\
                <div class="card shadow-sm">\
                    <img src="'+ product.product_img+'">\
                <div class="card-body">\
                    <p class="card-text fs-4">'+ product.product_name +'</p>\
                    <p class="card-text fw-bold">Price ￦ '+ product.price +'</p>\
                    <p class="card-text text-secondary">Delivery fee ￦ '+ product.delivery_fee +'</p>\
                    <div class="d-flex justify-content-between align-items-center">\
                        <div class="btn-group">\
                            <small class="text-muted">' + product.uploaded +'</small>\
                        </div>\
                    <button type="button" class="btn btn-sm btn-outline-secondary" onclick=\'openModal('+JSON.stringify(product)+')\'>Order</button>\
                    </div>\
                </div>\
                </div>\
            </div>')
        }
    })
})