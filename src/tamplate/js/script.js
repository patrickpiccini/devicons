var icon_tags = new Object() // object with selected values
var icon_list = []
var counter = 0 


function gerarLink() {
    let object_index = Object.keys(icon_tags)
    object_index.forEach((index) => {
        icon_list.push(icon_tags[index]["value"])
    });


    var icon = document.getElementById("select_icon").value;
    var perline = document.getElementById("perline").value;
    var size = document.getElementById("size").value;
    var theme = document.getElementById("theme").value;
    var link = "http://localhost/icons?icon=" + icon_list.toString()

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


function attualizeLabels() {
    var selecionador = document.getElementById("select_icon");
    var tag = document.createElement("label");
    var key = counter+=1
    var value = selecionador.value

    // Add the seletionaded options in object of icons
    icon_tags[key] = {value};

    tag.textContent = selecionador.value+' X';
    tag.className = key
    tag.id = "label_tag"


    tag.addEventListener("click", function() {
        // Delete the seletionaded options in object of icons

        delete icon_tags[this.className]
        
        this.parentNode.removeChild(this);
      });

    var tagsDiv = document.getElementById("div_tags");
    tagsDiv.appendChild(tag);
  }