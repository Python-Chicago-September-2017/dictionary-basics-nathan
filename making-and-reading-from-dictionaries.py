myself = {"name":"Nathan", "age": 22, "hometown": "Holland, MI"}

def reading_my_dictionary(dic):
    for key in dic:
        value = dic[key]
        print "My " + key + " is " + str(value)

reading_my_dictionary(myself)