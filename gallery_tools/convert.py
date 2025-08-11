from PIL import Image
import os

def prepare_image(input_path, output_large_path, output_thumb_path,
                  large_max_size=(1200, 900), thumb_size=(200, 150)):
    with Image.open(input_path) as img:
        # Большое изображение
        img_large = img.copy()
        img_large.thumbnail(large_max_size, Image.Resampling.LANCZOS)
        os.makedirs(os.path.dirname(output_large_path), exist_ok=True)
        img_large.save(output_large_path, "JPEG", quality=90)

        # Миниатюра с обрезкой по центру
        thumb = img.copy()
        thumb_ratio = thumb_size[0] / thumb_size[1]
        img_ratio = thumb.width / thumb.height

        if img_ratio > thumb_ratio:
            new_height = thumb_size[1]
            new_width = int(new_height * img_ratio)
        else:
            new_width = thumb_size[0]
            new_height = int(new_width / img_ratio)

        thumb = thumb.resize((new_width, new_height), Image.Resampling.LANCZOS)

        left = (new_width - thumb_size[0]) // 2
        top = (new_height - thumb_size[1]) // 2
        right = left + thumb_size[0]
        bottom = top + thumb_size[1]

        thumb = thumb.crop((left, top, right, bottom))
        os.makedirs(os.path.dirname(output_thumb_path), exist_ok=True)
        thumb.save(output_thumb_path, "JPEG", quality=90)


def process_folder(input_folder, output_folder_large, output_folder_thumb,
                   large_max_size=(1200, 900), thumb_size=(200, 150)):
    os.makedirs(output_folder_large, exist_ok=True)
    os.makedirs(output_folder_thumb, exist_ok=True)

    valid_exts = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
    for file in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file)
        if os.path.isfile(input_path) and file.lower().endswith(valid_exts):
            name, _ = os.path.splitext(file)
            output_large_path = os.path.join(output_folder_large, f"{name}-large.jpg")
            output_thumb_path = os.path.join(output_folder_thumb, f"{name}-thumb.jpg")

            print(f"Обрабатываю {input_path}...")
            prepare_image(input_path, output_large_path, output_thumb_path,
                          large_max_size=large_max_size, thumb_size=thumb_size)
    print("✅ Обработка завершена.")
