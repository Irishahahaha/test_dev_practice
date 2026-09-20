import json
users=[
    {"name":"张三","age":18},
    {"name":"李四","age":20},
    {"name":"王五","age":22},
]
with open('users.json','w') as f:
    json.dump(users,f,ensure_ascii=False,indent=2)
with open('users.json','r') as f:
    loded=json.load(f)
ages=[u["age"] for u in loded]
print("平均年龄：",sum(ages)/len(ages))
oldest=max(loded,key=lambda u:u["age"])
print("年龄最大：",oldest["name"])
sorted_users=sorted(loded,key=lambda u:u["age"])
print("按年龄排序：",[u["name"] for u in sorted_users])