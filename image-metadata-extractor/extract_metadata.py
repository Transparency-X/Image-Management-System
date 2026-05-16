import os
import zipfile
import sqlite3
import csv
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import argparse

def get_image_metadata(file_path):
    """Extract metadata from an image file."""
    try:
        with Image.open(file_path) as img:
            metadata = {
                "File Name": os.path.basename(file_path),
                "File Size (bytes)": os.path.getsize(file_path),
                "Format": img.format,
                "Mode": img.mode,
                "Width": img.width,
                "Height": img.height,
            }

            # Extract EXIF data
            exif_data = img._getexif() or {}
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                metadata[f"EXIF_{tag_name}"] = str(value)

            # Extract GPS data if available
            if 'GPSInfo' in exif_data:
                gps_info = {}
                for key in exif_data['GPSInfo'].keys():
                    gps_tag = GPSTAGS.get(key, key)
                    gps_info[gps_tag] = exif_data['GPSInfo'][key]
                metadata["GPS"] = str(gps_info)

            return metadata
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def process_folder(folder_path, output_csv=None, output_db=None):
    """Process all images in a folder."""
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    all_metadata = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(image_extensions):
                file_path = os.path.join(root, file)
                metadata = get_image_metadata(file_path)
                if metadata:
                    all_metadata.append(metadata)

    save_results(all_metadata, output_csv, output_db)

def process_zip(zip_path, output_csv=None, output_db=None):
    """Process all images in a ZIP file."""
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    all_metadata = []

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.lower().endswith(image_extensions):
                # Extract to temp directory
                temp_dir = "temp_extract"
                os.makedirs(temp_dir, exist_ok=True)
                zip_ref.extract(file, temp_dir)
                file_path = os.path.join(temp_dir, file)
                metadata = get_image_metadata(file_path)
                if metadata:
                    all_metadata.append(metadata)
                # Clean up
                os.remove(file_path)
        os.rmdir(temp_dir)

    save_results(all_metadata, output_csv, output_db)

def save_results(metadata_list, output_csv, output_db):
    """Save metadata to CSV and/or SQLite3."""
    if not metadata_list:
        print("No metadata to save.")
        return

    # Save to CSV
    if output_csv:
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=metadata_list[0].keys())
            writer.writeheader()
            writer.writerows(metadata_list)
        print(f"Metadata saved to CSV: {output_csv}")

    # Save to SQLite3
    if output_db:
        conn = sqlite3.connect(output_db)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS image_metadata")
        cursor.execute(f"CREATE TABLE image_metadata ({', '.join([f'{key} TEXT' for key in metadata_list[0].keys()])})")
        for metadata in metadata_list:
            cursor.execute(f"INSERT INTO image_metadata VALUES ({', '.join(['?'] * len(metadata))})", tuple(metadata.values()))
        conn.commit()
        conn.close()
        print(f"Metadata saved to SQLite3: {output_db}")

def main():
    parser = argparse.ArgumentParser(description="Extract image metadata from a folder or ZIP file.")
    parser.add_argument("--folder", help="Path to the folder containing images.")
    parser.add_argument("--zip", help="Path to the ZIP file containing images.")
    parser.add_argument("--csv", help="Output CSV file path (e.g., output.csv).")
    parser.add_argument("--db", help="Output SQLite3 database path (e.g., output.db).")
    args = parser.parse_args()

    if args.folder:
        process_folder(args.folder, args.csv, args.db)
    elif args.zip:
        process_zip(args.zip, args.csv, args.db)
    else:
        print("Please specify either --folder or --zip.")

if __name__ == "__main__":
    main()
