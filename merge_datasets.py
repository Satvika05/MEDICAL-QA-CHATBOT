import json
import os

merged_data = []

# List of JSON files to merge
json_files = [
    '1_CancerGov_QA.json',
    '2_GARD_QA.json',
    '3_GHR_QA.json',
    # Add other JSON files as needed
]

for file_name in json_files:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            question = item.get('question')
            context = item.get('context')
            if question and context:
                merged_data.append({
                    'question': question,
                    'context': context
                })

# Save the merged data to a new JSON file
with open('medquad_cleaned.json', 'w', encoding='utf-8') as outfile:
    json.dump(merged_data, outfile, indent=2)
