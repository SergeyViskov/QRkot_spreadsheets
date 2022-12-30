from datetime import datetime
from typing import List

from aiogoogle import Aiogoogle

from app.core.config import settings
from app.services import constants as const


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    now_date_time = datetime.now().strftime(const.FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheets_body = {
        'properties': {'title': f'QRKot_Отчет на {now_date_time}',
                       'locale': const.LOCALE},
        'sheets': [{
            'properties': {'sheetType': 'GRID',
                           'sheetId': const.SHEET_ID,
                           'title': const.TABLE_NAME,
                           'gridProperties': {'rowCount': const.ROW_COUNT,
                                              'columnCount': const.COL_COUNT}
                           }
        }]
    }
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheets_body)
    )
    spreadsheet_id = response['spreadsheetId']
    return spreadsheet_id


async def set_user_permissions(
    spreadsheet_id: str,
    wrapper_services: Aiogoogle
) -> None:
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email
    }
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields='id'
        )
    )


async def spreadsheets_update_value(
    spreadsheet_id: str,
    projects: List,
    wrapper_services: Aiogoogle
) -> None:
    now_date_time = datetime.now().strftime(const.FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    table_values = [
        ['Отчет от', now_date_time],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]
    for project in projects:
        new_row = [
            str(project['name']),
            str(project['duration']),
            str(project['description'])
        ]
        table_values.append(new_row)
    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    all_lines = len(table_values)
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=f'A1:C{all_lines}',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
