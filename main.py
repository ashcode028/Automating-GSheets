import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

from auth import client

# List of all names of the sheets you want to work on
titles = []
for spreadsheet in client.openall():
    if spreadsheet.title != 'Parent Sheet':
        titles.append(spreadsheet.title)
parent_sheet = client.open('Parent Sheet')
# parent_sheet.get_worksheet(0).clear()
# parent_sheet.get_worksheet(0).update([df.columns.values.tolist()])
parent_df = pd.DataFrame(parent_sheet.get_worksheet(0).get_all_records())
for sheet_name in titles:
    sheet = client.open(sheet_name)
    list_of_dicts = sheet.get_worksheet(0).get_all_records()

    df = pd.DataFrame(list_of_dicts)
    #  use join ,merge or concatenate join dataframes and update it
    final_df = pd.concat([parent_df, df])
    parent_sheet.get_worksheet(0).append_rows(final_df.values.tolist())
