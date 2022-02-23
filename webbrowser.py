import webbrowser
import time
website = input('''What URL should I use?
''')
time.sleep(8)
while True:
    webbrowser.open_new(website)

