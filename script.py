# Install: https://github.com/openai/whisper?tab=readme-ov-file

import whisper

model = whisper.load_model('large')
result = model.transcribe('la-ultima-noche-de-sandra-m.mp3', language='es', verbose=True)
srt_file_path = 'la-ultima-noche-de-sandra-m.srt'

def seconds_to_srt_time(seconds):
    milliseconds = int(seconds * 1000)
    hours = milliseconds // (1000 * 60 * 60)
    minutes = (milliseconds // (1000 * 60)) % 60
    seconds = (milliseconds // 1000) % 60
    milliseconds = milliseconds % 1000
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

with open(srt_file_path, 'w') as srt_file:
    for segment in result['segments']:
        start_time = seconds_to_srt_time(segment['start'])
        end_time = seconds_to_srt_time(segment['end'])
        text = segment['text']

        srt_file.write(f"{segment['id']+1}\n")
        srt_file.write(f"{start_time} --> {end_time}\n")
        srt_file.write(f"{text}\n\n")