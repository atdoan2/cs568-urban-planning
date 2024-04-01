import csv
import json
import os

def generate_qa_pairs_to_jsonl(csv_file):
    jsonl_file = os.path.splitext(csv_file)[0] + ".jsonl"

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        with open(jsonl_file, 'w') as jsonl_out:
            for row in reader:
                route = row['route']
                route_name = row['routename']
                month_beginning = row['Month_Beginning']
                avg_weekday_rides = row['Avg_Weekday_Rides']
                avg_saturday_rides = row['Avg_Saturday_Rides']
                avg_sunday_holiday_rides = row['Avg_Sunday-Holiday_Rides']
                month_total = row['MonthTotal']

                # Create QA dictionary
                qa_dict = {
                    "messages": [
                        {"role": "system", "content": f"Average weekday ridership for route {route} ({route_name}) in {month_beginning}:"},
                        {"role": "assistant", "content": avg_weekday_rides},
                        {"role": "system", "content": f"Average Saturday ridership for route {route} ({route_name}) in {month_beginning}:"},
                        {"role": "assistant", "content": avg_saturday_rides},
                        {"role": "system", "content": f"Average Sunday and holiday ridership for route {route} ({route_name}) in {month_beginning}:"},
                        {"role": "assistant", "content": avg_sunday_holiday_rides},
                        {"role": "system", "content": f"Total ridership for route {route} ({route_name}) in {month_beginning}:"},
                        {"role": "assistant", "content": month_total}
                    ]
                }
                jsonl_out.write(json.dumps(qa_dict) + '\n')

generate_qa_pairs_to_jsonl('CTA_-_Ridership_-_Bus_Routes_-_Monthly_Day-Type_Averages___Totals_20240324.csv')
