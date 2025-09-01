from flask import Flask, render_template
from waguri import waguri_bp
from emilia import emilia_bp
from jeno import jeno_bp
from jisung import jisung_bp
from jiwoo import jiwoo_bp
from zerotwo import zerotwo_bp
from alya import alya_bp
from nanami import nanami_bp
from oreki import oreki_bp
from gojo import gojo_bp
from levi import levi_bp




app = Flask(__name__)
app.secret_key = "Anjayakuganteng"
app.register_blueprint(waguri_bp)
app.register_blueprint(gojo_bp)
app.register_blueprint(jiwoo_bp)
app.register_blueprint(emilia_bp)
app.register_blueprint(jisung_bp)
app.register_blueprint(nanami_bp)
app.register_blueprint(alya_bp)
app.register_blueprint(jeno_bp)
app.register_blueprint(zerotwo_bp)
app.register_blueprint(levi_bp)
app.register_blueprint(oreki_bp)





@app.route('/')
def main():
    return render_template("index.html")
      


if __name__ == "__main__":
    app.run(debug=True)