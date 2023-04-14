$(document).ready(function () {
    var token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiQm9yYW0gSmVvbmcifQ.TPQHFjGctA6NZfeTnfm1CqnoN7Vx5TPOL60DXvZQt30"

    const apiGatewayUrl = "https://evxwnn1aca.execute-api.ap-northeast-2.amazonaws.com"
    
    $.ajax({
        url: apiGatewayUrl + "/forum",
        method: "GET",
        headers: {"Authorization": token},
        dataType: "json"
    })
    .done(function(forums){
        forums.forEach(function(forum, index){
            if(forum.Messages == undefined)
                forum.Messages = 0;
                
            $('#content').append('\
                <tr>\
                <th scope="row">'+(index + 1)+'</th>\
                <td>' + forum.Category + '</td>\
                <td>' + forum.Name+'</td>\
                <td>' + forum.Messages +'</td>\
            </tr>')

        });
    })
})