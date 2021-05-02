from os import system
from os.path import abspath, join, dirname
from time import sleep
from gtts import gTTS

adb_exec_path = "D:\\platform-tools_r31.0.2-windows\\platform-tools\\adb"
mpg123_exec_path = "D:\\mpg123-1.26.5-x86-64\\mpg123-1.26.5-x86-64\\mpg123"
sounds_dir_path = "D:\\sounds"

def phone_call(adb_exec, device_id, phone_number):
    system(f"{adb_exec} -s {device_id} shell am start -a android.intent.action.CALL -d tel:{phone_number}")

def save_text(message, language, filename):
    tts = gTTS(message, lang=language)
    sound_path = join(sounds_dir_path, filename)
    tts.save(sound_path)
    return sound_path

def play_sound(mpg123_exec, file_path):
    system(f"{mpg123_exec} {file_path}")

def main():
    sound_file = save_text('Hola, bienvenido a smart mail', 'es', 'hola.wav')
    phone_call(adb_exec_path, "7120018020022742", "8121465119")
    sleep(20)
    play_sound(mpg123_exec_path, sound_file)