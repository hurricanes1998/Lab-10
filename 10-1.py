from PIL import Image
image = Image.open('1.jpg')
cropped = image.crop((500,0, 1050, 240))
cropped.save('lab10/cropped_image.png')