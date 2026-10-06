import cv2
from PIL import Image

def img_to_ascii(image_path="data/processed_avatar.png", width=65):
    img = Image.open(image_path).convert("L")
    w, h = img.size
    aspect_ratio = h / w
    new_height = int(width * aspect_ratio * 0.55)
    img = img.resize((width, new_height))
    
    chars = "@%#*+=-:. "
    pixels = img.getdata()
    ascii_str = "".join([chars[pixel * len(chars) // 256] for pixel in pixels])
    
    lines = [ascii_str[i:i+width] for i in range(0, len(ascii_str), width)]
    return "\n".join(lines)

def generate_svg():
    ascii_art = img_to_ascii()
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 650" width="100%" height="100%">
  <style>
    .terminal-bg {{ fill: #0d1117; }}
    .terminal-header {{ fill: #161b22; }}
    .dot {{ r: 6; }}
    .text {{ fill: #58a6ff; font-family: 'Courier New', monospace; font-size: 13px; }}
  </style>
  <rect width="600" height="650" rx="10" class="terminal-bg"/>
  <rect width="600" height="40" rx="10" class="terminal-header"/>
  <circle cx="20" cy="20" fill="#ff5f56" class="dot"/>
  <circle cx="40" cy="20" fill="#ffbd2e" class="dot"/>
  <circle cx="60" cy="20" fill="#27c93f" class="dot"/>
  <text x="300" y="25" text-anchor="middle" fill="#8b949e" font-family="sans-serif" font-size="12">akin@terminal: ~</text>
  <text x="30" y="70" class="text"><tspan fill="#3fb950">akin@dev</tspan>:<tspan fill="#58a6ff">~</tspan>$ python render_avatar.py</text>
  <text x="30" y="110" font-family="monospace" font-size="9" fill="#00ff66" xml:space="preserve">{ascii_art}</text>
</svg>"""
    
    with open("akin-ascii.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("akin-ascii.svg oluşturuldu.")

if __name__ == "__main__":
    generate_svg()