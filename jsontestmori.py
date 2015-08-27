import json

f = open('jsonData.json', 'r')

jsonData = json.load(f)


#print json.dumps(jsonData, sort_keys = True, indent = 4)

keyList = jsonData.keys()

keyList.sort()

print "keyList",keyList

for k in keyList:
        print "[", k,"]"
        groupDict = jsonData[k]

        print "groupDict",groupDict

        nameList = groupDict.keys()

        nameList.sort()

        print "nameList",nameList


        for name in nameList:

                if groupDict[name] >= 50:
                        print "%s's value is %d" % (name, groupDict[name])

f.close()