print("\t------------------")
print("\t  Word Analyzer  ")
print("\t------------------")
file1  = open("file.txt", "r")
content = file1.read()
print("File.txt Content :")
print(content,"\n")
list1 = content.split()
list2 = list()
dict1 = dict()
for word in list1:
    dict1[word] = dict1.get(word,0) + 1
print("Counting : ")
for i,j in dict1.items():
    print(i,":",j,end=", ")
    
print("\n\nSorted Descending order : ")   
list2 = sorted([(j,i)for i,j in dict1.items()],reverse=True)
for i,j in list2:
    print(j,": ",i,end = " ")

file1.close()