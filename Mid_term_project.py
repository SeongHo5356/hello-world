name_1 = input("Enter first name : ")
name_2 = input("Enter second name : ")

name_1_list= name_1.split()
name_2_list=name_2.split()

new_list=[]
for name in (name_1_list):
    new_list.append(len(name))
    
for i in range(0,len(name_2_list)):
    new_list.insert((2*i)+1,len(name_2_list[i]))
    
rating_list = new_list[:]
while(len(rating_list)!=2):
    for i in range(0,len(rating_list)-1):
        rating_list[i]=(rating_list[i]+rating_list[i+1])%10
    rating_list.pop()

print("rating : ", int(rating_list[0])*10+int(rating_list[1]))