from pymongo import *
from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)

#  #连接runoob数据库，没有则自动创建
db = conn.runoob

# 使用coll集合，没有则创建
coll = db.coll

# 测试前先删除之前集合里的所有数据
db.coll.delete_many({})

coll.insert_one({"name": "zhangsan", "age": 18,  'contact': {"email": "132636@163.com"}})
coll.insert_one({"name": "wangge", "age": 15, "li": [1, 2, 3, 4, 5, 6]})
# 构造多级数据
coll.insert_one({"name": "NiuBi", "age": 0, "li": [1, 2, 5, 6],
                 'contact': {'email': '1234567@qq.com', 'phone': '11223344'}})
# 插入多条数据
users = [{"name": "LiSi", "age": 25}, {"name": "test", "age": 36}, {"name": "wanger", "age": 96}]
coll.insert_many(users)

# for i in coll.find():
#     print("User:", i)
# 查找
print("查找：", coll.find_one({"name": "zhangsan"}))
# 更新
coll.update_one({"name": "zhangsan"}, {'$set': {"age": 250}})
print("更新后：", coll.find_one({"name": "zhangsan"}))

# 删除
# coll.delete_one({"name": "zhangsan"})
print("查找张三年龄：", coll.find_one({"name": "zhangsan"})["age"])

print()
print("******所有用户信息********")
for i in coll.find():
    print("User--姓名：{} 年龄：{}".format(i["name"], i["age"]))

# limit()方法用来读取指定数量的数据
# skip()方法用来跳过指定数量的数据
print()
print("******skip和limit的用法***")
for i in coll.find().skip(1).limit(2):  # 跳过数据后读取两条
    print("User--姓名：{} 年龄：{}".format(i["name"], i["age"]))

print()
print("******年龄大于25岁的用户信息****")
# 查询年龄大于25岁的用户，结果按年龄升序排列,1为升序，2为降序
for i in coll.find({"age": {"$gt": 25}}).sort([("age", 1)]):
    print("姓名:{},年龄：{}".format(i["name"], i["age"]))

print()
print("******push、pushall******")
coll.update_one({"name": "NiuBi"}, {"$push": {"li": 100}})
for i in coll.find({"name": "NiuBi"}):
    print("\"li\"  push->100:", i["li"])
coll.update_one({"name": "NiuBi"}, {"$pushAll": {"li": [1000, 2000]}})
for i in coll.find({"name": "NiuBi"}):
    print("\"li\"  pushAll->[1000,2000]:", i["li"])

print()
print("*******pop/pull/pullAll****")
# pop(1)移除最后一个元素(-1为移除第一个)
coll.update_one({"name": "NiuBi"}, {"$pop": {"li": 1}})
for i in coll.find({"name": "NiuBi"}):
    print("\"li\"  pop->1:", i["li"])
# pull按值移除
coll.update_one({"name": "NiuBi"}, {"$pull": {"li": 1}})
for i in coll.find({"name": "NiuBi"}):
    print("\"li\"  pull->1:", i["li"])
# pullAll移除所有符合条件的
coll.update_one({"name": "NiuBi"}, {"$pullAll": {"li": [2, 5, 6]}})
for i in coll.find({"name": "NiuBi"}):
    print("\"li\"  pullAll->[2, 5, 6]:", i["li"])

# 多级目录用.连接
print("查找电话为11223344的邮箱：", coll.find_one({"contact.phone": "11223344"})["contact"]["email"])

# 多级目录下的修改操作
coll.update_one({"contact.phone": "11223344"}, {"$set": {"contact.email": "99999@163.com"}})
print("修改后的邮箱：", coll.find_one({"contact.phone": "11223344"})["contact"]["email"])

for i in coll.find():
    print(i)















