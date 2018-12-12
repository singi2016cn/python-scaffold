"""验证用户"""

import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input('请输入用户名:\n')
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """问候用户，并指出起名字"""
    username = get_stored_username()
    print('请问您的名字是' + username + '吗')
    answer = input('是:y 否:n\n')
    if answer.lower() == 'n':
        username = get_new_username()
    if username:
        print('欢迎回来，' + username + '!')
    else:
        username = get_new_username()
        print('当你再次登录时，我们将记住你的名字,' + username)


greet_user()
