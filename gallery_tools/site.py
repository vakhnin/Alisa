import json


def build_site(data_json, template_file, output_html):
    with open(data_json, "r", encoding="utf-8") as f:
        images = json.load(f)

    with open(template_file, "r", encoding="utf-8") as f:
        template = f.read()

    # Генерация HTML миниатюр
    thumbs_html = "\n".join(
        f'<img src="{img["msrc"]}" data-full="{img["src"]}" '
        f'data-w="{img["w"]}" data-h="{img["h"]}" alt="">'
        for img in images
    )

    final_html = template.replace("{{GALLERY_ITEMS}}", thumbs_html)

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"✅ HTML сохранён в {output_html}")
