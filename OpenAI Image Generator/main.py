from flask import Flask, jsonify
from config import key
import openai
from flask import render_template

app = Flask(__name__)
openai.api_key=key


@app.route('/')
def index():
  return render_template('index.html')
@app.route('/generateimages/<prompt>')
def generate(prompt):
  print("prompt: ", prompt)
  response = openai.Image.create(prompt=prompt, n=3, size="256x256")
  print(response)
  # Extract the required data from the response
  #images = response['data']
  # Create a list of image URLs
  #image_urls = [image['url'] for image in images]
  # Return the image URLs as JSON
  return jsonify(response)


app.run(host='0.0.0.0', port=81)
