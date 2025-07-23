`pdf-content-analysis-ai`

---

### `README.md`

```markdown
# 📄 PDF Content Analysis and Question Generation using Python

This project is a Python-based tool that extracts both **text** and **images** from a PDF file—particularly educational PDFs—and generates a structured JSON output. It is designed as part of an **AI/Python Intern Assignment** for content analysis and question preparation based on visuals.

---

## 📌 Features

- ✅ Extracts all **text content** from each PDF page
- 🖼️ Extracts and saves all **images** from each page
- 📁 Creates an **organized `images/` folder**
- 📦 Generates a structured **`output.json`** file containing:
  - Page number
  - Extracted text
  - Question image path
  - Option image paths (if available)

---

## 📁 Folder Structure

```

pdf-content-analysis-ai/
├── input.pdf                 # PDF file to be analyzed
├── main.py                   # Main Python script
├── output.json               # JSON file generated after running the script
├── images/                   # Folder where extracted images will be stored
├── requirements.txt          # Required Python libraries
├── .gitignore                # Ignore files/folders from GitHub
└── README.md                 # This file

````

---

## 🖥️ How to Run

### 1. 🔧 Install Required Library

```bash
pip install -r requirements.txt
````

### 2. 📌 Rename your PDF to `input.pdf`

Place it in the root folder of the project.

### 3. 🚀 Run the Script

```bash
python main.py
```

---

## 📄 Sample `output.json`

```json
[
  {
    "page_number": 1,
    "text": "Q1. What comes next?",
    "question": "images/page1_image1.png",
    "option_images": [
      "images/page1_image2.png",
      "images/page1_image3.png"
    ]
  },
  {
    "page_number": 2,
    "text": "Q2. Count the objects.",
    "question": "images/page2_image1.png",
    "option_images": []
  }
]
```

---

## 🧠 Technologies Used

* Python
* [PyMuPDF](https://pymupdf.readthedocs.io/) (`fitz`)

---

## 🙋‍♀️ Author

**Apeksha Chandak**
B.Tech in Artificial Intelligence and Machine Learning
[GitHub: @apekshachandak1](https://github.com/apekshachandak1)

---

## 📜 License

This project is for academic and learning purposes.

````

---
