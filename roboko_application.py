import csv
import sys

from roboko_message.roboko_message import roboko

def file_create():
    try:
        with open(roboko.csv_path,'x', encoding = 'utf-8') as f:
            return 0
    except FileExistsError as e:
            return 1
    
def file_read(flag):
    if flag == 1:
        with open(roboko.csv_path) as csvfile:
            reader = csv.reader(csvfile)
            csvlist = [[]]
            csvlist = [row for row in reader]
            csvlist.sort(reverse = True)
            print(csvlist)
            for i in range(len(csvlist)):
                print(roboko.roboko_like_resutaurant + csvlist[i][0] + 'です。')
                print(roboko.do_you_like_resutaurant)
                user_like = input()
                if user_like.lower() == 'yes' or user_like.lower() == 'y':
                    break
                elif user_like.lower() == 'no' or user_like.lower() == 'n':
                    pass
                else:
                    print('入力されている文字が違います。[Yes/No]')
                    continue
        return csvlist
    elif flag == 0:
        pass
    else:
        sys.exit()


def file_write(resutaurant):
    with open(roboko.csv_path,'a') as f:
        f.write(resutaurant.title() + ',1' + '\n')

def file_rewrite(csvlist):
    with open(roboko.csv_path,'w') as f:
        for i in range(len(csvlist)):
            f.write(csvlist[i][0].title() + ',' + str(csvlist[i][1]) + '\n')

def file_control(csvlist,resutaurant):
    for i in range(len(csvlist)):
        if csvlist[i][0] == resutaurant.title():
            csvlist[i][1] = int(csvlist[i][1]) + 1
            break
        elif i == (len(csvlist) -1 ):
            return csvlist,0
        else:
            pass
    return csvlist,1

def main():
    flag = file_create()
    print(roboko.hello_message + roboko.who_are_you) 
    user_name = input()
    csvlist = file_read(flag)
    print(user_name + roboko.where_restaurant_like)
    resutaurant = input()
    if flag == 1:
        csvlist,write_flag = file_control(csvlist,resutaurant)
        if write_flag == 1:
            file_rewrite(csvlist)
        else:
            file_write(resutaurant)
    else:
        file_write(resutaurant)

    print(user_name + roboko.thank_you)
    print(roboko.goodby_message)

if __name__ == '__main__':
    main()
