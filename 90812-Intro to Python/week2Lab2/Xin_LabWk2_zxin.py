#!uer/bin/python3
# @author Zhiwei Xin, andrew ID zxin
# Created on Sep 7, 2016
# Modified on Sep 7, 2016
# @version 0.0.0
#
# This is a file to finish Lab on Week 2

def main():
    while(True):
        inputVal = input("Please enter the flag\n").strip()
        if (inputVal == "1"):
            print ("Good Morning!")
        elif (inputVal == "2"):
            print ("Good Evening!")
        for x in range(10):
            print("I love programming!")

main()