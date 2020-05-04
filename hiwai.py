import subprocess
from subprocess import PIPE

def speech(word):
    return 'jsay ' + word


word = input('読ませたい卑猥なワード')
cmd = subprocess.run(speech(word), shell=True, stdout=PIPE)
jsay = cmd.stdout