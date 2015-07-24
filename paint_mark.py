import time


def read_mark():
    action = []
    action_time = []
    with open('mark.txt') as m:
        for line in m.readlines():
            line = line.strip()
            # print line
            item = line.split(',')
            if item[2] != 'None':
                action.append(float(item[2]))
                t = time.localtime(float(item[0]))
                # print t
                t = time.strftime("%Y-%m-%d %H:%M:%S", t)
                action_time.append(t)
                # print t
        '''print type(line)
            up_down = line[2]
            print up_down'''
    # print action
    data = {'action': action, 'action_time': action_time}
    #print data
    return data


def main():
    read_mark()


if __name__ == '__main__':
    main()
