# extract audio track from lecture videos
#for f in videos/*.mp4; do ffmpeg -i "$f" -vn -acodec libmp3lame -q:a 2 "audioTrack/$(basename "${f%.mp4}").mp3"; done
for f in videos/*.mp4; do ffmpeg -i "$f" -vn -acodec libmp3lame -q:a 5 "audioTrack/$(basename "${f%.mp4}").mp3"; done


# transcribe audio files
export OPENAI_API_KEY=""
source ~/.virtualenvs/transcribePsyModule/bin/activate
python transcribe_all.py