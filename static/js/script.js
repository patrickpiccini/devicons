var host = 'localhost'
var port = 80
var hml = false
var icon_tags = new Object() // object with selected values
var counter = 0 

var texte = ["Ableton", "ActivityPub", "Actix", "Adonis", 
"AfterEffects", "AiScript", "AlpineJS", "AndroidStudio", 
"Angular", "Ansible", "Apollo", "Appwrite", "Arduino", 
"Astro", "Atom", "Audition", "AutoCAD", "AWS", "Azul", 
"Azure", "Babel", "Bash", "Bevy", "Blender", "Bootstrap", 
"BSD", "C", "Cassandra", "Clojure", "Cloudflare", "CMake", 
"CodePen", "CoffeeScript", "CPP", "Crystal", "CS", "CSS", 
"D3", "Dart", "DENO", "devicon", "DevTo", "Discord", "DiscordBots", 
"Django", "Docker", "DotNet", "DynamoDB", "Eclipse", "Electron", 
"Elixir", "Emacs", "Ember", "Emotion", "ExpressJS", "FastAPI", 
"Fediverse", "Figma", "Firebase", "Flask", "Flutter", "Forth", 
"Fortran", "GameMakerStudio", "Gatsby", "GCP", "Gherkin", "Git", 
"Github", "GithubActions", "GitLab", "Godot", "GoLang", "Gradle", 
"Grafana", "GraphQL", "GTK", "Gulp", "Haskell", "Haxe", "HaxeFlixel", 
"Heroku", "Hibernate", "HTML", "Idea", "Illustrator", "Instagram", 
"IPFS", "Java", "JavaScript", "Jenkins", "Jest", "JQuery", "Julia", 
"Kafka", "Kotlin", "Ktor", "Kubernetes", "Laravel", "LaTeX", "LinkedIn", 
"Linux", "Lit", "Lua", "Markdown", "Mastodon", "MaterialUI", "Matlab", 
"Maven", "Misskey", "MongoDB", "MySQL", "NeoVim", "NestJS", "Netlify", 
"NextJS", "Nginx", "Nim", "NodeJS", "NuxtJS", "OCaml", "Octave", 
"OpenShift", "OpenStack", "Perl", "Photoshop", "PHP", "Plan9", 
"PlanetScale", "PostgreSQL", "Postman", "Powershell", "Premiere", 
"Prisma", "Processing", "Prometheus", "Pug", "Python", "PyTorch", 
"QT", "R", "RabbitMQ", "Rails", "RaspberryPi", "React", "ReactiveX", 
"Redis", "Redux", "Regex", "RemiX", "Replit", "Rocket", "RollupJS", 
"ROS", "Ruby", "Rust", "Sass", "Scala", "Selenium", "Sentry", 
"Sequelize", "Sketchup", "Solidity", "SolidJS", "Spring", "SQLite", 
"StackOverflow", "StyledComponents", "Supabase", "Svelte", "SVG", 
"Swift", "Symfony", "TailwindCSS", "Tauri", "TensorFlow", "ThreeJS", 
"Twitter", "TypeScript", "Unity", "UnrealEngine", "V", "Vala", "Vercel", 
"VIM", "VisualStudio", "Vite", "VSCode", "VueJS", "WebAssembly", 
"Webflow", "Webpack", "WindiCSS", "Wordpress", "Workers", "XD", "Zig"]
    
async function loadLabels() {

    texte.forEach((index) =>{
        var selector = document.getElementById("select_icon");
        var option = document.createElement("option");
        option.textContent = index
        option.value = index
        selector.appendChild(option);
    })
    

}

function gerarLink() {
    var icon_list = [] 
    let object_index = Object.keys(icon_tags)
    object_index.forEach((index) => {
        icon_list.push(icon_tags[index]["value"])
    });

    var perline = document.getElementById("perline").value;
    var size = document.getElementById("size").value;
    var theme = document.getElementById("theme").value;
    if (hml== true){
        var url =  `http://${host}:${port}/icons?`
    } else {
        var url =  `http://${host}/icons?`
    }

    if(icon_list != null && icon_list != []){
        console.log(icon_list);
        url += "icon="+icon_list.toString()
    }
    if(size){
        url += `&size=`+size
    }
    if(theme){
        url += `&theme=`+theme
    }
    if(perline){
        url += `&perline=`+perline
    }

    if (perline >= 1){
        width_icon = icon_list.length*55.962 / icon_list.length * perline
    } else {
        width_icon = icon_list.length*55.962
    }

    $("#colum_div_1").empty()
    $("#colum_div_1").append(`<label class="label_text" for="tema">Preview:</label>
    <img id="preview" src="" style=width:${width_icon}px alt="">`)
    
    var linkGerado = document.getElementById("link-gerado");
    var preview = document.getElementById("preview")
    linkGerado.innerHTML = url
    preview.setAttribute('src', url)
}

""
function copy_textLink() {
    var text_link = document.getElementById("link-gerado").innerHTML;
    
    navigator.clipboard.writeText(text_link)
    if (text_link != null && text_link != '')
        alert(`Has been copyed the link to use:\n${text_link}`)
}


function attualizeLabels() {
    var selector = document.getElementById("select_icon");
    var tag = document.createElement("label");
    var key = counter+=1
    var value = selector.value

    // Add the seletionaded options in object of icons
    icon_tags[key] = {value};

    tag.textContent = selector.value+' X';
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