#!/usr/bin/python


import numpy as np
from PIL import Image, ImageColor
import random
import json
import pdb
import argparse
import pathlib

# mmccoo_markers/python/genimage.py -voxel_path stl/Yoga_Girl/yoga_girl.json
parser = argparse.ArgumentParser(description='generate texture map for Miles markers in minecraft.')
parser.add_argument('-voxel_path', type=pathlib.Path, help='path to txt file from https://drububu.com/miscellaneous/voxelizer/?out=json')
parser.add_argument('-rotate', type=str, default="", help='list is rotations to perform. for example, "xxyz" will first rotate counterclockwise twice about x axix, then y and then z')
args = parser.parse_args()



#Read image
#im = Image.open( 'mmccoo_markers/textures/layer1.png' )
#Display image
#im.show()
with open(args.voxel_path) as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()


texture_size = 128

image = Image.new('RGBA', (texture_size*10,texture_size*10))


numpoints = len(jsonObject['voxels'])

print("txt has {} points".format(numpoints))


points = np.array([[int(voxel['x']),int(voxel['y']),int(voxel['z'])] for voxel in jsonObject['voxels']])

trans = np.identity(3)

rx = np.array([[1,0,0],
               [0,0,-1],
               [0,1,0]])

ry = np.array([[0, 0, 1],
               [0, 1, 0],
               [-1, 0, 0]])

rz = np.array([[0, -1, 0],
               [1, 0, 0],
               [0, 0, 1]])

for c in args.rotate:
    if (c=='x'):
        print("rotating x")
        trans = np.matmul(trans, rx)
    elif (c=='y'):
        print("rotation y")
        trans = np.matmul(trans, ry)
    elif (c=='z'):
        print("rotating z")
        trans = np.matmul(trans, rz)
    else:
        print("unexpected rotatio char {}. expecting x,y or z".format(c))
        exit


points = np.array([np.matmul(pt, trans) for pt in points])


(xl,yl,zl,xh,yh,zh) = bbox = (points[:,0].min(),points[:,1].min(),points[:,2].min(),
        points[:,0].max(),points[:,1].max(),points[:,2].max())

center = (round((points[:,0].min()+points[:,0].max())/2),
          round((points[:,1].min()+points[:,1].max())/2),
          round((points[:,2].min()+points[:,2].max())/2))


# minecraft will only show you stuff within 60 blocks of the armor stand.
# if building tall structures, it's better for the armor stand to be more centered.
# by default, I set it to 0. the first 50 layers in the texture map (it's a 10x10 array)
# are negative layers and a height adjustment of 0 should have layers starting at 50
height_adjustment = 0

if (yh>30):
    print("height is {}. some layers will be below the armor stand. this is done for designs taller than 30".format(yh))
    height_adjustment = int(yh/2)

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



for (x,y,z) in points:

    # the matmul operation yields floats.
    x = int(x)
    y = int(y)
    z = int(z)

    # we want to center the object in x,z
    x = x - center[0] + int(texture_size/2)
    #y = y - center[1] + int(texture_size/2)
    z = z - center[2] + int(texture_size/2)


    y = y - height_adjustment

    # I'm adding 5 so I can have negative layers.
    x = x + (5+int(y/10))*texture_size
    z = z + (y%10)*texture_size

    # if not y in colors:
    #     # color plus alpha/transparency
    #     colors[y] = ImageColor.getrgb(random.choice(list(ImageColor.colormap.values()))) + (128,)

    image.putpixel((x,z), ImageColor.getrgb(pallette[y])+(128,))


image.save("gened.png")
