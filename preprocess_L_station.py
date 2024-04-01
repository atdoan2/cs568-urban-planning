import csv
import json
import os

def generate_qa_pairs_to_jsonl(csv_file):
    jsonl_file = os.path.splitext(csv_file)[0] + ".jsonl"

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        with open(jsonl_file, 'w') as jsonl_out:
            for row in reader:
                station_id = row['station_id']
                station_name = row['stationame']
                month_beginning = row['month_beginning']
                avg_weekday_rides = row['avg_weekday_rides']
                avg_saturday_rides = row['avg_saturday_rides']
                avg_sunday_holiday_rides = row['avg_sunday-holiday_rides']
                month_total = row['monthtotal']

                qa_dict = {
                    "messages": [
                        {"role": "system", "content": f"Average weekday ridership at {station_name} in {month_beginning}:"},
                        {"role": "assistant", "content": avg_weekday_rides},
                        {"role": "system", "content": f"Average Saturday ridership at {station_name} in {month_beginning}:"},
                        {"role": "assistant", "content": avg_saturday_rides},
                        {"role": "system", "content": f"Average Sunday and holiday ridership at {station_name} in {month_beginning}:"},
                        {"role": "assistant", "content": avg_sunday_holiday_rides},
                        {"role": "system", "content": f"Total ridership at {station_name} in {month_beginning}:"},
                        {"role": "assistant", "content": month_total}
                    ]
                }
                jsonl_out.write(json.dumps(qa_dict) + '\n')

generate_qa_pairs_to_jsonl('CTA_-_Ridership_-__L__Station_Entries_-_Monthly_Day-Type_Averages___Totals_20240324.csv')
