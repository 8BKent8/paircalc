import mx

'''
creates object for umc1000 equipment
    (6 ports, 22 slots, 8 banks, 18 no_pairs at end of channel banks, 1200 tot_pairs)
'''

umc = mx.Mx(6, 22, 8, (list(range(133, 151))
                     + list(range(283, 301))
                     + list(range(433, 451))
                     + list(range(583, 601))
                     + list(range(733, 751))
                     + list(range(883, 901))
                     + list(range(1033, 1051))
                     + list(range(1183, 1201))),
                     1200)

'''
to test object uncomment lines below
'''

# print('ports',umc.ports)
# print('slots',umc.slots)
# print('no_pairs',umc.no_pairs)
# print('tot_pairs',umc.tot_pairs)
# n = 134   # select no_pair to test
# if n in umc.no_pairs:
# 	print(n,'is a no_pairs')