function gerarLink() {
    var icon = document.getElementById("select_icon").value;
    var perline = document.getElementById("perline").value;
    var size = document.getElementById("size").value;
    var theme = document.getElementById("theme").value;
    var link = "http://www.exemplo.com.br/icons?icon=" + icon

    if(size){
        link += "&size="+size
    }
    if(theme){
        link += "&theme="+theme
    }
    if(perline){
        link += "&perline="+perline
    }
    $("#colum_div_1").empty()
    $("#colum_div_1").append(`<label class="label_text" for="tema">Preview:</label><img id="preview" src="" alt="">`)
    
    link="https://skillicons.dev/icons?i=js,html,css,wasm,python,js,html,css,wasm,python,js,html,css,wasm,python,js,html,css,wasm,python,css,wasm,python,css,wasm,python,css,wasm,python&perline=7"


    console.log(link)
    var linkGerado = document.getElementById("link-gerado");
    var preview = document.getElementById("preview")
    linkGerado.innerHTML = link
    preview.setAttribute('src', link)
}


function copy_textLink() {
    var text_link = document.getElementById("link-gerado").innerHTML;
    
    navigator.clipboard.writeText(text_link)
    if (text_link != null && text_link != '')
        alert(`Has been copyed the link to use:\n${text_link}`)
}

