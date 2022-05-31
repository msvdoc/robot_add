import webbrowser
import requests
from pybitrix24 import Bitrix24
REQUEST_FOR_BITRIX = 'https://oauth.bitrix.info/oauth/token/?grant_type=authorization_code&client_id=local.628270ee49e045.76651210&client_secret=H9VRI6CPLvrCvZdPZ32xuWfUVklLEs8LJYXd5AVSclJ2G4WqEi&code=78d78562005b74c0005b62f80000000100000775bc39845deadbc0dbc298c0807ff855'
params = {
            'CODE': 'robot2',
            'HANDLER': 'https://34cf-37-29-88-209.eu.ngrok.io',
            'AUTH_USER_ID': 1,
            'NAME': 'Василий',
            'PROPERTIES':
            {
                'bool': {
                    'Name': 'Да/Нет',
                    'Type': 'bool',
                    'Required': 'Y',
                    'Multiple': 'N'
                },
                'date': {
                    'Name': 'Дата',
                    'Type': 'date'
                },
                'datetime': {
                    'Name': 'Дата/Время',
                    'Type': 'datetime'
                },
                'double': {
                    'Name': 'Число',
                    'Type': 'double',
                    'Required': 'Y'
                },
                'int': {
                    'Name': 'Целое число',
                    'Type': 'int'
                },
                'select': {
                    'Name': 'Список',
                    'Type': 'select',
                    'Options': {
                        'one': 'one',
                        'two': 'two'
                    }
                },
                'string': {
                    'Name': 'Строка',
                    'Type': 'string',
                    'Default': 'default string value'
                },
                'text': {
                    'Name': 'Текст',
                    'Type': 'text'
                },
                'user': {
                    'Name': 'Пользователь',
                    'Type': 'user'
                }
            }
        }

bx24 = Bitrix24('https://b24-5rup0p.bitrix24.ru', 'local.628270ee49e045.76651210', 'H9VRI6CPLvrCvZdPZ32xuWfUVklLEs8LJYXd5AVSclJ2G4WqEi')
ac = str(bx24.build_authorization_url())
ac = str(ac[8:])
res2 = requests.get(ac)
ac = res2.text

# webbrowser.open(ac, new=2, autoraise=True)




# Этот пример запроса (только там было добавление лида), взят из примеров для разработчика infocom
# aa = requests.post('https://b24-5rup0p.bitrix24.ru/rest/bizproc.robot.add?auth=76e88562005b74c0005b62f800000001000007386599a8b77d5ea03c38d3e8d268fe1d', json=params)

#bx24.obtain_tokens('4ac88362005b74c0005b62f800000001000007b501e03e36ff2560c7be94407205d424')
# bx24.refresh_tokens()
# bx24.call('user.get', {'ID': 1})



