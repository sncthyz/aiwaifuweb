from flask import Flask, render_template
from waguri import waguri_bp

app = Flask(__name__)
app.secret_key = "Anjayakuganteng"
app.register_blueprint(waguri_bp)


@app.route('/')
def main():
    return render_template("index.html")
      

