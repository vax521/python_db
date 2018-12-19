from pymongo import MongoClient

# 连接配置
settings = {
    "ip": "127.0.0.1",
    "port": 27017,
    "db_name": "runoob",
    "set_name": "coll"
}


class MyMongoDB(object):
    def __init__(self):
        try:
            self.conn = MongoClient(settings["ip"],settings["port"])
        except Exception as e:
            print(e)
        self.db = self.conn[settings["db_name"]]
        self.my_set = self.db[settings["set_name"]]

    def insert(self, dict):
        print("Insert....")
        self.my_set.insert(dict)

    def update(self, dict, newDict):
        print("Update...")
        self.my_set.update(dict, newDict)

    def delete(self, dict):
        print("Delete...")
        self.my_set.remove(dict)

    def dbFind(self, dict):
        print("Find...")
        data = self.my_set.find(dict)
        for result in data:
            print("姓名：{}，年龄：{}".format(result["name"],result["age"]))


def main():
    dict = {"name": "xingXF", "age": 100}
    mongo = MyMongoDB()
    mongo.insert(dict)
    mongo.dbFind({"name": "xingXF"})

    mongo.update({"name": "xingXF"}, {"$set": {"age": "24"}})

    mongo.update({"name": "xingXF"}, {"$set":{"age": "25"}})
    mongo.dbFind({"name": "xingXF"})

    mongo.delete({"name": "xingXF"})
    mongo.dbFind({"name": "xingXF"})

if __name__ == "__main__":
    main()














