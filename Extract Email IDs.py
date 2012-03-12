f = open("/home/mankaj/Downloads/Write your Own FS - Sheet1.tsv").readlines()
emailList = []
for line in f[1:]:
    listofdata = line.split("\t")
    try:
        emailList.append(listofdata[2])
    except:
        pass

listofemail = open("ListOfEmailIDs.txt", 'w')
for emailid in emailList:
    listofemail.write(emailid + "\n")

listofemail.close()
print "Done"
