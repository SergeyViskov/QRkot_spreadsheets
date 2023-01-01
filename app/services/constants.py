from datetime import datetime


FORMAT = "%Y/%m/%d %H:%M:%S"
NOW_DATE_TIME = datetime.now().strftime(FORMAT)
SPREADSHEETS_BODY = {
    'properties': {'title': f'QRKot_Отчет на {NOW_DATE_TIME}',
                       'locale': 'ru_RU'},
    'sheets': [{
        'properties': {'sheetType': 'GRID',
                        'sheetId': 0,
                        'title': 'Скорость закрытия',
                        'gridProperties': {'rowCount': 100,
                                            'columnCount': 11}
                        }
    }]
}
