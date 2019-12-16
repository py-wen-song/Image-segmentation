from PIL import Image
def image_contrast(img1):
  image1 = Image.open(img1).convert("L")
  image1.save(img1)
if __name__ == '__main__':
    image_contrast('1_1.png')
