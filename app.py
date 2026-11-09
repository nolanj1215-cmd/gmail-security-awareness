from flask import Flask, render_template_string

app = Flask(__name__)

page = """
<!DOCTYPE html>
<html>
<head>
<title>Gmail Security Awareness</title>
<style>
body {
    font-family: Arial;
    background: #f1f3f4;
    text-align: center;
    padding: 50px;
}
.box {
    background: white;
    padding: 30px;
    margin: auto;
    max-width: 400px;
    border-radius: 12px;
}
button {
    background: #4285f4;
    color: white;
    padding: 12px;
    border: none;
    border-radius: 5px;
}
</style>
</head>
<body>
<div class="box">
<h2>Gmail Security Awareness</h2>
<p>This is a cybersecurity training simulation.</p>
<p>A suspicious email asks you to verify your
Google account immediately.</p>
<p><b>Would you trust that email?</b></p>
<button onclick="alert('Training lesson: Never enter your password through an unexpected email link. Visit Google directly instead.')">
Reveal the lesson
</button>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(page)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

