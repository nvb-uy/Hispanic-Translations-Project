import os
import json
import shutil
import zipfile

# --------------------------------------------------------------------------------------------------------------- #

languages = ['es_es', 'es_ar', 'es_uy', 'es_cl', 'es_mx', 'es_ve']

mcmeta_content = {
    "pack": {
        "pack_format": 10,
        "description": "%NAME Spanish Language Pack by Hispanic Translation Team"
    }
}

translations_dir = './src/translations'
output_dir = './build/out'
pack_image_path = './resources/pack.png'

slang_languages = ["es_ar", "es_uy", "es_cl", "es_mx"]

slang_replacements = [
        ("Peto", "Pechera"),
        ("Leotardo", "Pantalones"),
        ("Rodillera", "Bota"),
        ("Coger", "Agarrar")
]

aruy_replacements = [
        ("Losa", "Baldosa"),
        ("Cristal", "Vidrio"),
        ("Píldora", "Pastilla"),

        (" tienes", " tenés"),
        (" quieres ", " querés"),
        (" vosotros", " ustedes"),
        (" tú", " vos")
]

# --------------------------------------------------------------------------------------------------------------- #

def replaceSlang(text, replacements):
    for slang, replacement in replacements:
        text = text.replace(slang, replacement)
    return text

def create_resource_pack(json_file, total_files, current_index):
    base_path = './src/translations/'
    pack_name = json_file.split('.')[0]
    pack_dir = f'./{pack_name}'

    mcmeta_content['pack']['description'] = mcmeta_content['pack']['description'].replace('%NAME', pack_name.capitalize())

    lang_dir = f'{pack_dir}/assets/{pack_name}/lang'
    os.makedirs(lang_dir, exist_ok=True)

    print(f"Processing '{json_file}'...")

    with open(f'{base_path}{json_file}', 'r', encoding='utf-8') as file:
        content = json.load(file)

    translation_version = content.get("htp_metadata_version", "unknown")
    credits = content.get("htp_metadata_credits", "This translation was made by the HTP (Hispanic Translations Project) Team")

    for lang in languages:
        lang_content = content

        if lang in slang_languages:
            for key, value in lang_content.items():
                if isinstance(value, str):
                    if lang == "es_ar" or lang == "es_uy":
                        value = replaceSlang(value, aruy_replacements)

                    lang_content[key] = replaceSlang(value, slang_replacements)
        
        with open(f'{lang_dir}/{lang}.json', 'w', encoding='utf-8') as lang_file:
            json.dump(content, lang_file, ensure_ascii=False, indent=4)
        print(f"[{json_file}] Written language file for {lang}")

    with open(f'{pack_dir}/pack.mcmeta', 'w', encoding='utf-8') as mcmeta_file:
        json.dump(mcmeta_content, mcmeta_file, ensure_ascii=False, indent=4)

    with open(f'{pack_dir}/CREDITS.txt', 'w', encoding='utf-8') as credits_file:
        credits_file.write(credits)

    if os.path.exists(pack_image_path):
        shutil.copy(pack_image_path, pack_dir)

    zip_file_path = f'{output_dir}/HTP-{pack_name.capitalize()}-TranslationPack-v{translation_version}.zip'
    zipf = zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(pack_dir):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, pack_dir))

    zipf.close()
    shutil.rmtree(pack_dir)

    percentage_done = (current_index + 1) / total_files * 100
    print(f"Completed '{json_file}'. Progress: {percentage_done:.2f}%")

# --------------------------------------------------------------------------------------------------------------- #

os.makedirs(output_dir, exist_ok=True)

json_files = [f for f in os.listdir(translations_dir) if f.endswith('.json')]
total_files = len(json_files)

for index, file in enumerate(json_files):
    create_resource_pack(file, total_files, index)