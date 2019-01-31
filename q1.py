'''Task 1
i. Write a program which can read a list of students with their roll numbers and save
it in the form of dictionary with {rollnumber:Name}must have at least 10 students with
name and roll number.
ii. Save this file as my_friends.txt.
iii. From this file now read each name and find vowels used in each student name.
iv. Find the maximum and minimum names with vowels in the list and save it in the same
file with the text on the top The Max and Min Vowels. For example: Ali got 2 vowels so it’s
 the smallest whereas Syed Muhammad Jibran Ali will have 8 vowels will come as maximum.'''



student = []
for x in range(10):
    st = []
    roll = input("enter roll:")
    st.append(roll)
    name = input("enter name:")
    st.append(name)

    student.append(st)
student_dict = dict(student)

write_to_file = []
for key,val in student_dict.items():
    text_to_append = key+' '+val+'\n'
    write_to_file.append(text_to_append)

my_friend_file = open('my_friends.txt','w')
my_friend_file.writelines(write_to_file)
my_friend_file.close()

my_friend_file = open('my_friends.txt','r')
friends_text = my_friend_file.readlines()
my_friend_file.close()

names = []
for each in friends_text:
    splitted_line = each.split()
    del splitted_line[0]
    names.append(' '.join(splitted_line))

def vovels_num(name):
    count = 0
    for char in name:
        if char in 'aeiouAEIOU':
            count+=1
    return count

vovels_in_each_name = {}
for each in names:
    num_of_vovels = vovels_num(each)
    vovels_in_each_name[each] = num_of_vovels
print(vovels_in_each_name)

max_vovels = {}
for k,v in vovels_in_each_name.items():
    if v is max(vovels_in_each_name.values()):
        max_vovels[k] = v

min_vovels = {}
for k,v in vovels_in_each_name.items():
    if v is min(vovels_in_each_name.values()):
        min_vovels[k] = v
print(max_vovels)
print(min_vovels)

my_friend_file = open('my_friends.txt','r')
text_in_file = my_friend_file.readlines()
my_friend_file.close()

max_text = ''
for k,v in max_vovels.items():
    max_text +=k+' '+str(v)+'\n'

min_text = ''
for k,v in min_vovels.items():
    min_text +=k+' '+str(v)+'\n'

text_in_file.insert(0,min_text)
text_in_file.insert(0,'Min\n')
text_in_file.insert(0,max_text)
text_in_file.insert(0,'Max\n')

print(text_in_file)
my_friend_file = open('my_friends.txt','w')
my_friend_file.writelines(text_in_file)
my_friend_file.close()