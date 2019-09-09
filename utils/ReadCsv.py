import csv


# 读取csv文件内容
class ReadCsv(object):
    def read_csv(self, file_path):
        my_list = []
        result = csv.reader(open(file_path, 'r', encoding='UTF-8'))
        # print(result)
        for i in result:
            my_list.append(i)
            my_lists = my_list[1:]
        return my_lists


if __name__ == '__main__':
    r = ReadCsv()
    read = r.read_csv('../data/register.csv')
    print(read[0])
    print(read[1])
