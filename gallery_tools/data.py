import json
import os

from gallery_tools.config import INPUT_DIR

INPUT_JSON = os.path.join(INPUT_DIR, "data.json")


def generate_data_json(large_dir, thumb_dir, output_json_path):
    # Загружаем описания из входного JSON
    descriptions = {}
    if os.path.exists(INPUT_JSON):
        with open(INPUT_JSON, "r", encoding="utf-8") as f:
            meta_data = json.load(f)
            for item in meta_data:
                descriptions[item["id"]] = {
                    "date": item.get("date", ""),
                    "description": item.get("description", "")
                }

    data = []

    for file_name in sorted(os.listdir(large_dir)):
        if not file_name.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            continue

        image_id = os.path.splitext(file_name)[0].replace("-large", "")

        large_path = os.path.join(large_dir, file_name)
        thumb_file = file_name.replace("-large", "-thumb")
        thumb_path = os.path.join(thumb_dir, thumb_file)

        desc_data = descriptions.get(image_id, {"date": "", "description": ""})

        data.append({
            "id": image_id,
            "src": f"images_large/{file_name}",
            "msrc": f"images_thumb/{thumb_file}",
            "date": desc_data["date"],
            "description": desc_data["description"]
        })

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ JSON с данными сохранён в {output_json_path}")
