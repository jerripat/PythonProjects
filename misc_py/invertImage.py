from PIL import Image, ImageChops

image = Image.open("Images/EmpireState.jpg")
inverted_image = ImageChops.invert(Image)
inverted_image.save("inverted_ESB.jpg")
