import os, json


def build_json() -> None:
    dict_icons ={}
    label_icon = {}
    for icon_name in os.listdir('./lambda/icons'):

        dict_icons[f"{icon_name.replace('.svg','').lower()}"] = f"./icons/{icon_name}"
        label_icon[f"{icon_name.replace('.svg','')}"] = f"./icons/{icon_name}"
        # print(dict_icons)

    dict_icons_json = json.dumps(dict_icons, indent=4)

    with open(f"./lambda/data/labels.json", "a") as my_file:
        my_file.write(dict_icons_json)
    
    label_icon_json = json.dumps(label_icon, indent=4)
    with open(f"./lambda/data/labels_name.json", "a") as my_file:
        my_file.write(label_icon_json)


def load_select_options() -> None:
    # Supondo que o JSON esteja salvo em um arquivo chamado "icons.json"
    with open("./lambda/data/labels_name.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    unique_names = set()

    for key in data.keys():
        if key.endswith("-dark"):
            base_name = key[:-5]
        elif key.endswith("-light"):
            base_name = key[:-6]
        else:
            base_name = key
        unique_names.add(base_name)

    # Salva os nomes únicos no arquivo
    with open("./lambda/data/icon_names.txt", "w", encoding="utf-8") as output_file:
        sorted_names = sorted(unique_names)
        for i in range(0, len(sorted_names), 8):
            line = ", ".join(f'"{name}"' for name in sorted_names[i:i+8])
            output_file.write(line + ", \n")

def build_markdown_table():
    '''Apos criar o arquivo renomeie  /icons por /lambda/icons'''
    with open(f"./lambda/data/labels.json", "r", encoding="utf-8") as my_file:
        data = json.load(my_file)

        # Cabeçalho da tabela Markdown
    markdown_table = "| Icon ID | Icon | Icon ID | Icon | Icon ID | Icon |\n|---------|------|---------|------|---------|------|\n"

    # Adiciona as linhas da tabela
    line_count = 0
    line = '|'
    for icon_id, path in data.items():
        if '-light' not in icon_id:
            line_count += 1
            if line_count <=2:
                line += f' `{icon_id}` | <img src="{path}" width="48"> |'
            else:
                line += f' `{icon_id}` | <img src="{path}" width="48">|\n'
                markdown_table += line
                line_count = 0
                line = '|'

    # Escreve a tabela em um arquivo Markdown
    with open("./lambda/data/tabela_icones.md", "w", encoding="utf-8") as f:
        f.write(markdown_table)

if __name__ == '__main__':
    build_markdown_table()
    # build_json()
    # load_select_options()