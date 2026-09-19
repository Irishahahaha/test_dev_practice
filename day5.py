with open("test.txt", "w") as f:
    f.write("hello\n")
    f.write("world\n")
with open("test.txt", "r") as f:
    content = f.read()
    print(content)

import json
data={
    "name":"张三",
    "age":18,
    "skills":["python","java"]
}
with open("data.json","w") as f:
    json.dump(data,f,ensure_ascii=False,indent=2)

with open("data.json","r") as f:
    loaded=json.load(f)
print(loaded["name"])
print(loaded["skills"])