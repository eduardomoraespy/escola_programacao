// Obter valores
let telefone= document.querySelector('input#id_telefone');
let lista = document.querySelector('select#telefone_lista');
let res = document.querySelector('div#res');
let cad_body = document.querySelector('div#id_cad_body');
let valores = [];


function inLista(n, l){
    if (l.indexOf(n) != -1){
        return true
    } else {
        return false
    }
};

function adicionar(){
    cad_body.innerHTML = ''
    if(telefone.value && !inLista(telefone.value, valores)){

        cad_body.innerHTML += `
        <div class="alert alert-success" role="alert">
            Telefone adicionado a lista
        </div>`

        // adicionar valor no vetor
        valores.push(telefone.value)

        // adicionar option no select
        let item = document.createElement('option')
        item.text = `${telefone.value}`
        item.value = `${telefone.value}`

        // Adicionar na lista
        lista.appendChild(item)
        res.innerHTML = ''
        telefone.value = ''

    }else{
        //window.alert('numero iválido ou já existente')
        //new Error('numero iválido ou já existente');
        
        cad_body.innerHTML = ''
        cad_body.innerHTML += `
        <div class="alert alert-warning" role="alert">
            Telefone já existente
        </div>`
    }

    telefone.value = ''
    telefone.focus()
};
