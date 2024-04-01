import csv
import json
import os

def generate_qa_pairs_to_jsonl(csv_file):
    jsonl_file = os.path.splitext(csv_file)[0] + ".jsonl"

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        with open(jsonl_file, 'w') as jsonl_out:
            for row in reader:
                id_ = row['ID ']
                location_address = row['Traffic Volume Count Location  Address']
                street = row['Street']
                date_of_count = row['Date of Count']
                total_passing_vehicle_volume = row['Total Passing Vehicle Volume']
                vehicle_volume_by_direction = row['Vehicle Volume By Each Direction of Traffic']
                latitude = row['Latitude']
                longitude = row['Longitude']
                location = row['Location']

                json_obj = {
                    "messages": [
                        {"role": "system", "content": f"ID: {id_}"},
                        {"role": "assistant", "content": f"Location Address: {location_address}"},
                        {"role": "assistant", "content": f"Street: {street}"},
                        {"role": "assistant", "content": f"Date of Count: {date_of_count}"},
                        {"role": "assistant", "content": f"Total Passing Vehicle Volume: {total_passing_vehicle_volume}"},
                        {"role": "assistant", "content": f"Vehicle Volume By Each Direction of Traffic: {vehicle_volume_by_direction}"},
                        {"role": "assistant", "content": f"Latitude: {latitude}"},
                        {"role": "assistant", "content": f"Longitude: {longitude}"},
                        {"role": "assistant", "content": f"Location: {location}"}
                    ]
                }
                jsonl_out.write(json.dumps(json_obj) + '\n')

generate_qa_pairs_to_jsonl('Average_Daily_Traffic_Counts_20240324.csv')
