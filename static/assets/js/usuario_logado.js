$(document).ready(function(){

    carrega_usuario_logado();

    function carrega_usuario_logado(){ 
        $.ajax({
            url: `usuario-logado/`,
            type: "GET",
            headers: { "X-CSRFToken": crf_token },
            success: function (data) {
                $('#more-details').append(`<span>${data[0].email}</span>`)
            },

            failure: function (data) {

            },

        });
    }
})