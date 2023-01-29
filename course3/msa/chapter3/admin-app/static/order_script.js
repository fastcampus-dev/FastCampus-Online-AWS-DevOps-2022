$(document).ready(function () {
    
    $.ajax({
        url: "/admin/orders",
        method: "GET",
        dataType: "json"
    })
    .done(function(orders){
        for (var order of orders) {
            $('#content').append('\
            <tr>\
                <td scope="row">'+order.order_id+'</tds>\
                <td>'+order.product_name+'</td>\
                <td>'+order.user_name+'</td>\
                <td>'+order.created+'</td>\
            </tr>')
            
        }
    })

    var ws = new WebSocket("ws://localhost:8000/admin/ws");
    ws.onmessage = function(event) {
        data = event.data.split("'")[1]
        order = JSON.parse(data)
        
        $('#content').prepend('\
            <tr>\
                <td scope="row">'+order.order_id+'</tds>\
                <td>'+order.product_name+'</td>\
                <td>'+order.user_name+'</td>\
                <td>'+order.created+'</td>\
            </tr>')


    };
})