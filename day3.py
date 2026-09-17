person={
    "name":"Amy",
    "age":18,
    "major":"software engineer",
}
print(person["name"])
print(person.get("age"))
print(person.get("gender","未知"))#无key返回默认

person["age"]=19
person["school"]="东北大学"

for key,value in person.items():
    print(key,":",value)

nums=[1,2,3,4,4,1]
unique=set(nums)  #set适合判断是否出现过
print(unique)
print(2 in unique)
print(10 in unique)

s="Hello,world"
print(s.split()) #['hello','world']
print(s.lower())
print(s.replace("world","python"))
print(s.startswith("Hello"))
print(len(s))