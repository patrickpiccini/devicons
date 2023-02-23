
import json, math

class BuildSVG(object):
    def __init__(self, theme='', perline='') -> None:
        self.icon_list :list    = []
        self.theme     :str     = theme
        self.perline   :int     = int(perline)

    def build_icons(self, icons) -> list:
        icon_list = [icons[i].lower() for i in range(len(icons))]

        # Opening JSON file
        with open(f'./data/{self.theme}.json', 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)

        for icon in icon_list:
            try:
                self.icon_list.append(json_object[icon])
            except:
                pass

    def build_svg(self) ->object:

        group_build = ''
        line        = 0
        colum       = 0
        scale       = 0.1875
        length          = min(self.perline * 300, len(self.icon_list) * 300) - 44
        height          = math.ceil(len(self.icon_list) / self.perline) * 300 - 44
        scaleWidth      = length * scale
        scaleHeight     = height * scale

        print(length, height, scaleWidth, scaleHeight)

        for svg in self.icon_list:

            if line == self.perline:
                line = 0
                colum += 1
            print(line, colum)
            

            with open(svg, "r") as my_file:
                svg_file = my_file.read()

            group_build += f'''
            <g transform="translate({line * 300}, {colum * 300})">
                {svg_file}
            </g>
            '''
            line +=1
        
        obj_svg = f'''
        <svg width="{scaleWidth}" height="{scaleHeight}" viewBox="0 0 {length} {height}" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">

            {group_build}

        </svg> 
        '''
        
        return obj_svg 


    