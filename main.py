from flask import Flask, request, jsonify, render_template
from datetime import datetime
import json
import os
import pandas as pd

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


@app.route('/solution', methods=['GET'])
def solution_page():
    f = open(r'static\zero-fees.txt', encoding='utf-8', mode='r')
    text = f.read()
    f.close()

    f = open(r'static\no-chargebacks.txt', encoding='utf-8', mode='r')
    text2 = f.read()
    f.close()

    f = open(r'static\no-registration.txt', encoding='utf-8', mode='r')
    text3 = f.read()
    f.close()

    return render_template('solution.html', text=text, text2=text2, text3=text3)


@app.route('/android-pos')
def android_pos_page():

    return render_template('android-pos.html')


@app.route('/apply-now')
def apply_now_page():

    return render_template('apply-now.html')


@app.route('/Hsdfsd120')
def blog_email_list_page():

    return render_template('blog-post-email.html')


@app.route('/Adfgbd6513')
def x_email_list_page():

    return render_template('x-post-email.html')

@app.route('/Casd57lxzv')
def x_email_list_2_page():

    return render_template('x-post-email-2.html')
    

@app.route('/Psdfcjbssd43')
def fb_email_list_page():

    return render_template('fb-post-email.html')


@app.route('/Nmasy898csaws')
def fb_email_list_2_page():

    return render_template('fb-post-email-2.html')


@app.route('/Xkfs98b8dfgsc', methods=['POST'])
def save_email():
    email = request.form.get('email')
    if email and '@' in email: 
        try:
            with open('data/subscribers.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append({
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "details": email,
        "event": "main"
        })

        with open('data/subscribers.json', 'w') as f:
            json.dump(data, f, indent=4)

        return render_template('demo-wallet-address.html')
    else:
        return jsonify({'message': 'Invalid email'}), 400


@app.route('/DxacxurY73', methods=['POST'])
def blog_email_list():
    email = request.form.get('email')
    if email and '@' in email: 
        try:
            with open('data/subscribers.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append({
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "details": email,
        "event": "blog"
        })

        with open('data/subscribers.json', 'w') as f:
            json.dump(data, f, indent=4)

        return render_template('welcome.html')
    else:
        return jsonify({'message': 'Invalid email'}), 400


@app.route('/Bsdfvx874d', methods=['POST'])
def x_email_list():
    email = request.form.get('email')
    if email and '@' in email: 
        try:
            with open('data/subscribers.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append({
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "details": email,
        "event": "x"
        })

        with open('data/subscribers.json', 'w') as f:
            json.dump(data, f, indent=4)

        return render_template('demo-wallet-address.html')
    else:
        return jsonify({'message': 'Invalid email'}), 400
        


@app.route('/Gcxaiuhas09', methods=['POST'])
def fb_email_list():
    email = request.form.get('email')
    if email and '@' in email: 
        try:
            with open('data/subscribers.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append({
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "details": email,
        "event": "fb"
        })

        with open('data/subscribers.json', 'w') as f:
            json.dump(data, f, indent=4)

        return render_template('demo-wallet-address.html')
    else:
        return jsonify({'message': 'Invalid email'}), 400


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

    data.append({
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "details": email,
        "event": "main"
    })

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    return render_template('welcome.html')

@app.route('/admin-dashboard')
def admin_dashboard_page():
    df = pd.read_json('data/subscribers.json')
    df = pd.DataFrame(df)
    logs = sorted(df.to_dict(orient='records'), key=lambda x: x['datetime'], reverse=True)

    total_subscription = df['event'].count() - 1

    df['datetime'] = pd.to_datetime(df['datetime'])
    first_datetime = df['datetime'].min()
    last_datetime = df['datetime'].max()
    total_duration = (last_datetime - first_datetime).days
    
    event_1 = 'main'
    event_2 = 'blog'
    event_3 = 'x'
    event_4 = 'fb'

    event_counts = df['event'].value_counts()

    try:
        count_1 = int(event_counts.get(event_1, 0))
    except KeyError:
        count_1 = 0
        
    try:
        count_2 = int(event_counts.get(event_2, 0))
    except KeyError:
        count_2 = 0
        
    try:
        count_3 = int(event_counts.get(event_3, 0))
    except KeyError:
        count_3 = 0
        
    try:
        count_4 = int(event_counts.get(event_4, 0))
    except KeyError:
        count_4 = 0

    data = pd.read_json('data/subscribers.json')
    data['datetime'] = pd.to_datetime(data['datetime'])
    event_counts_per_day = data.resample('D', on='datetime')['event'].count()
    labels = event_counts_per_day.index.strftime('%Y-%m-%d').tolist()
    data_values = event_counts_per_day.tolist()

    sales_data = {
        'labels': labels,
        'data': data_values
    }

    print(sales_data)

    return render_template('admin-dashboard.html', 
                           logs=logs, 
                           total_subscription=total_subscription, 
                           total_duration=total_duration,      
                           sales_data=sales_data,
                           event_1 = event_1,
                           event_2 = event_2,
                           event_3 = event_3,
                           event_4 = event_4,
                           count_1=count_1,
                           count_2=count_2,
                           count_3=count_3,
                           count_4=count_4)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
