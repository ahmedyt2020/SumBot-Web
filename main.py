from flask import Flask, render_template
import json

with open("config.json", "r") as f:
    config = json.load(f)

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html", pagetitle='SumBot')

@app.route("/commands")
def commands():
  return render_template("commands.html", pagetitle="commands")

@app.route("/support")
def support():
  return '<meta http-equiv="refresh" content="0; url={}">'.format(config['support'])

@app.route("/invite")
def invite():
  return '<meta http-equiv="refresh" content="0; url=https://discord.com/api/oauth2/authorize?client_id={}&permissions=8&scope=bot">'.format(str(config['client_id']))

@app.route("/source")
def source():
  return '<meta http-equiv="refresh" content="0; url=https://discord.com/api/oauth2/authorize?client_id={}&permissions=8&scope=bot">'.format(str(config['client_id']))

@app.route("/vote")
def vote():
  return '<meta http-equiv="refresh" content="0; url=https://top.gg/bot/{}/vote">'.format(str(config['client_id']))

if __name__ == "__main__":
  app.run(debug=True, port=9000)