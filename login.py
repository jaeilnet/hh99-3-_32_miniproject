from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
import jwt
import datetime
import hashlib
import requests
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

client = MongoClient('localhost', 27017)
db = client.miniproject

# 메인 페이지
@app.route('/', methods=['GET'])
def home():
    token_receive = request.cookies.get('my_info')
    movie = list(db.moodtheater.find({}, {"_id": False}))
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        print("나는홈",user_info)
        return render_template('main.html', user_info=user_info, movie=movie)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

#로그인 페이지
@app.route('/login')
def login():
    return render_template('login.html')


# 메인페이지
@app.route('/main', methods=['GET'])
def main():
    # 토큰 가져오기
    token_receive = request.cookies.get('my_info')
    # 영화 목록 가져오기
    movie = list(db.moodtheater.find({}, {"_id": False}))
    try:
        # jw토큰 로그인 정보 디코드
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        # 현재 로그인 된 id와 일치하는 로그인 정보 가져오기
        user_info = db.users.find_one({"username": payload["id"]})

        # 메인 페이지 렌더링, db에서 가져온 로그인 정보, 영화 정보 main 페이지로 전달
        return render_template('main.html', user_info=user_info, movie=movie)
    except jwt.ExpiredSignatureError:

        # 토큰 시간이 완료되면 로그인 페이지로 보내버림 msg  - 시간이 만료 되었습니다.
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:

        # 토큰이 존재하지 않다면 로그인 페이지로 보내버림 msg 정보가 존재 하지 않습니다.
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

# Tag #울고싶은
@app.route('/main/123', methods=['GET'])
def tag1():
    token_receive = request.cookies.get('my_info')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})

        sad_counts = list(db.moodtheater.find({"sad_count": {"$gt": 0}}).sort('sad_count', -1))
        print(sad_counts)

        return render_template('mainTag.html', user_info=user_info, movie=sad_counts)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


# Tag #힐링되는
@app.route('/main/124', methods=['GET'])
def tag2():
    token_receive = request.cookies.get('my_info')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})

        healcounts = list(db.moodtheater.find({"heal_count": {"$gt": 0}}).sort('heal_count', -1))
        print(healcounts)

        return render_template('mainTag.html', user_info=user_info, movie=healcounts)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

# Tag #간질간질한
@app.route('/main/125', methods=['GET'])
def tag3():
    token_receive = request.cookies.get('my_info')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})

        itchy_counts = list(db.moodtheater.find({"itchy_count": {"$gt": 0}}).sort('itchy_count', -1))
        print(itchy_counts)

        return render_template('mainTag.html', user_info=user_info, movie=itchy_counts)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

# Tag #짜릿한
@app.route('/main/126', methods=['GET'])
def tag4():
    token_receive = request.cookies.get('my_info')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        
        thrillcounts = list(db.moodtheater.find({"thrill_count": {"$gt": 0}}).sort('thrill_count', -1))
        print(thrillcounts)

        return render_template('mainTag.html', user_info=user_info, movie=thrillcounts)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

# Tag #아기자기한
@app.route('/main/127', methods=['GET'])
def tag5():
    token_receive = request.cookies.get('my_info')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})

        baby_counts = list(db.moodtheater.find({"baby_count": {"$gt": 0}}).sort('baby_count', -1))
        print(baby_counts)

        return render_template('mainTag.html', user_info=user_info, movie=baby_counts)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

# Tag #매콤한
@app.route('/main/128', methods=['GET'])
def tag6():
    token_receive = request.cookies.get('my_info')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})

        spicy_counts = list(db.moodtheater.find({"spicy_count": {"$gt": 0}}).sort('spicy_count', -1))
        print(spicy_counts)

        return render_template('mainTag.html', user_info=user_info, movie=spicy_counts)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
         'id': username_receive,
         'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        print("로그인 palyload",payload)
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
        "nick_name": nickname_receive,                           # 프로필 이름 기본값은 아이디
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})

@app.route('/sign_up/username_check_dup', methods=['POST'])
def username_check_dup():
    username_receive = request.form['username_give']
    user_exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': user_exists})

@app.route('/sign_up/nickname_check_dup', methods=['POST'])
def nickname_check_dup():
    nickname_receive = request.form['nickname_give']
    nick_exists = bool(db.users.find_one({"nickname": nickname_receive}))
    return jsonify({'result': 'success', 'exists': nick_exists})


@app.route('/detail/<keyword>')
def detail(keyword):
    token_receive = request.cookies.get('my_info')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        movie = list(db.moodtheater.find({}, {"_id": False}))
        review = list(db.movie_review.find({}, {"_id": False}))

        print("나는 리뷰:",review)
        return render_template('detail.html', movie=movie, word=keyword, review=review, user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

@app.route('/api/review_create', methods=['POST'])
def review_create():
    title_receive = request.form["title_give"]
    review_receive = request.form["review_give"]
    tag_receive = request.form["tag_give"]
    nickname_receive = request.form["nickname_give"]

    compareSad = "울고싶은"
    compareHeal = "힐링되는"
    compareItchy = "간질간질한"
    compareThrill = "짜릿한"
    compareBaby = "아기자기한"
    compareSpicy = "매콤한"

    count01 = request.form["tag1_count"]
    count02 = request.form["tag2_count"]
    count03 = request.form["tag3_count"]
    count04 = request.form["tag4_count"]
    count05 = request.form["tag5_count"]
    count06 = request.form["tag6_count"]

    if tag_receive==compareSad:
        count = int(count01) + 1
        str(count)
        db.moodtheater.update({'title': title_receive}, {'$set': {'sad_count': count}})
    elif tag_receive==compareHeal:
        count = int(count02) + 1
        db.moodtheater.update({'title': title_receive}, {'$set': {'heal_count': count}})
    elif tag_receive == compareItchy:
        count = int(count03) + 1
        db.moodtheater.update({'title': title_receive}, {'$set': {'itchy_count': count}})
    elif tag_receive == compareThrill:
        count = int(count04) + 1
        db.moodtheater.update({'title': title_receive}, {'$set': {'thrill_count': count}})
    elif tag_receive == compareBaby:
        count = int(count05) + 1
        db.moodtheater.update({'title': title_receive}, {'$set': {'baby_count': count}})
    elif tag_receive == compareSpicy:
        count = int(count06) + 1
        db.moodtheater.update({'title': title_receive}, {'$set': {'spicy_count': count}})

    doc ={
        "title": title_receive, "review": review_receive, "tag": tag_receive, "nick_name": nickname_receive
    }

    db.movie_review.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '리뷰가 저장 되었습니다!!'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)