$(document).ready(function () {
    
    $.ajax({
        url: "/admin/users",
        method: "GET",
        dataType: "json"
    })
    .done(function(users){
        for (var user of users) {
            $('#content').append('\
            <tr>\
                <td scope="row">'+user.user_name+'</tds>\
                <td>'+user.user_email+'</td>\
                <td>'+user.street_address+'</td>\
                <td>'+user.address_line_2+'</td>\
                <td>'+user.phone+'</td>\
            </tr>')
            
        }
    })
})