#Text Analyzer Project
#function for count a single character in Textfile
def count_char(text,ch):
    count=0
    l = len(text)
    for i in range(l):
        if text[i]==ch:
            count+=1
    return count

file = open("textfile.txt", 'w')
file.write("Android Rooting means of unlocking the operating system so you can install unapproved apps,deleted unwanted bloatware,update the OS,replace the firmware , overcllock or underclock the processor customize anything and so on Of course for the average user this sounds like and can be a scary process After all rooting around in your smartphone core software might seem like a recipe for disaster Once wrong move and you could end up with bricked hand set Android is a very versatike customizable and open operating system You may think that rooting is not for you but it can actually help you to a very great extent With so little work so much can be achevied You may have heard bad thing about rooting butr in some cases you may consider using it especially if it is done by prople who are aware of what needs to be done Some of the reasonds include")
file.close()
with open("project files/textfile.txt") as f:
    text = f.read()
    f.close()

print("\t\tTEXT ANALYZER PROGRAM")
print("FileText :")
print(text)
#Text analyzing for all text in the file 
for ch in "abcdefghijklmnopqrstuvwxyz":
    #print percentage of all characters in the text file
    perc=100*count_char(text,ch)/len(text)
    print("{0}%\t- {1} in the FileText".format(round(perc,2),ch))