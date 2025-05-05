
import json, math, logging, re

class BuildSVG(object):
    def __init__(self, theme='', perline='', size=48) -> None:
        self.icon_list :list    = []
        self.theme     :str     = theme.lower()
        self.perline   :int     = int(perline)
        self.size      :int     = int(size)

    def build_icons(self, icons) -> list:

        icon_list = [icons[i].lower() for i in range(len(icons))]

        # Opening JSON file
        with open(f'./lambda/data/labels.json', 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)

        for icon in icon_list:
            if icon == 'all':
                try:
                    self.perline = 15
                    for icons_name, path in json_object.items():
                        if '-light' not in icons_name:
                            self.icon_list.append(path)

                except Exception as e:
                    logging.error(f'message: Error to found ALL icons: {e}')
            else:
                try:
                    icon_path = json_object.get(f'{icon}-{self.theme}', None)
                    if icon_path:
                        self.icon_list.append(icon_path)
                    else:
                        self.icon_list.append(json_object.get(icon))
                except:
                    logging.error(f'message: Error to found ALL icons: {e}')

            
    def build_svg(self) -> str:
        group_build = []
        line = 0
        column = 0
        scale = self.size / 256

        total_icons = len(self.icon_list)
        length = min(self.perline * 300, total_icons * 300) - 44
        height = math.ceil(total_icons / self.perline) * 300 - 44
        scale_width = length * scale
        scale_height = height * scale

        for svg_path in self.icon_list:
            if line == self.perline:
                line = 0
                column += 1

            with open(svg_path, "r", encoding="utf-8") as f:
                svg_content = f.read().strip()

            # Adicionando o grupo no SVG final
            group = f'<g transform="translate({line * 300},{column * 300})">{svg_content}</g>'
            group_build.append(group)
            line += 1

        # Construindo o SVG final
        svg_output = (
            f'<svg width="{scale_width}" height="{scale_height}" '
            f'viewBox="0 0 {length} {height}" fill="none" '
            f'xmlns="http://www.w3.org/2000/svg" '
            f'xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">'
            f'{"".join(group_build)}</svg>'
        )

        # Retornar a string sem escape de aspas
        return svg_output  # Sem o escape do \"
    
if __name__ == '__main__':
        # icons = 'C,Python,Java,AWS'
        icons = 'all'
        icons = icons.split(',')
        BSVG = BuildSVG('dark', 30, 48)
        BSVG.build_icons(icons)
        svg_object = BSVG.build_svg()