import os, json

def build_json():
    for dir in os.listdir('./icons'):

        dict_icons ={}
        json_object=''

        for file in os.listdir(f'./icons/{dir}'):

            dict_icons[f"{file.replace('.svg','').lower()}"] = f"./icons/{dir}/{file}"
        # print(dict_icons)
        json_object = json.dumps(dict_icons, indent=4)

        with open(f"./data/{dir}.json", "w") as my_file:
            my_file.write(json_object)

def load_select_options():
    list=''
    for file in os.listdir(f'./icons/light'):
        list += file.replace('.svg','')+', '
    with open(f"tamplate/icons_name.txt", "w") as my_file:
        my_file.write(list[:-1])


if __name__ == '__main__':
    # build_json()
    load_select_options()