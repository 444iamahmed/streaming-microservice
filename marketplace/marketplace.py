import os
from flask import Flask, render_template, request, redirect, url_for
import grpc
import cgi
from recommendations_pb2 import MovieCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub
app = Flask(__name__)
app.debug = True
recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
categories = ['Mystery','Science Fiction','Comedy','Thriller','Action']
recommendations_client = RecommendationsStub(recommendations_channel)

@app.route("/")
def render_homepage():
  recommendations_request = RecommendationRequest(user_id=1, category=MovieCategory.ALL, max_results=20)
  recommendations_response = recommendations_client.Recommend(recommendations_request)
  return render_template("homepage.html", recommendations=recommendations_response.recommendations,)

@app.route('/dropdown', methods=['GET'])
def dropdown():
    return render_template('recommendations.html', categories = categories)

@app.route('/send_data', methods=['GET','POST'])
def send_data():
    if request.method == "POST":
        searchterm = request.form['categories']
        index = categories.index(searchterm)
        recommendations_request = RecommendationRequest(user_id=1, category=index, max_results=20)
        recommendations_response = recommendations_client.Recommend(recommendations_request)
        return render_template("show_recommendations.html", recommendations=recommendations_response.recommendations, )
    else:
        return render_template("recommendations.html")
if __name__ == "__main__":
    app.run()