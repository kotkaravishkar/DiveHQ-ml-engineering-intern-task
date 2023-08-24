
import csv

def process_csv_file(meeting_transcript):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
          
            action_item = {
                "text": row['text'],
                "assignee": row['speaker'],
                "ts": row['start_time']
            }
            print(f'{{"text": "{action_item["text"]}", "assignee": "{action_item["assignee"]}", "ts": "{action_item["ts"]}"}}')

#  file path of the CSV file
file_path = 'C:/Users/Avishkar/Desktop/ML/meeting_transcript.csv'

# function to process the CSV file
process_csv_file(file_path)
