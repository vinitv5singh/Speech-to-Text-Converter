from faster_whisper import WhisperModel

# Size here can always be adjusted acc. to requirement
model = WhisperModel("small")

def transcribe_audio(audio_file):
    print("Transcribing...")
    
    segments, _ = model.transcribe(audio_file)
    
    transcript = " ".join(segment.text for segment in segments)
    return transcript


if __name__ == "__main__":
    audio_path = input("Enter the full path of the audio file: ").strip()

    try:
        transcript = transcribe_audio(audio_path)
        print("\nTranscription Output:\n", transcript)
    except Exception as e:
        print("\n❌ Error:", e)

