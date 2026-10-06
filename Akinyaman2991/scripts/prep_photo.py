import sys
from PIL import Image
from rembg import remove

def process_image(input_path, output_path="data/processed_avatar.png"):
    input_image = Image.open(input_path)
    # Arka planı otomatik temizle
    output_image = remove(input_image)
    output_image.save(output_path)
    print(processed successfully: {output_path})

if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_image(sys.argv[1])
    else:
        print("Lütfen bir kaynak fotoğraf belirtin.")