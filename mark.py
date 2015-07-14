import xlrd
import datetime
import time


def read_xls(filename):
    bk = xlrd.open_workbook(filename)
    sheet = bk.sheet_by_name("Sheet1")

    nrows = sheet.nrows

    with open('mark.txt', 'w') as f:
        tmp = 2.0
        for i in range(1, nrows):
            row = sheet.row_values(i)
            time_str = str(row[0])
            dt = datetime.datetime(2015, 5, 18,
                                   int(time_str[:2]),
                                   int(time_str[2:4]),
                                   int(time_str[4:6]))
            f.write(str(time.mktime(dt.timetuple()))+',')

            if row[1] == u'OS':
                f.write('0'+',')
            elif row[1] == u'CF':
                f.write('1'+',')
            else:
                f.write('None'+',')

            if row[2] == u'US':
                f.write('0'+',')
            elif row[2] == u'UF':
                f.write('1'+',')
            elif row[2] == u'DS':
                f.write('2'+',')
            elif row[2] == u'DF':
                f.write('3'+',')
            else:
                f.write('None'+',')

            if type(row[3]) == float:
                f.write(str(row[3])+',')
                tmp = row[3]
            else:
                f.write(str(tmp)+',')

            if len(row[5]) > 0:
                if row[5][0] == 'I':
                    f.write('1')
                else:
                    f.write('0')
            else:
                f.write('None')

            f.write('\n')


def main():
    fname = "mark.xls"
    read_xls(fname)


if __name__ == '__main__':
    main()
