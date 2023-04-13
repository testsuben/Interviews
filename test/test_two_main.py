# -*- coding: UTF-8 -*-


"""
第二题
未调试
"""




def writepb():
    my_metric = Person ()
    my_metric.name = 'test'
    my_metric.id = 11111
    my_metric.valuemaile = "test@***.com"
    my_metric.PhoneType =0
    my_PhoneNumber =PhoneNumber ()
    my_PhoneNumber.PhoneNumber=1234
    my_AddressBook  = AddressBook ()
    my_AddressBook.AddressBook="xjfpejpjg.xjpfjp"


    with open('out.bin', 'wb') as f:
        f.write(my_metric.SerializeToString())
        f.write(my_PhoneNumber.SerializeToString())
        f.write(my_AddressBook.SerializeToString())


def readpb():
    with open('out.bin', 'rb') as f:
        read_metric = Person.Metric()
        read_metric.ParseFromString(f.read())
        print(read_metric)

        read_PhoneNumber =PhoneNumber ()
        read_PhoneNumber.ParseFromString(f.read())
        print(read_PhoneNumber)

        read_AddressBook  = AddressBook ()
        read_AddressBook.ParseFromString(f.read())
        print(read_AddressBook)
        # do something with read_metric


if __name__ == "__main__":
    writepb()
    readpb()