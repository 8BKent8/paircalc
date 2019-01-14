import re
import mx
'''calulator using separate functions for ccpt and pair calculations
    placed in class Mx.
    program starts by creating an object for each type of equipment.
'''
umc = mx.Mx(8,  #umc banks per sys
            22, #umc slots per bank
            6,  #umc ports per slot
            150,#umc pairs per bank
            (list(range(133, 151))
            + list(range(283, 301)) 
            + list(range(433, 451))
            + list(range(583, 601))
            + list(range(733, 751))
            + list(range(883, 901))
            + list(range(1033, 1051))
            + list(range(1183, 1201))), #umc no pairs
            1200)   #umc total pairs
           
ls2k = mx.Mx(9, #ls2k banks per sys
            56, #ls2k slots per bank
            4,  #ls2k ports per slot
            225,#ls2k pairs per bank
            [225, 226, 675, 676, 1125, 1126, 1575, 1576, 2025], #ls2k no_pairs pair
            2025)    #ls2k total pairs

#while loop will continually ask for input till you are finished calculating.

while True:

#get user input
    
    equipment = input('Enter equipment type [ls2k/umc]: ')
    rawinput = input('Enter CCPT/Pair: ')
# better input validation needed, breaks when mixed strings are input.
    
    if equipment and rawinput:
        # check for equipment and rawinput and if both are True,
        # split and create a string list and integer list out of rawinput.
        slist = rawinput.split('-')
        ilist = []
        for num in slist:
            ilist.append(int(num))

#filter by slist length and equipment.  validate ccpt or pair with class data
#if valid convert with funtion from class file

            #if list of 3 is found call convert to pair

        if len(slist) == 3:
            if equipment == 'umc':
                if ilist[0] in umc.banks:
                    if ilist[1] in umc.slots:
                        if ilist[2] in umc.ports:
                            umc.convert_to_pair(ilist, slist)

            elif equipment == 'ls2k':
                if ilist[0] in ls2k.banks:
                    if ilist[1] in ls2k.slots:
                        if ilist[2] in ls2k.ports:
                            ls2k.convert_to_pair(ilist, slist)

        #if list of 1 is found call convert to ccpt

        elif len(slist) == 1 and re.match(r'[0-9]', rawinput):
            if equipment == 'umc':
                if ilist[0] <= umc.total_prs:
                    umc.convert_to_ccpt(ilist, slist)
         
            elif equipment == 'ls2k':
                if ilist[0] <= ls2k.total_prs:
                   ls2k.convert_to_ccpt(ilist, slist)

        #else staments to indicate which data validation failed.
            
            else:
                print('Not quite enough to work with')                    
        else:
            print('Hmmmmm')
        #else:
            #print('? what pair or ccpt ?')
    else:
        print('? What equipment type ?')

