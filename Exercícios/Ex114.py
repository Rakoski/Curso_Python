import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://youtube.com.br')
except urllib.error.URLError:
    print('\033[1;31mO site não está acessível no momento!\033[m')
else:
    print(f'\033[1;32mTudo ok!')