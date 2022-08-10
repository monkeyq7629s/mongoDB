# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 16:32:04 2022

@author: LEE HSIN-CHI
"""
#初始化資料庫連線
import pymongo
client = pymongo.MongoClient("mongodb+srv://root:root123@mycluster.6o3qc.mongodb.net/?retryWrites=true&w=majority")
db = client.member_system
print("資料庫連線建立成功")

#初始化flask伺服器
from flask import*
app = Flask(
    __name__, 
    static_folder = "public",
    static_url_path = "/"
    )

app.secret_key = "any string but secret"

#處理路由
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member():
    if "nickname" in session:
        return render_template("member.html")
    else:
        return redirect("/")

#/error?msg=錯誤訊息
@app.route("/error")
def error():
    message = request.args.get("msg", "發生錯誤，請聯繫客服")
    return render_template("error.html", message= message)

@app.route("/signup", methods=["POST"])
def signup():
    #從前端接收資料
    nickname = request.form["nickname"]
    email = request.form["email"]
    password = request.form["password"]
    # 根據資料，與資料庫互動
    collection = db.user
    #以email確認有沒有重複註冊
    result = collection.find_one({
        "email":email
        }) 
    if result != None:
        return redirect("/error?msg=信箱已經被註冊")
    
    #把資料放進資料庫並完成註冊
    collection.insert_one({
        "nickname":nickname,
        "email":email, 
        "password":password
        })
    return redirect("/")

@app.route("/signin", methods=["POST"])
def signin():
    #從前端取得使用者輸入資料
    email = request.form["email"]
    password = request.form["password"]
    #和資料庫作互動
    collection = db.user
    #檢查信箱是否正確
    result = collection.find_one({
        "$and":[
            {"email":email},
            {"password":password}
            ]
        })
    #找不到對應資料，登入失敗，導向錯誤頁面
    if result == None:
        return redirect("/error?msg=帳號或密碼輸入錯誤")
    #登入成功，導向會員頁面
    session["nickname"] = result["nickname"]
    return redirect("/member")

@app.route("/signout")
def signout():
    #移除session的會員資訊
    del session["nickname"]
    return redirect("/")

app.run(port = 3000)

