import webbrowser

client_id = '52166656'
redirect_uri = 'https://oauth.vk.com/blank.html'
scope = 'wall,groups,offline'
auth_url = f"https://oauth.vk.com/authorize?client_id={client_id}&display=page&redirect_uri={redirect_uri}&scope={scope}&response_type=token&v=5.131"

webbrowser.open(auth_url)

print("Перейдите по ссылке в браузере, авторизуйтесь, и скопируйте токен из URL.")
