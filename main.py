from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'my_secret_key'

if not os.path.exists('data'):
    os.makedirs('data')

@app.route('/')
def home_page():
    return render_template('simplify-your-crypto-payments.html')

@app.route('/terms-and-condition', methods=['GET'])
def terms_and_condition_page():
    f = open(r'static\terms-and-condition.txt', encoding='utf-8', mode='r')
    text = f.read()
    f.close()

    return render_template('terms-and-condition.html', text=text)
    
@app.route('/privacy-policy', methods=['GET'])
def privacy_policy_page():
    f = open(r'static\privacy-policy.txt', encoding='utf-8', mode='r')
    text = f.read()
    f.close()

    return render_template('privacy-policy.html', text=text)

@app.route('/AufAED35', methods=['GET','POST'])
def subscribe():
    email = request.form.get('Footer-Email')
    if not email:
        return jsonify({"error": "Email is required"}), 400
    
    file_path = 'data/subscribers.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        data = []

    data.append({'email': email})

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    return render_template('simplify-your-crypto-payments.html', 
                            success="Thank you! Your submission has been received!", 
                            error="Oops! Something went wrong while submitting the form.")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
