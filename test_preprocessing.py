import os
from preprocess_audio import preprocess_audio

# Define paths
input_path = "sample_data/raw"
output_path = "sample_data/processed"

# Run preprocessing
preprocess_audio(
    input_dir=input_path,
    output_dir=output_path,
    sample_rate=16000,
    mono=True,
    trim_silence=True
)

# Verify output
print("\n✅ Preprocessing complete!")
print(f"Processed files saved to: {output_path}")
print("Files:", os.listdir(output_path))
