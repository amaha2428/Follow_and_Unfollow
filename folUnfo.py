from flask import Flask, request, jsonify
import mysql.connector as db


app = Flask(__name__)


mydb = db.connect(host='localhost', user='root', passwd='Put_your_password', database='socia_medial')

cur = mydb.cursor()

def follow(follower_id, following_id):
  cur.execute("INSERT INTO user_followers (follower_id, following_id) VALUE (%s, %s) ", (follower_id, following_id))
  mydb.commit()
  return True

def unfollow(follower_id, following_id):
  cur.execute("DELETE FROM user_followers WHERE follower_id=%s AND following_id=%s", (follower_id, following_id))
  mydb.commit()
  return True

@app.route('/api/follow', methods=['POST'])
def follow_route():
  # code to handle the follow request goes here
  data = request.get_json(force=True)
  follower_id = data['follower_id']
  following_id = data['following_id']
  # code to follow the user goes here

  result = follow(follower_id, following_id)

  if result:
  #  return jsonify({'message': 'Successfully followed user'}), 200
    return jsonify({'success': True})

  else:
    return jsonify({'success': False, 'error': 'An error occurred while trying to follow the user.'})


@app.route('/api/unfollow', methods=['DELETE'])
def unfollow_route():
  # code to handle the unfollow request goes here
  data = request.get_json()
  follower_id = data['follower_id']
  following_id = data['following_id']
  # code to unfollow the user goes here
  result = unfollow(follower_id, following_id)

  if result:
    return jsonify({'success': True})

  else:
    return jsonify({'success': False, 'error': 'An error occurred while trying to unfollow the user.'})
  

if __name__ == '__main__':
  app.run(debug=True)