# python-template
This repository is a template for python projects


### Arquitetura do Projeto:

~~~
dev-icon
│   .env
│   .gitignore
│   app.py
│   LICENSE
│   README.md
│   requirements.txt
│
├───conf
│       devicon
│       devicon.service
│       gunicorn.conf.py
│
├───data
│       dark.json
│       light.json
│
├───icons
│   ├───dark
│   │       ...svg
│   │
│   └───light
│           ...svg
├───logs
│        log.log
│
├───src
│   │   __init__.py
│   │
│   ├───resources
│   │       build_icons.py
│   │       home.py
│   │       icons.py
│   │       __init__.py
│   │
│   ├───tamplate
│   │       icons_name.txt
│   │       index.html
│   │
│   ├───test
│   │       __init__.py
│   │
│   └───utils
│           build_json.py
│           __init__.py
│   
└───static
    ├───css
    │        index.css
    ├───img        
    │        devicon.svg
    │        email.svg
    │        exemple.png
    │        git.svg
    │        linkedin.svg
    │        logo.svg
    └───js
            script.js
~~~
