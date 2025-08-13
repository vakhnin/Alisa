import json
import os

from PIL import Image


def generate_data_json(large_dir, thumb_dir, output_json):
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

        caption = "caption"

        data.append({
            "src": f"images_large/{filename}",
            "msrc": f"images_thumb/{filename.replace('-large', '-thumb')}",
            "w": width,
            "h": height,
            "description": caption
        })

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Сохранено {len(data)} записей в {output_json}")
