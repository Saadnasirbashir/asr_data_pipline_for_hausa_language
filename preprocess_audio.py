import os
import argparse
import librosa
import soundfile as sf
from tqdm import tqdm

def preprocess_audio(input_dir, output_dir, sample_rate=16000, mono=True, trim_silence=False):
    os.makedirs(output_dir, exist_ok=True)
    
    for file_name in tqdm(os.listdir(input_dir), desc="Processing audio files"):
        if file_name.endswith(".wav"):
            file_path = os.path.join(input_dir, file_name)
            try:
                audio, sr = librosa.load(file_path, sr=sample_rate, mono=mono)

                if trim_silence:
                    audio, _ = librosa.effects.trim(audio, top_db=20)

                # Normalize audio
                audio = audio / max(abs(audio))

                output_path = os.path.join(output_dir, file_name)
                sf.write(output_path, audio, sample_rate)
            except Exception as e:
                print(f"Error processing {file_name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch preprocess WAV audio files.")
    parser.add_argument("input_dir", type=str, help="Directory containing raw .wav files")
    parser.add_argument("output_dir", type=str, help="Directory to save processed .wav files")
    parser.add_argument("--sample_rate", type=int, default=16000, help="Target sample rate")
    parser.add_argument("--mono", type=bool, default=True, help="Convert audio to mono")
    parser.add_argument("--trim_silence", action="store_true", help="Trim leading/trailing silence")

    args = parser.parse_args()
    preprocess_audio(args.input_dir, args.output_dir, args.sample_rate, args.mono, args.trim_silence)
