#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID - 20220645
#Student Name - T.Vishnujan
#Date - 14/12/2022.

markslist=[]
passlist=[]
deferlist=[]
faillist=[]

state1= True
outputval = 0

progress= ""
pnum= 0

trailer= ""
tnum= 0

retriever= ""
rnum=0

excluded= ""
enum=0
#error handling for range 
def numrange(num):
    if (num) not in range(0, 121, 20) :
        return print ("Out of Range\n")
    
#Main Program Loop
loop=True
while loop:

    #Print main menu
    print("\n |****************************|")
    print(" |   M  A  I  N  M  E  N  U   |")
    print(" |****************************|")
    print(" |1. Student path             |")
    print(" |2. Staff path               |")
    print(" |3. Exit                     |")
    print(" |                            |")
    print(" |                            |")
    print(" |****************************|")
    selection =input("Enter your preferred option (1-3): ")

    #Take action based on menu selection
    if selection =="1":
        try:
            passCredits = int(input("\nPlease Enter your Credits at Pass: "))
            numrange(passCredits)
        
            deferCredits = int(input("Please Enter your Credits at Defer: "))
            numrange(deferCredits)
        
            failCredits = int(input("Please Enter your Credits at Fail: "))
            numrange(failCredits)
            #INITILIZING THE INPUT DIMENSIONS
            if ((passCredits == 120) and ((deferCredits and failCredits) == 0)):
                a=[passCredits]
                a= a+[deferCredits]
                a= a+[failCredits]
                print("Progress",a,"\n")

            if ((100 <= passCredits < 120) and ((deferCredits or failCredits) == 20)):
                a=[passCredits]
                a= a+[deferCredits]
                a= a+[failCredits]
                print("Progress (module trailer)",a,"\n")
            
            if ((0 <= passCredits <= 80) and (0 <= failCredits <= 60)):
                a=[passCredits]
                a= a+[deferCredits]
                a= a+[failCredits]
                print("Do not progress – module retriever",a,"\n")
                    
            if ((0 <= passCredits <= 80) and (80 <= failCredits <= 120)):
                a=[passCredits]
                a= a+[deferCredits]
                a= a+[failCredits]
                print("Exclude",a,"\n")
                        
            elif (passCredits + deferCredits + failCredits) != 120 :
                print("Total Incorrect\n")
                
        except ValueError:
            print("Integer required\n")

        #RESTART OPTION
        restart=input("\nDo you want to continue (y/n): ")
        if (restart=="y" or restart=="Y"):
                loop=True
        
        if (restart=="n" or restart=="N"):
                print("Exit")
                loop=False    
        
    if selection =="2":
        

        while state1 == True:
                    try:
                        passCredits = int(input("\nPlease Enter your Credits at Pass: "))
                        numrange(passCredits)
                        passlist.append(passCredits)
                    
                        deferCredits = int(input("Please Enter your Credits at Defer: "))
                        numrange(deferCredits)
                        deferlist.append(deferCredits)
                    
                        failCredits = int(input("Please Enter your Credits at Fail: "))
                        numrange(failCredits)
                        faillist.append(failCredits)
                

                 #Displaying Progress results for seperate inputs of credits    
                        if ((passCredits == 120) and ((deferCredits and failCredits) == 0)):
                            markslist.append("Progress")

                            progress= progress + '*'
                            pnum +=1
                    
                        if ((100 <= passCredits < 120) and ((deferCredits or failCredits) == 20)):
                            markslist.append("Progress (module trailer)")
                        
                            trailer = trailer + '*'
                            tnum += 1

                        if ((0 <= passCredits <= 80) and (0 <= failCredits <= 60)):
                            markslist.append("Do not progress – module retriever")
                        
                            retriever = retriever + '*'
                            rnum += 1
                    
                        if ((0 <= passCredits <= 80) and (80 <= failCredits <= 120)):
                            markslist.append("Exclude")
                        
                            excluded = excluded + '*'
                            enum += 1

                        elif (passCredits + deferCredits + failCredits) != 120 :
                                print("Total Incorrect\n")
                        #VALIDATING INPUTS
                    except ValueError:
                        print("Integer required\n")

                    outputval += 1
            
                    state2 = True

                    while state2 == True:
                        user= str(input("Would you like to enter another set of data? Enter 'y' to continue or 'q' to quit and view results: "))
                
                        if user=='y':
                            state2 = False
                    
                        if user =='q':
                            f=open("results.txt","w")#to create a new file
                            f.close()
                            state2 = False
                            state1 = False
                            #Display Histogram stars
                            print("\nHISTOGRAM")
                            print("----------")
                            print('Progress ', pnum, ':', progress)
                            print('Trailer  ', tnum, ':', trailer)
                            print('Retriever', rnum, ':', retriever)
                            print('Excluded ', enum, ':', excluded)
                        
                            print(outputval, "outcome(s) in total.\n")

                            print("part2")
                            for x in range(len(markslist)):
                                print(markslist[x],"-",passlist[x],deferlist[x],faillist[x])

                            print("\npart3")
                            for x in range(len(markslist)):
                                f = open("results.txt","a") #to store data
                                f.write(str(markslist[x])+"-"+str(passlist[x])+","+str(deferlist[x])+","+str(faillist[x])+"\n")
                                f.close()

                            f=open("results.txt","r")
                                #To print data
                            for line in f:
                                print(line, end="")
                
                            f.close()
                            #RESTART OPTION
                            restart=input("\nDo you want to continue (y/n): ")
                            if (restart=="y" or restart=="Y"):
                                    loop=True
                            
                            if (restart=="n" or restart=="N"):
                                    print("Exit")
                                    loop=False   

    elif selection =="3":
            print("Thank you..")
            loop=False
     



