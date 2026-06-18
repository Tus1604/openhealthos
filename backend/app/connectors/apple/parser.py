import os
import sys
import zipfile
import xml.etree.ElementTree as ET

def parse_apple_health_xml(file_path):
    print(f"Opening XML file: {file_path}...")
    tree = ET.parse(file_path)
    root = tree.getroot()

    print("Extracting Records...")
    for record in root.findall('Record'):
        record_type = record.get('type')
        if record_type == "HKQuantityTypeIdentifierStepCount":
            source = record.get('sourceName')
            value = record.get('value')
            date = record.get('startDate')
            print(f"Found Steps: {value} steps on {date} from {source}")

    print("\nExtracting Workouts...")
    for workout in root.findall('Workout'):
        activity_type = workout.get('workoutActivityType')
        duration = workout.get('duration')
        source = workout.get('sourceName')
        print(f"Found Workout: {activity_type} for {duration} mins from {source}")

def unzip_and_parse(zip_path, extract_to):
    print(f"Unzipping {zip_path} to {extract_to}...")
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extract('apple_health_export/export.xml', extract_to)

    extracted_xml_path = os.path.join(extract_to, 'apple_health_export/export.xml')
    parse_apple_health_xml(extracted_xml_path)

def create_dummy_zip_if_missing(zip_path, xml_source_path):
    if not os.path.exists(zip_path):
        print(f"No zip found. Auto-creating a test zip at {zip_path}...")
        os.makedirs(os.path.dirname(zip_path), exist_ok=True)
        with zipfile.ZipFile(zip_path, 'w') as zip_ref:
            zip_ref.write(xml_source_path, 'apple_health_export/export.xml')

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    if len(sys.argv) > 1:
        zip_file_path = sys.argv[1]
    else:
        zip_file_path = os.path.join(current_dir, "../../../test_data/export.zip")

        default_xml_source = os.path.join(current_dir, "../../../test_data/apple_sample.xml")
        create_dummy_zip_if_missing(zip_file_path, default_xml_source)
        
    temp_extract_dir = os.path.join(current_dir, "../../../test_data/temp")
    
    unzip_and_parse(zip_file_path, temp_extract_dir)