from flask import Flask,render_template
import pickle
import string
import nltk
from nltk.corpus import stopwords


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " "
    pickle.load(open('vectorizer.pkl','rb'))
    pickle.load(open('model.pkl','rb'))
app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.route('/predict',methods=['POST'])
def predict_spam():
   message= request.FORM.get('message')

   #prediction
   transformed_sms = transform_text(message)
   vector_input=transform([transformed_sms])
   result= predict(vector_input)[0]
   if result ==1:
       result="Spam"
   else:
       result="NotSpam"
   return render_template('index.html',result=result)

if __name__=='__main__':
    app.run(debug=True )