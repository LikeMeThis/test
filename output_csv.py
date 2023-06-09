import csv

def split_and_print_csv_data(filename, batch_size):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

        for i in range(0, len(data), batch_size):
            batch = data[i:i+batch_size]
            print(batch)


filename = "fyx_chinamoney.csv"

# 将 CSV 数据按照批次拆分并打印输出
split_and_print_csv_data(filename, 80)
