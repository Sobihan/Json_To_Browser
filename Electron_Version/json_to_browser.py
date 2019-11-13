import eel, webbrowser, validators

eel.init('web', allowed_extensions=['.js', '.html'])


@eel.expose
def open_url(content):
    url = []
    tmp = None
    split = content.split("\"")
    for i  in range(len(split)):
        if i + 2 >= len(split):
            break
        if split[i] == 'url':
            tmp = split[i + 2]
            if not tmp in url and validators.url(tmp) == True:
                url.append(tmp)
    if (len(url) <= 0):
        print("[DEBUG] There is no url [DEBUG]")
        return (False)
    for i  in range(len(url)):
        webbrowser.open(url[i])
    return (True)

eel.start('index.html', size=(1000, 600))