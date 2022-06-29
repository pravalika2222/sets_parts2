    #   "symmertric_difference_update"
    # 'in symmetric_difference_update will get the distinct elements from both the sets'
# a={1,2,4,5,6}
# b={2,5,7,9,10}
# a.symmetric_difference_update(b)
# print(a) # {1, 4, 6, 7, 9, 10}
# b.symmetric_difference_update(a)
# print(b)    # {1, 4, 6, 7, 9, 10}  will get the both values are same

        # "intersection update"
# a={1,2,3,4,5}
# b={3,5,9,7,2}
# a.intersection_update(b)
# print(a)   # {2, 3, 5}   # it will get the common values
# b.intersection_update(a)
# print(b)     # {2, 3, 5} 

           # "remove set"
        #  'in remove the keyerror will get the distinct'
('''if we want to remove the value which is in the i/p it will be remove''' 
'''but,if we want to remove the value which is not in the i/p,it will show the o/p as 'keyerror''')
# a={2,5,6,9}
#  a.remove(2)
#  print(a)      # {9, 5, 6}
#  a.remove(45)
#  print(a)    # keyerror: 45  

        # 'issupper set'
'''in issupper set the both sets should contain same elements or values . then the another set can contain 
less elements with same values but shouldn't contain distinct elements'''
# a={1,2,3,4,5}
# b={1,2,3}
# print(a.issuperset(b))   # true
# print(b.issuperset(a))    # false 

        #    ''copy set''
# a={'prava'}
# a.copy()
# print(a)    # prava


