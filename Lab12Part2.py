from mcpi_addons.minecraft import Minecraft

mc = Minecraft.create()
import time

for _ in range(30):

    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y -1, pos.z, 12)
    time.sleep(1)

