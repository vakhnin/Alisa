import json
import os
import shutil

from gallery_tools.config import TEMPLATES_DIR


def build_site(data_json_path, template_html_path, output_html_path):
    # 1. Загружаем список изображений
    with open(data_json_path, "r", encoding="utf-8") as f:
        items = json.load(f)

    # 2. Загружаем переменные шаблона
    vars_path = os.path.join(TEMPLATES_DIR, "vars.json")
    if os.path.exists(vars_path):
        with open(vars_path, "r", encoding="utf-8") as f:
            vars_data = json.load(f)
    else:
        vars_data = {}

    # 3. Генерируем HTML-элементы галереи с description
    gallery_items_html = "\n".join(
        f'<div class="gallery-item">'
        f'  <img src="{item["msrc"]}" '
        f'       data-full="{item["src"]}" '
        f'       data-desc="{item.get("description", "")}">'
        f'  <div class="thumb-caption">{item.get("description", "")}</div>'
        f'</div>'
        for item in items
    )

    # 4. Читаем HTML-шаблон
    with open(template_html_path, "r", encoding="utf-8") as f:
        template_html = f.read()

    # 5. Подставляем переменные
    for key, value in vars_data.items():
        template_html = template_html.replace(f"{{{{{key}}}}}", value)

    # 6. Подставляем галерею
    result_html = template_html.replace("{{GALLERY_ITEMS}}", gallery_items_html)

    # 7. Копируем css и js в выходную папку
    output_dir = os.path.dirname(output_html_path)
    for folder in ["css", "js"]:
        src = os.path.join(TEMPLATES_DIR, folder)
        dst = os.path.join(output_dir, folder)
        if os.path.exists(dst):
            shutil.rmtree(dst)
        if os.path.exists(src):
            shutil.copytree(src, dst)

    # 8. Записываем готовый HTML
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(result_html)

    print(f"✅ Сайт собран в {output_dir}")
