# Задания средний балл

grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]] # Список 
studes= {'Johnny','Bildo','Steve','Khendrik','Aaron'}   # Множество

studes=list(studes) # Множество преобразования в лист
#print(studes)

a=sum(grades[0])/len(grades[0]) # решение сред.ариф
b=sum(grades[1])/len(grades[1])
c=sum(grades[2])/len(grades[2])
d=sum(grades[3])/len(grades[3])
f=sum(grades[4])/len(grades[4])

grades_studes=dict(zip(studes,(a,b,c,d,f)))  # преобразования в словарь 
print(grades_studes)
