# from flask import Flask, render_template, request, jsonify, redirect, url_for
# import requests
# from pymongo import MongoClient
#
# app = Flask(__name__)
#
# client = MongoClient('13.124.70.33', 27017, username="test", password="test")
# db = client.mini_project
#
# 메인 페이지
# @app.route('/main', methods=['GET'])
# def moive_list():
#     movie = list(db.moodtheater.find({}, {"_id": False}))
#     return render_template("pracmain.html", movie=movie)
#
# 상세 페이지
# @app.route('/detail/<keyword>')
# def detail(keyword):
#     movie = list(db.moodtheater.find({}, {"_id": False}))
#     review = list(db.movie_review.find({}, {"_id": False}))
#     return render_template("detail.html", movie=movie, word=keyword, review=review)
#
# 리뷰 저장하기
# @app.route('/api/review_create', methods=['POST'])
# def review_create():
#     title_receive = request.form["title_give"]
#     review_receive = request.form["review_give"]
#     tag_receive = request.form["tag_give"]
#
#     doc ={
#         "title": title_receive, "review": review_receive, "tag": tag_receive
#     }
#     db.movie_review.insert_one(doc)
#     return jsonify({'result': 'success', 'msg': '리뷰가 저장 되었습니다!!'})
#
# #리뷰 삭제하기
# @app.route('/api/review_delete', methods=['POST'])
# def review_delete():
#     review_receive = request.form["review_give"]
#     db.moodtheater.delete_one({"title": review_receive})
#     return jsonify({'result': 'success', 'msg': '리뷰가 삭제 되었습니다.'})
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)


