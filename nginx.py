

import pandas as pd
xlArray = []

fileArray = ["secure-site.conf.txt","nginx.conf.txt","internal-site.conf.txt"]
textFile = "secure-site.conf.txt"
mylines = [] 
filtered = []
count = 0
for textFile in fileArray:
    with open(textFile) as f:
        for myline in f:              
            sp = myline.split()
            if "location" in sp:
                if sp[0] == "location":
                    path = sp[1].replace("/","")
                    mylines.append(path)
                    x = path.find("-enc")
                    if x > 0:
                        splitWord = path.split("-enc")
                        if splitWord not in mylines:
                            filtered.append(splitWord[0])
                            count += 1
                    else:
                        filtered.append("-")
                if sp[1]== "location":
                    path = sp[2].replace("/","")
                    mylines.append(path)
                    x = path.find("-enc")
                    if x > 0:
                        splitWord = path.split("-enc")
                        if splitWord not in mylines:
                            filtered.append(splitWord[0])
                            count += 1
                    else:
                        filtered.append("-")
                
    print(textFile + " has " + str(len(mylines)) + " location Entry  out of this "+ str(count) + " is with enc and " + str(len(mylines) - count) +" is without enc")
    xlArray.append(mylines)
    xlArray.append(filtered)
    filtered = []
    mylines = []
    count =  0
df = pd.DataFrame(xlArray).T
df.columns = ["secure-site.conf.txt","with-enc","nginx.conf.txt","with-enc","internal-site.conf.txt","with-enc"]
df.to_excel(excel_writer = "test.xlsx")












































# textFile = "nginx.conf.txt"
# mylines1 = [] 
# with open(textFile) as f:

#     for myline in f:              
#         sp = myline.split()
#         if "location" in sp:
#         #    print(sp)
#         #    print("==================================")
#            mylines1.append(sp[1])

# # print(mylines)
# print(textFile + " has " + str(len(mylines1)) + " location Entry")


# textFile = "internal-site.conf.txt"
# mylines2 = [] 
# with open(textFile) as f:

#     for myline in f:              
#         sp = myline.split()
#         if "location" in sp:
#         #    print(sp)
#         #    print("==================================")
#            mylines2.append(sp[1])

# # print(mylines)
# print(textFile + " has " + str(len(mylines2)) + " location Entry")



   