import json
import os
import shutil

from gallery_tools.config import TEMPLATES_DIR


def build_site(data_json_path, template_html_path, output_html_path):
    # 1. Загружаем список изображений
    with open(data_json_path, "r", encoding="utf-8") as f:
        items = json.load(f)

    # 2. Генерируем HTML-элементы галереи
    gallery_items_html = "\n".join(
        f'<img src="{item["msrc"]}" '
        f'data-full="{item["src"]}" '
        f'data-desc="{item.get("description", "")}">'
        for item in items
    )

    # 3. Читаем шаблон
    with open(template_html_path, "r", encoding="utf-8") as f:
        template_html = f.read()

    # 4. Подставляем данные
    result_html = template_html.replace("{{GALLERY_ITEMS}}", gallery_items_html)

    # 5. Создаём папки и копируем css и js
    output_dir = os.path.dirname(output_html_path)
    css_src = os.path.join(TEMPLATES_DIR, "css")
    js_src = os.path.join(TEMPLATES_DIR, "js")
    css_dst = os.path.join(output_dir, "css")
    js_dst = os.path.join(output_dir, "js")

    if os.path.exists(css_dst):
        shutil.rmtree(css_dst)
    shutil.copytree(css_src, css_dst)

    if os.path.exists(js_dst):
        shutil.rmtree(js_dst)
    shutil.copytree(js_src, js_dst)

    # 6. Записываем итоговый HTML
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(result_html)

    print(f"✅ Сайт собран в {output_dir}")
