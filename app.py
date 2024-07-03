from flask import Flask, request, jsonify

app = Flask(__name__)

# Global variable ot store posts
posts = {
    0: {
        "id": 0,
        "title": "Hello world",
    }
}

post_id_counter = 1


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hi")
def hi():
    return "hi"


@app.route("/api/posts/", methods=["GET"])
def get_all_posts():
    return jsonify({"posts": list(posts.values())}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
