import random
import string
from captcha.image import ImageCaptcha

# Function to generate random CAPTCHA text
def generate_random_text(length=6):
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

# Create an image instance of the given size
image = ImageCaptcha(width=280, height=90)

# Generate random CAPTCHA text
captcha_text = generate_random_text()

# Generate the image of the given text
data = image.generate(captcha_text)

# Write the image to a file and save it
image.write(captcha_text, 'CAPTCHA.png')

# Read from image text
X = input("Enter text from the image captcha below:\n")

# Compare input with CAPTCHA text
if X == captcha_text:
    print("Verified")
else:
    print("Failed")
