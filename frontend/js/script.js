const host = 'localhost';
const port = 5563;
const hml = false;
const iconTags = {};
let counter = 0;

function gerarLink() {
    const iconList = Object.values(iconTags).map(obj => obj.value);
    const perline = parseInt(document.getElementById("perline").value) || 30;
    const size = parseInt(document.getElementById("size").value) || 48;
    const theme = document.getElementById("theme").value || 'dark';

    let url = hml 
        ? `http://${host}:${port}/icon?` 
        : `https://api.devicons.dev.br/icon?`;

    const queryParams = new URLSearchParams();
    if (iconList.length) queryParams.append("icons", iconList.join(","));
    queryParams.append("size", size);
    queryParams.append("theme", theme);
    queryParams.append("perline", perline);
    url += queryParams.toString();

    if (iconList.length > 0) {
        const width = 56 * Math.min(iconList.length, perline);
        document.getElementById("colum_div_1").innerHTML = `
            <label class="label_text" for="tema">Preview:</label>
            <img id="preview" src="${url}" style="width:${width}px;" alt="">
        `;

        document.getElementById("link_gerado").textContent = url;
    }
}
function copy_textLink() {
    const textElement = document.getElementById("link_gerado");
    const text = textElement.textContent || textElement.innerText;

    if (!text) {
        alert("Nenhum link para copiar.");
        return;
    }

    // Cria um elemento de texto temporário
    const tempInput = document.createElement("textarea");
    tempInput.value = text;
    document.body.appendChild(tempInput);

    // Seleciona e copia o conteúdo
    tempInput.select();
    tempInput.setSelectionRange(0, 99999); // Para dispositivos móveis
    document.execCommand("copy");

    // Remove o elemento temporário
    document.body.removeChild(tempInput);

    // Mensagem de sucesso (opcional)
    alert("Link copiado!");
}


function attualizeLabels() {
    const selector = document.getElementById("select_icon");
    const value = selector.value;

    if (!value || Object.values(iconTags).some(obj => obj.value === value)) {
        return; // impede duplicatas
    }

    const key = ++counter;
    iconTags[key] = { value };

    const tag = document.createElement("label");
    tag.textContent = `${value} ✖  `;
    tag.className = "label_tag";
    tag.dataset.key = key;
    tag.id = `label_${key}`;
    tag.style.cursor = "pointer";

    tag.addEventListener("click", () => {
        delete iconTags[tag.dataset.key];
        tag.remove();
    });

    document.getElementById("div_tags").appendChild(tag);
}