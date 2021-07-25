This is a minecraft resource pack to assist in building structures from 3d models.

It involves the following steps:
* find an stl/obj file from thingiverse, fusion360...
* voxelize it at this website: https://drububu.com/miscellaneous/voxelizer/?out=jso and generate a json file
* run the script in the python directory of this pack:
** python/genimage.py -voxel_path <path to the json file>
* move the resulting gened.png file into the textures directory
* copy the whole pack into /storage/emulated/0/games/com.mojang/development_resource_packs
* activate the pack
* in minecraft, create an armor stand, give it a banner, and iterate through the poses. The guidance objects show show up after the chunk borders.


To write this I started with Foxy's Markers [Experimental] resource pack
# Created: 22/05/2021 [dd/mm/YYYY]
# Version: 1.0.2
# Made for MC Bedrock Edition 1.16.220+
# For more info visit https://www.foxynotail.com
#


Much of this code is lifted from foxynotail's markers addon.


if your 3d file is the wrong orientation, you can rotate in incremenst of 90 along each axis by adding this option
    -rotate xxyz
this example rotates twice by 90 on x axis, then on y and last on z.

