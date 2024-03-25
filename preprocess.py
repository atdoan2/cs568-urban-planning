import csv
import json

# Define questions related to crash attributes
questions = {
    "CRASH_DATE": "When did the crash occur?",
    "POSTED_SPEED_LIMIT": "What was the posted speed limit during the crash?",
    "TRAFFIC_CONTROL_DEVICE": "What type of traffic control device was present?",
    "DEVICE_CONDITION": "What was the condition of the traffic control device?",
    "WEATHER_CONDITION": "What was the weather condition during the crash?",
    "LIGHTING_CONDITION": "What was the lighting condition during the crash?",
    "FIRST_CRASH_TYPE": "What was the first crash type?",
    "TRAFFICWAY_TYPE": "What type of traffic way was involved?",
    "LANE_CNT": "How many lanes were there?",
    "ALIGNMENT": "What was the alignment of the road?",
    "ROADWAY_SURFACE_COND": "What was the condition of the roadway surface?",
    "ROAD_DEFECT": "Was there any road defect?",
    "REPORT_TYPE": "What was the report type?",
    "CRASH_TYPE": "What was the crash type?",
    "INTERSECTION_RELATED_I": "Was the crash intersection-related?",
    "NOT_RIGHT_OF_WAY_I": "Was the crash not right of way?",
    "HIT_AND_RUN_I": "Was it a hit-and-run?",
    "DAMAGE": "What was the extent of damage?",
    "PRIM_CONTRIBUTORY_CAUSE": "What was the primary contributory cause?",
    "SEC_CONTRIBUTORY_CAUSE": "What was the secondary contributory cause?",
    "STREET_NO": "What was the street number?",
    "STREET_DIRECTION": "What was the street direction?",
    "STREET_NAME": "What was the street name?",
    "BEAT_OF_OCCURRENCE": "What was the beat of occurrence?",
    "PHOTOS_TAKEN_I": "Were photos taken?",
    "STATEMENTS_TAKEN_I": "Were statements taken?",
    "DOORING_I": "Was there any dooring?",
    "WORK_ZONE_I": "Was there any work zone?",
    "WORK_ZONE_TYPE": "What was the type of work zone?",
    "WORKERS_PRESENT_I": "Were workers present?",
    "NUM_UNITS": "How many units were involved?",
    "MOST_SEVERE_INJURY": "What was the most severe injury?",
    "INJURIES_TOTAL": "How many total injuries were there?",
    "INJURIES_FATAL": "How many fatal injuries were there?",
    "INJURIES_INCAPACITATING": "How many incapacitating injuries were there?",
    "INJURIES_NON_INCAPACITATING": "How many non-incapacitating injuries were there?",
    "INJURIES_REPORTED_NOT_EVIDENT": "How many injuries were reported but not evident?",
    "INJURIES_NO_INDICATION": "How many injuries had no indication?",
    "INJURIES_UNKNOWN": "How many injuries were unknown?",
    "CRASH_HOUR": "What hour did the crash occur?",
    "CRASH_DAY_OF_WEEK": "What day of the week did the crash occur?",
    "CRASH_MONTH": "What month did the crash occur?",
    "LATITUDE": "What was the latitude of the crash location?",
    "LONGITUDE": "What was the longitude of the crash location?",
    "LOCATION": "Where did the crash occur?",
    "Boundaries - ZIP Codes": "What was the ZIP code boundary?",
}

# Load data from CSV file and create input-output pairs
input_output_pairs = []
with open("Traffic_Crashes_-_Crashes_20240317.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for attribute, question in questions.items():
            input_output_pairs.append({
                "input": f"{question} ({row['CRASH_RECORD_ID']})",
                "output": f"{attribute}: {row[attribute]}"
            })

# Save input-output pairs to a JSON file
with open("input_output_pairs.json", "w") as outfile:
    json.dump(input_output_pairs, outfile, indent=4)

print("Input-output pairs saved to input_output_pairs.json.")
