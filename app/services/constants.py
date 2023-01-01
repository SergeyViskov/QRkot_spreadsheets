FORMAT = "%Y/%m/%d %H:%M:%S"
SPREADSHEET_TITLE = 'QRKot_Отчет на {now}'
SPREADSHEETS_BODY = {
    'properties': {'title': 'spreadsheet title',
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
