import os
import json
from PIL import Image

# Папка с большими картинками
large_dir = "output_images_large"
thumb_dir = "output_images_thumb"
output_json = "data.json"

data = []

for filename in sorted(os.listdir(large_dir)):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        continue

    large_path = os.path.join(large_dir, filename)
    thumb_path = os.path.join(thumb_dir, filename.replace("-large", "-thumb"))

    if not os.path.exists(thumb_path):
        print(f"⚠ Миниатюра для {filename} не найдена, пропускаю.")
        continue

    with Image.open(large_path) as img:
        width, height = img.size

    data.append({
        "src": large_path.replace("\\", "/"),
        "msrc": thumb_path.replace("\\", "/"),
        "w": width,
        "h": height
    })

# Сохраняем JSON
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Сохранено {len(data)} записей в {output_json}")
