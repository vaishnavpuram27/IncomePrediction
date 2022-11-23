from flask import Flask,request,jsonify,render_template
import pickle

app = Flask(__name__)
model  = pickle.load(open("model.pkl",'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict',methods = ["POST"])
def predict():
    input_year = [x for x in request.form.values()]
    year = int(input_year[0])
    result = model.predict([[year]])[0][0]
    print(result)
    return render_template('index.html',prediction_text ='$ {}'.format(result))
    # return render_template('index.html')

if __name__ == "__main__":
    app.run()