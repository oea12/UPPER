import os

def generate_html_for_image(image_path, folder_name):
    image_name = os.path.basename(image_path)
    html_template = f"""
<div class="grid-item running trainer" data-pg-collapsed> 
    <div class="gallery-item"> 
        <div class="gallery-thumb"> 
            <img src="assets/images/gallery/{folder_name}/{image_name}" alt="gallery"> 
            <div class="gallery-overlay"> 
                <div class="gallery-content"> 
                    <h4 class="title">{folder_name}</h4> 
                    <div class="gallery-icon"> <a class="img-popup" data-rel="lightcase:myCollection" href="assets/images/gallery/{folder_name}/{image_name}"><img src="assets/images/icon/icon-47.png" alt="gallery"></a> 
                    </div>                     
                </div>                 
            </div>             
        </div>         
    </div>     
</div>
"""
    return html_template

root_folder = r'C:\Users\oea1_\Casa Armando Guillermo\Upper\sword-mixed-boxing-martial-arts-html-template-2022-09-17-07-38-53-utc\Sword-HTML-Placeholder\UPPER\assets\images\gallery'

for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)
    if os.path.isdir(folder_path):
        output_file = os.path.join(folder_path, f"{folder_name}_html_output.txt")
        with open(output_file, 'w') as file:
            for image_file in os.listdir(folder_path):
                if image_file.endswith(('.png', '.jpg', '.jpeg')):  # Asegúrate de incluir los formatos de imagen que usas
                    image_path = os.path.join(folder_path, image_file)
                    html_code = generate_html_for_image(image_path, folder_name)
                    file.write(html_code + "\n\n")
        print(f"HTML generado para {folder_name} guardado en {output_file}")
