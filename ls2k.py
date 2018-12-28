import mx
'''
creates object for litespan 2000 equipment
	(4 ports, 55 slots, 9 banks, 225,226,675,676,1125,1126,1575,1576,2025 no_pair, 2025 tot_pairs)
'''

ls2k = mx.Mx(4, 55, 9, (225,226,675,676,1125,1126,1575,1576,2025), 1200)

'''
to test object uncomment lines below
'''

# print('ports',ls2k.ports)
# print('slots',ls2k.slots)
# print('no_pairs',ls2k.no_pairs)
# print('tot_pairs',ls2k.tot_pairs)
# n = 1575   # select no_pair to test
# if n in ls2k.no_pairs:
# 	print(n,'is a no_pairs')