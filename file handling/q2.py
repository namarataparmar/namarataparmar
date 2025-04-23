def q2():
     students_data={}
     f=open('marks.csv','r')
     lines=f.readlines()
     for line in lines[1:]:           #strt with one bcoz we dont want headings
         data=line.strip().split(',')
         rollNo=int(data[0])
         name=data[1]
         sub1=int(data[2])
         sub2=int(data[3])
         sub3=int(data[4])
         total=chemisty+maths+english
         students_data[rollno]={
             "name":name,
             "sub1":sub1,
             "sub2":sub2,
             "sub3":sub3,
             "total":total
         }
     print(students_data)
q2()
