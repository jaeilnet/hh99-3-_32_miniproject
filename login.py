from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

client = MongoClient('13.124.70.33', 27017, username="test", password="test")
db = client.mini_project

# 메인페이지에서 사용
# @app.route('/')
# def home():
#     token_receive = request.cookies.get('my_info')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#
#         return render_template('login.html')
#     except jwt.ExpiredSignatureError:
#         return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
#     except jwt.exceptions.DecodeError:
#         return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    # nickname_receive = request.form["nickname_give"]


    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
         'id': username_receive,
         # 'nickname' : nickname_receive,
         'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})




@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    nickname_receive = request.form['nickname_give']

    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,                               # 아이디
        "password": password_hash,                                  # 비밀번호
        "nick_name": nickname_receive,                              # 닉네임
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


# 아이디 중복확인
@app.route('/sign_up/username_check_dup', methods=['POST'])
def username_check_dup():
    username_receive = request.form['username_give']
    user_exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': user_exists})

# 닉네임 중복확인
@app.route('/sign_up/nickname_check_dup', methods=['POST'])
def nickname_check_dup():
    nickname_receive = request.form['nickname_give']
    nick_exists = bool(db.users.find_one({"nickname": nickname_receive}))
    return jsonify({'result': 'success', 'exists': nick_exists})


# @app.route('/update_profile', methods=['POST'])
# def save_img():
#     token_receive = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         # 프로필 업데이트
#         return jsonify({"result": "success", 'msg': '프로필을 업데이트했습니다.'})
#     except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
#         return redirect(url_for("home"))
#
#
# @app.route('/posting', methods=['POST'])
# def posting():
#     token_receive = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         # 포스팅하기
#         return jsonify({"result": "success", 'msg': '포스팅 성공'})
#     except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
#         return redirect(url_for("home"))

# 메인페이지 이동
@app.route('/detail')
def detail():
    # return render_template("detail.html")
    token_receive = request.cookies.get('my_info')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username" : payload["id"]})
        print(user_info)
        return render_template("detail.html", user_info=user_info)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("login", msg="로그인 다시 해주세요."))


@app.route('/api/save_word', methods=['POST'])
def save_word():
    # 리뷰 저장하기
    review_receive = request.form["review_give"]
    tag_receive = request.form["tag_give"]
    nickname_receive = request.form["nickname_give"]
    doc = {
            "nicknames": nickname_receive,
            "review": review_receive,
            "tag": tag_receive,
           }
    db.reviews.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '리뷰가 저장되었습니다.'})


@app.route('/api/delete_word', methods=['POST'])
def delete_word():
    # 리뷰 삭제하기
    return jsonify({'result': 'success', 'msg': '리뷰가 삭제되었습니다.'})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)