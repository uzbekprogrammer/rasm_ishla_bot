import cv2


async def pencil_sketch(photo_name):
    image = cv2.imread(photo_name)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch1 = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    cv2.waitKey(0)
    cv2.imwrite(f'{photo_name}', pencil_sketch1)


# if __name__ == "__main__":
#     photos = [
#         'xoxo.xo_05.png',
#         'xoxo.xo_04.png',
#         'xoxo.xo_01.png',
#         'xoxo.xo_02.png',
#         'xoxo.xo_03.png',
#         'xoxo.xo_06.png',
#         'xoxo.xo_07.png',
#         'xoxo.xo_08.png',
#         'xoxo.xo_09.png'
#         ]
#     for photo in photos:
#         pencil_sketch(photo)
#         os.remove(f'{photo}.jpg')
