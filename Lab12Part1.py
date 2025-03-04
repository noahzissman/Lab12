from mcpi_addons.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("Hello World!")

x = int(input("X Coordinate: "))
y = int(input("Y Coordiante: "))
z = int(input("Z Coordinate: "))

width = 5
height = 4
length = 5

mc.setBlocks(x, y, z, x + width, y + height, z + length, 3)
mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height -1, z + length -1, 0) 

