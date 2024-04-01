import csv
import json
import os

def generate_qa_pairs_to_jsonl(csv_file):
    jsonl_file = os.path.splitext(csv_file)[0] + ".jsonl"

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        with open(jsonl_file, 'w') as jsonl_out:
            for row in reader:
                route_name = row['route_name']
                route_miles = row['route_miles']
                avg_ridership = row['avg_ridership']

                qa_dict = {
                    "messages": [
                        {"role": "system", "content": f"Route miles for {route_name} Metra route:"},
                        {"role": "assistant", "content": route_miles},
                        {"role": "system", "content": f"Average ridership for {route_name} Metra route:"},
                        {"role": "assistant", "content": avg_ridership}
                    ]
                }
                jsonl_out.write(json.dumps(qa_dict) + '\n')

generate_qa_pairs_to_jsonl('Metra_Ridership.csv')
