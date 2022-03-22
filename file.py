#w : greating new doccument
# resul =open("newfile.text","w")
# resul.write("my name is moha i am a programmer")
# resul.close()
#print(resul)

#w : greating new doccument if there is already document it add only.
# resul =open("newfile.text","a")
# resul.write("\ni am studying Ktu")
# resul.close()
# file =open("newfile.text","r")
# content =file.read(10)
# print(content)
# file.seek(10)
# print(file.tell())
# print(content)
# file.close()
#file.seek(10) =waxa laga wadaa kusarku inuu taga bytka 10naad
# process about file in python example
def calculating_marks(rows):
  rows =rows[:-1] #this is means taking white space.
  liste  =rows.split(":") #we are spliting after this:
  #print(liste[0])
  #print(liste[1])
  student_Names =liste[0]
  schol_Marks =liste[1].split(',')

  marks1 =int(schol_Marks[0])
  marks2 =int(schol_Marks[1])
  marks3 =int(schol_Marks[2])

  Avrag =(marks1+marks2+marks3)/3
  if Avrag >=90 and Avrag <=100:
    Grat ='AA'
  elif Avrag >=80 and Avrag <=89:
    Grat ='BA'
  elif Avrag >=70 and Avrag <=79:
    Grat ='BB'
  elif Avrag >=60 and Avrag <=69:
    Grat ='CB'
  elif Avrag >=50 and Avrag <=69:
    Grat ='CC'
  else:
    Grat ='FF'
    print("you are failed !!!")
  return student_Names+" :"+ Grat +"\n"




def read_Avg():
  with open("file_of_exam.text","r") as file:
    for rows in file:
      print(calculating_marks(rows))

def enter_Mark():
  name=input("Enter your name:")
  surname=input("Enter your surname:")
  marks1=input("Enter your marks 1:")
  marks2=input("Enter your marks2:")
  marks3=input("Enter your marks3:")
  with open("file_of_exam.text","a") as file:
    file.write(name+" "+surname+" :"+marks1+","+marks2+","+marks3+"\n")

def Regis_mark():
  with open("file_of_exam.text","r") as file:
    liste =[]
    for i in file:
      liste.append(calculating_marks(i))

    with open("result_of exam.text","w") as file2:
      for i in liste:
        file2.write(i)
  pass
while True:
  proc =input("1-read marks\n2-Enter your marks:\n3-register your mark\n4-exit_program :")
  if proc == '1':
    read_Avg()
  elif proc =='2':
    enter_Mark()
  elif proc =='3':
    Regis_mark()
  else:
      break