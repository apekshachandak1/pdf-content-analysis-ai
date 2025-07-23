import fitz  # PyMuPDF
import os
import json

# Input PDF file
pdf_file = r"C:\PYTHON\PDF Content Analysis\IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf"

# Create output image folder
image_folder = r"C:\PYTHON\PDF Content Analysis\images"
os.makedirs(image_folder, exist_ok=True)

# Open PDF
doc = fitz.open(pdf_file)

output_data = []

for page_number in range(len(doc)):
    page = doc[page_number]
    text = page.get_text()
    
    # Extract images
    image_list = page.get_images(full=True)
    img_paths = []

    for img_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        img_name = f"page{page_number+1}_image{img_index}.{image_ext}"
        img_path = os.path.join(image_folder, img_name)
        
        with open(img_path, "wb") as img_file:
            img_file.write(image_bytes)
        img_paths.append(img_path)

    # For simplicity, assuming all images on page are question images and options
    # You can improve this based on coordinates or image size
    question_img = img_paths[0] if len(img_paths) >= 1 else ""
    option_imgs = img_paths[1:] if len(img_paths) > 1 else []

    page_data = {
        "page_number": page_number + 1,
        "text": text.strip(),
        "question": question_img,
        "option_images": option_imgs
    }
    output_data.append(page_data)

# Save output JSON
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=4)

print("✅ Extraction complete! Check 'images/' folder and 'output.json'")
