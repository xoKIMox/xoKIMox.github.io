import diffusers
from PIL import Image, ImageDraw, ImageFont
def text_to_image(text, diffuser_modle):
    diffuser = diffusers.loaf_diffuser(diffuser_model)
    image_data = diffuser.generate(text)
    image = Image.fromarray(image_data)
    image.show()
    
if __name__ == "__main__":
    input_text = "Hello world"
    diffuser_model = "example_diffuser_model"
    text_to_image(input, diffuser_model)
