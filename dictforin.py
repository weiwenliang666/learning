dict1 = {
    "a": 1
}
for v in dict1.values():
    print (v)



users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

pet1 = {"类型":"cat","主人":"A"}
pet2 = {"类型":"dog","主人":"B"}
pet3 = {"类型":"snake","主人":"C"}
pets = (pet1,pet2,pet3)
for pet in pets:
    print ("pet的类型是" + pet["类型"] + ',')
