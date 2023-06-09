
import requests
import csv
def scrape(page,list1):
    # 1. 从链接页面获取 HTML 内容
    url = "https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"
    data = {'pageNo':page,'pageSize': 15,'bondType': '100001','issueYear':'2023'}
    response = requests.post(url,data=data)
    json_data = response.json()
    print(json_data)
    for information in json_data['data']['resultList']:
        isin = information.get('isin')
        bond_code = information.get('bondCode')
        issuer = information.get('entyFullName')
        bond_type = information.get('bondType')
        issue_date = information.get('issueStartDate')
        latest_rtng = information.get('debtRtng')
        dict1 ={
            'ISIN': isin,
            'Bond_Code': bond_code,
            'Issuer': issuer,
            'Bond_type':bond_type,
            'Issue_Date':issue_date,
            'Latest_Rating': latest_rtng
        }
        list1.append(dict1)

def write_dicts_to_csv(dicts, filename):
    # 获取所有字典的键，作为 CSV 文件的表头
    fieldnames = set().union(*[d.keys() for d in dicts])

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 写入表头
        writer.writeheader()

        # 写入每个字典的值
        for d in dicts:
            writer.writerow(d)

def main():
    list1 = []
    for page in range(1,5):
        scrape(page,list1)
    # 调用函数将字典写入 CSV 文件
    write_dicts_to_csv(list1, "output.csv")
if __name__ =='__main__':
    main()

