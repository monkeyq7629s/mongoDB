# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:03:05 2022

@author: LEE HSIN-CHI
"""
clear
#載入pymongo套件
import pymongo
from bson.objectid import ObjectId

#連線到mongoDB雲端資料庫
client = pymongo.MongoClient("mongodb+srv://root:root123@mycluster.6o3qc.mongodb.net/?retryWrites=true&w=majority")

#把資料放進資料庫中
db = client.mywebsite #選擇操作mywebsite資料庫
collection = db.users #選擇操作users集合

# #篩選集合中的文件資料
# doc = collection.find_one({
#     "email":"ply@ply.com"
#     })
# print("取得的資料的名字欄位:", doc["name"])
# #複合篩選條件
# doc = collection.find_one({
#     "$and":[
#         {"email":"ply@ply.com"},
#         {"password":"ply"}]
#     })
# print("取得的資料",doc)
#篩選結果排序
cursor = collection.find({
    "$or":[
        {"email":"ply@ply.com"},
        {"level":1}
        ]
    }, sort= [
        ("level", pymongo.ASCENDING)
        ])
for c in cursor:
    print(c)

# #更新集合中的一筆文件資料
# result = collection.update_one({
#     "email":"ply@ply.com"
#     },{
#        "$mul":{
#            "level":0.25
#            }
#        }
#     )
# print("符合篩選條件的文件數量", result.matched_count)
# print("實際更新的文件數量", result.modified_count)

# #更新集合中的多筆文件資料
# result = collection.update_many({
#     "level":2
#     }, {
#         "$set":{
#             "level":4
#             }
#         })
# print("符合篩選條件的文件數量", result.matched_count)
# print("實際更新的文件數量", result.modified_count)

# #取得集合中的第1筆文件資料
# data = collection.find_one()
# print(data)
# #根據objectID取得文件資料
# data = collection.find_one(ObjectId("62ea745869ab514ae5e5bac3"))
# print(data)
# #取得文件資料中的欄位
# print(data["_id"])
# print(data["email"])
#一次取得多筆文件資料
# cursor=collection.find()
# print(cursor)
# for doc in cursor:
#     print(doc["name"])
# #一次新增多筆資料，取得多筆資料的編號
# result = collection.insert_many([{
#      "name":"阿爭",
#      "email":"jin@jin.com",
#      "passoword":"jin",
#      "level":2
#     }, {
#         "name":"澎澎",
#         "email":"ply@ply.com",
#         "passoword":"ply",
#         "level":1
#         }
#     ]
#     )

# #把資料新增到集合中(json格式)
# collection.insert_one({
#     "name":"阿爭",
#     "email":"jin@jin.com",
#     "passoword":"jin",
#     "level":2
#     })

#print("資料新增成功")
#print(collection.inserted_id)