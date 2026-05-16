# Image Metadata Extractor

A Python script to extract metadata (name, size, EXIF, GPS, etc.) from images in a folder or ZIP file, and save the results to **CSV** or **SQLite3** for analysis.

---

## **✨ Features**
- Extracts metadata from **JPG, PNG, GIF, BMP, TIFF, WebP**.
- Supports **folders** and **ZIP files**.
- Outputs to **CSV** and/or **SQLite3**.
- Uses **Pillow (PIL)** for reliable metadata extraction.

---

## **📦 Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/image-metadata-extractor.git
cd image-metadata-extractor
```

### **2. Set Up a Virtual Environment (Recommended)**
```bash
python -m venv venv
```

- **Activate the virtual environment:**
  - **Windows:**
    ```bash
    venv\Scripts\activate
    ```
  - **macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```
*If `requirements.txt` does not exist, create it with:*
```bash
echo "Pillow" > requirements.txt
pip install -r requirements.txt
```

---

## **🚀 Usage**

### **Basic Usage**
Run the script with a **folder** or **ZIP file** as input:

#### **For a Folder:**
```bash
python extract_metadata.py --folder /path/to/images --csv output.csv --db output.db
```

#### **For a ZIP File:**
```bash
python extract_metadata.py --zip /path/to/images.zip --csv output.csv --db output.db
```

### **Arguments**
| Argument | Description | Required |
|----------|-------------|----------|
| `--folder` | Path to the folder containing images. | No (either `--folder` or `--zip` is required) |
| `--zip` | Path to the ZIP file containing images. | No (either `--folder` or `--zip` is required) |
| `--csv` | Output CSV file path (e.g., `output.csv`). | No |
| `--db` | Output SQLite3 database path (e.g., `output.db`). | No |

---

## **📂 Example Outputs**
- **CSV:** A table with columns for file name, size, format, dimensions, and all extracted metadata (EXIF, GPS, etc.).
- **SQLite3:** A database table with the same data, named `image_metadata`.

---

## **📜 License**
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
```

---

---

## **2. Release Template (for GitHub Releases)**

---

**Tag:** `v1.0.0`
**Title:** `Initial Release: Image Metadata Extractor`

---

### **📌 What’s New**
- First stable release of the **Image Metadata Extractor**.
- Extracts metadata from **JPG, PNG, GIF, BMP, TIFF, WebP** files.
- Supports **folders** and **ZIP files**.
- Outputs to **CSV** and/or **SQLite3**.

---

### **📥 Downloads**
- **[Source Code (zip)](https://github.com/your-username/image-metadata-extractor/archive/refs/tags/v1.0.0.zip)**
- **[Source Code (tar.gz)](https://github.com/your-username/image-metadata-extractor/archive/refs/tags/v1.0.0.tar.gz)**

---

### **🛠️ Setup Instructions**

#### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/image-metadata-extractor.git
cd image-metadata-extractor
```

#### **2. Set Up a Virtual Environment**
```bash
python -m venv venv
```
- **Activate:**
  - **Windows:** `venv\Scripts\activate`
  - **macOS/Linux:** `source venv/bin/activate`

#### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **4. Run the Script**
```bash
python extract_metadata.py --folder /path/to/images --csv output.csv --db output.db
```
or for a ZIP file:
```bash
python extract_metadata.py --zip /path/to/images.zip --csv output.csv --db output.db
```

---
---

### **📝 Notes**
- Tested on **Python 3.8+**.
- Requires **Pillow** (`pip install Pillow`).
- For **GPS metadata**, ensure images contain EXIF GPS tags.

---
---
---

### **📁 Repository Structure**
```
image-metadata-extractor/
│
├── extract_metadata.py    # Main script
├── requirements.txt       # Dependencies
├── README.md              # This file
└── LICENSE                # License file
```
