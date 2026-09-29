class_professors = {'Cart_253_A':'Pippin Bar',
                    'Cart_211':'Brad Todd',
                    'Cart_214':'Joanna Berzowska', 
                    'Cart_215':'Jonathan Lessard'}
# print(type(class_professors))

speciallist = {17: [1.6, 2.45], 42: [11.6, 19.4], 101: [0.123, 4.89]}
# print(speciallist [17])
# # strings need to be in quotes, numbers do not
# print(class_professors['Cart_214'])

# print(speciallist.keys())
# for key in speciallist.keys():
#     print(speciallist[key])
# print(speciallist.values())
# for value in speciallist.values():
#     print(value)
# print(speciallist.items())
# for item in speciallist.items():
#     print(item[0])

shopping = {
            'vegetables': [{'spinach': "green"}, 'carrots','broccoli','lettuce'],
            'fruit': ['canteloupe', 'banananas'],
             'bakery': ['bagels', 'rye bread'],
            }
# accessing the list of vegetables
print (shopping ['vegetables'] [0] ['spinach'] [0]) # returns 'green'
