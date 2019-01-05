'''
 class file for equipment to create different equipment types and declare
 variables associated with the equipment types
'''

class Mx():
    def __init__(self, banks, slots, ports, prs_per_bank, no_pair, total_prs):
        self.banks = banks
        self.slots = slots
        self.ports = ports
        self.prs_per_bank = prs_per_bank
        self.no_pair = no_pair
        self.total_prs = total_prs

    
    def convert_to_ccpt(self, ilist, slist):
        pair = ilist[0]

        # simple but rowdy math for conversion(.5 push, floor division, conv int)
        bank = (pair // self.prs_per_bank[-1]) + 1
        slot = int((((pair % self.prs_per_bank[-1]) - .5) // self.ports[-1])+ 1)
        port = ((pair + self.ports[-2]) % self.ports[-1]) + 1

        # turn integers to strings for concatonation
        ccpt = (str(bank), str(slot), str(port))
        ccpt = '-'.join(ccpt)
        pair = slist[0]
        # fiter to catch no pairs
        if int(pair) in self.no_pair:
            print('No Pair')
            return

        # print("CCPT is " + ccpt + "\n" + "Pair is " + pair) #concatonation
        answer = ("CCPT is {}\nPair is {}")
        print(answer.format(ccpt, pair))                     #.format
        
    def convert_to_pair(self, ilist, slist):  
        ccpt = '-'.join(slist)
        pair = (ilist[0] - 1) * self.prs_per_bank[-1] \
               + (ilist[1] * self.ports[-1]) - self.ports[-1] + ilist[2]
                
        # only pair needs type change here for concatonation
        print("Pair is " + str(pair) + "\n" + "CCPT is " + ccpt)