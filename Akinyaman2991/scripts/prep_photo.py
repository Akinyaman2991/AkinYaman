from PIL import Image
import sys, os

def process_photo(image_path, output_path="data/processed_avatar.png"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img = Image.open(image_path)
    img = img.resize((100, 100))
    img.save(output_path)
    print(f"processed successfully: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_photo(sys.argv[1])
    else:
        process_photo("source-photo.jpg")

