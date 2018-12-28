# paircalc
Tool to convert location in mux equipment to a sequential number, accounting for lost pairs due to overhead in bandwidth.

The parameters for this project are: write a program that converts channel bank-slot-port into pair#. 
a sample:
    1-1-1   is equal to channel bank 1, slot 1, port 1. This will convert to pair 1. 
    1-1-2   is equal to channel bank 1, slot 1, port 2. This will convert to pair 2.
    1-1-3   is 3
    1-1-4   is 4
    1-1-5   is 5
    1-1-6   is 6
    1-2-1   is 7
    1-2-2   ....etc...each channel bank goes to 1-22-6  is 132
    133-150 are no_pairs and then the address sequence starts over at the next bank.
    2-1-1   all the way to 8-22-6
    
I have written a version using math, a dictionary, and now I would like to try to use something inspired by the Python calendar and timedelta.
It would be nice to be able to learn to use some of the functions of those Python classes to display the channel banks similar to months, weeks, days. 

I have started off by creating a class Mx that can be used to create different objects that represent different equipment. The details for the two types so far are in separate files called umc and ls2k.

My motivation is 90% to challenge myself to learn to code tools in Python and 10% to be able to make a web app and phone app when I'm done to use the tool. 

 
