from datetime import date

today = date.today()
s = str(today)
print(s)
l = s.split('-')
cur_date = l[2]

from datetime import date
import calendar

today = date.today()
print(today)
s = str(today)
l = s.split('-')
year = int(l[0])
month = int(l[1])
date = int(l[2])
res = calendar.month_name[month]
cur_month = res[:3]


class TestData_Add_Relabel:
    test_data_add = [{'RelabelFrom': '03 HONDA', 'FromCustCode': 'DF_Honda-WuHan-2P',
                      'FromMaterialCode': '53392345', 'FromBatch': '20181018', 'StorageLocation': 'CJ01',
                      'Qty': '150', 'Priority': '2', 'Remarks': 'Request added by selenium script', 'RelabelTo': '03 '
                                                                                                                 'HONDA',
                      'ToCustCode': 'Honda-GZ-2P', 'ToMaterialCode': '53392345', 'ToBatch': '20181018C',
                      'CurrentDate': cur_date, 'ExpiryMonth': 'Dec', 'Year': '2023', 'ExpiryDate': '31',
                      'CurrentMonth': cur_month}]

    test_data_copy = [{'FromMaterial': '53392345', 'ToMaterial': '53392345', 'ToBatch': '20181018C'}]




