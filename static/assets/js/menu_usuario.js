$(document).ready(function(){

    carrega_menu();

    function carrega_menu(){ 
        $.ajax({
            url: `menu-usuario/`,
            type: "GET",
            headers: { "X-CSRFToken": crf_token },
            success: function (data) {
                
                $('#more-details').append(`<span>${data[0].username}</span>`)
                console.log(data.id)
                $.each(data, function(index, value){

                    let nome_menu = value.nome_menu
                    let caminho = value.caminho

                    $('#menu_interativo').append(
                        `
                        <li class="nav-item">
                            <a href="${window.location.host}/${caminho}" class="nav-link "><span class="pcoded-mtext">${nome_menu}</span></a>
                        </li>
                        `
                    )
                })
            },

            failure: function (data) {

            },

        });
    }
})