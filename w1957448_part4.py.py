#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID - 20220645
#Student Name - T.Vishnujan
#Date - 14/12/2022.

markslist=[]
passlist=[]
deferlist=[]
faillist=[]
dicti={}
id_list=[]
name=""
    
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
while True:
    while state1 == True:
                    try:
                        stu_name =input("\nEnter student ID number:")
                        if stu_name in dicti:
                            print("Student id already added")
                            continue
                            
                        passCredits = int(input("Please Enter your Credits at Pass: "))
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

                    id_list.append(stu_name) 
                    

                    outputval += 1
            
                    state2 = True

                    for x in range(len(markslist)):
                        dicti[id_list[x]]=(markslist[x],passlist[x],deferlist[x],faillist[x])

                    while state2 == True:
                        user= str(input("Would you like to enter another set of data? Enter 'y' to continue or 'q' to quit and view results: "))
                
                        if user=='y':
                            state2 = False
                    
                        if user =='q':
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
   
                         

                            print("\npart4")

                            for key,value in dicti.items():
                                print(key,":",value,end=" ")



     



