from PIL import Image

im = Image.open("png_test.png")
rgb_im = im.convert('RGB')
rgb_im.save('png_test.jpg')

