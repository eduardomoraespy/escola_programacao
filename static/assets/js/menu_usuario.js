$(document).ready(function(){

    carrega_menu();

    function carrega_menu(){ 
        $.ajax({
            url: `menu-usuario/`,
            type: "GET",
            headers: { "X-CSRFToken": crf_token },
            success: function (data) {
                
                console.log(data.id)
                $.each(data, function(index, value){

                    let nome_menu = value.nome_menu
                    let caminho = value.caminho

                    console.log(caminho)
                    console.log(window.location.host)

                    $('#menu_interativo').append(
                        `
                        <li class="nav-item">
                            <a href="https://escola-prog.herokuapp.com/${caminho}" class="nav-link "><span class="pcoded-mtext">${nome_menu}</span></a>
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