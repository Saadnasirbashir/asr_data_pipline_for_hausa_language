# generate_transcript_csv.py

import os
import csv

AUDIO_DIR = 'audio'
TRANSCRIPT_FILE = 'transcripts.txt'
OUTPUT_CSV = 'transcripts.csv'

def load_transcripts(transcript_path):
    transcripts = {}
    with open(transcript_path, 'r', encoding='utf-8') as f:
        for line in f:
            if '|' in line:
                filename, text = line.strip().split('|', 1)
                transcripts[filename.strip()] = text.strip()
    return transcripts

def create_csv(audio_dir, transcripts, output_csv):
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['audio_filepath', 'transcript'])
        
        for filename in os.listdir(audio_dir):
            if filename.endswith('.wav') and filename in transcripts:
                writer.writerow([os.path.join(audio_dir, filename), transcripts[filename]])

if __name__ == '__main__':
    if not os.path.exists(TRANSCRIPT_FILE):
        print(f"Transcript file {TRANSCRIPT_FILE} not found.")
    else:
        transcripts = load_transcripts(TRANSCRIPT_FILE)
        create_csv(AUDIO_DIR, transcripts, OUTPUT_CSV)
        print(f"Transcript CSV generated at {OUTPUT_CSV}")
