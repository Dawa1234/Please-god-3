'''Write a function called showNumbers that takes a prameter called limit. It should point all the number
between 0 and limit with a label to identify the even and odd numbers. For example , if the limit is 3,
it should print::     0 EVEN , 1 ODD , 2 EVEN'''


def shouNumbers(limit):
    while limit <= 20:
        if limit % 2 == 0 :
            print(f"{limit} EVEN")
        else:
            print(f"{limit} ODD")
        limit += 1

shouNumbers(0)


