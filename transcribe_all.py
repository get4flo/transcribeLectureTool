import openai
import os

client = openai.OpenAI()

INPUT_DIR = "audioTrack"
OUTPUT_DIR = "transcript"
os.makedirs(OUTPUT_DIR, exist_ok=True)

for fname in os.listdir(INPUT_DIR):
    if fname.lower().endswith(".mp3"):
        inp = os.path.join(INPUT_DIR, fname)
        out_fname = os.path.splitext(fname)[0] + ".txt"
        outp = os.path.join(OUTPUT_DIR, out_fname)

        print(f"Transcribing {fname} …")
        with open(inp, "rb") as audio_file:
            #try:
            transcription = client.audio.transcriptions.create(
                #model="gpt-4o-transcribe",
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
            '''
            except openai.BadRequestError as e:
                if (
                    hasattr(e, "message") and
                    "audio duration" in str(e) and
                    "is longer than" in str(e)
                ):
                    print(f"Try again {fname}: {e}")
                    transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    response_format="text"
                )
                else:
                    raise e
            '''

        print(transcription)
        with open(outp, "w", encoding="utf‑8") as f:
            f.write(transcription)
        print(f"  → Saved: {outp}")


