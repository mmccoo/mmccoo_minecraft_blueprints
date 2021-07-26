from PIL import Image, ImageColor, ImageDraw
import pdb


im = Image.new('RGBA', (500, 500))

pallette = ['aqua',  'azure',     'bisque', 'black',     'blanchedalmond',
            'blue', 'blueviolet', 'brown',  'burlywood', 'cadetblue',

            'chartreuse', 'chocolate', 'cornsilk',     'crimson',  'cyan',
            'darkblue',   'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey',

            'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange',
            'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue',

            'darkslategray', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue',
            'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro',

            'gold', 'gray', 'green', 'honeydew', 'indianred',
            'lawngreen', 'lightcoral', 'lightgreen', 'lightpink', 'lightseagreen',

            'lightskyblue', 'lightslategrey', 'lightyellow', 'lime', 'linen',
            'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid',

            'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumturquoise', 'mediumvioletred',
            'midnightblue', 'mintcream',  'moccasin', 'navy', 'oldlace',

            'orangered', 'orchid', 'palegoldenrod', 'palevioletred', 'peachpuff',
            'peru', 'plum', 'powderblue', 'purple', 'rebeccapurple',

            'red', 'rosybrown', 'royalblue', 'saddlebrown', 'seagreen',
            'seashell', 'sienna', 'slateblue', 'slategray', 'snow',

            'springgreen', 'steelblue', 'tan', 'teal', 'thistle',
            'tomato', 'turquoise', 'violet', 'yellow', 'yellowgreen']


print("num colors: {}".format(len(pallette)))

swatch_size = 50

draw = ImageDraw.Draw(im)
id = 0
for c in pallette:
    x = int(id/10)
    y = id % 10
    id = id + 1

    draw.rectangle([x*swatch_size,    y*swatch_size,
                    (x+1)*swatch_size,(y+1)*swatch_size],
                   fill=ImageColor.getrgb(c))

im.save('pallette.png')
