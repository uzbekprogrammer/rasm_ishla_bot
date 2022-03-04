from PIL import Image


async def white_black(inp):
    color_image = Image.open(inp)
    bw = color_image.convert('L')
    bw.save(inp)
