from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'my_secret_key'

@app.route('/home', methods=['GET'])
def home_page():
    f = open('static\intro_1.txt', encoding='utf-8', mode='r')
    intro_1 = f.read()
    f.close()

    f = open('static\intro_2.txt', encoding='utf-8', mode='r')
    intro_2 = f.read()
    f.close()

    f = open('static\intro_3.txt', encoding='utf-8', mode='r')
    intro_3 = f.read()
    f.close()

    return render_template('home.html', intro_1=intro_1, intro_2=intro_2, intro_3=intro_3)


@app.route('/airdrop', methods=['GET'])
def airdrop_page():
    f = open('static\drop_1.txt', encoding='utf-8', mode='r')
    drop_1 = f.read()
    f.close()

    f = open('static\drop_2.txt', encoding='utf-8', mode='r')
    drop_2 = f.readlines()
    f.close()

    f = open('static\intro_3.txt', encoding='utf-8', mode='r')
    intro_3 = f.read()
    f.close()

    return render_template('airdrop.html', drop_1=drop_1, drop_2=drop_2, intro_3=intro_3)


@app.route('/faqs', methods=['GET'])
def faqs_page():
    f = open('static\intro_3.txt', encoding='utf-8', mode='r')
    intro_3 = f.read()
    f.close()

    f = open(r'static\faq_1.txt', encoding='utf-8', mode='r')
    faq_1 = f.read()
    f.close()
    
    f = open(r'static\faq_2.txt', encoding='utf-8', mode='r')
    faq_2 = f.read()
    f.close()

    f = open(r'static\faq_3.txt', encoding='utf-8', mode='r')
    faq_3 = f.read()
    f.close()

    f = open(r'static\faq_4.txt', encoding='utf-8', mode='r')
    faq_4 = f.read()
    f.close()

    f = open(r'static\faq_5.txt', encoding='utf-8', mode='r')
    faq_5 = f.read()
    f.close()

    f = open(r'static\faq_6.txt', encoding='utf-8', mode='r')
    faq_6 = f.read()
    f.close()

    f = open(r'static\faq_7.txt', encoding='utf-8', mode='r')
    faq_7 = f.read()
    f.close()

    f = open(r'static\faq_8.txt', encoding='utf-8', mode='r')
    faq_8 = f.read()
    f.close()

    f = open(r'static\faq_9.txt', encoding='utf-8', mode='r')
    faq_9 = f.read()
    f.close()

    f = open(r'static\faq_10.txt', encoding='utf-8', mode='r')
    faq_10 = f.read()
    f.close()

    return render_template('faqs.html', intro_3=intro_3, faq_1=faq_1, faq_2=faq_2,
                            faq_3=faq_3, faq_4=faq_4, faq_5=faq_5, faq_6=faq_6, 
                            faq_7=faq_7, faq_8=faq_8, faq_9=faq_9, faq_10=faq_10)

@app.route('/terms-and-condition', methods=['GET'])
def tc_page():
    f = open(r'static\tc.txt', encoding='utf-8', mode='r')
    tc = f.read()
    f.close()

    f = open('static\intro_3.txt', encoding='utf-8', mode='r')
    intro_3 = f.read()
    f.close()

    return render_template('terms-and-condition.html', tc=tc, intro_3=intro_3)

@app.route('/private-policy', methods=['GET'])
def pp_page():
    f = open(r'static\pp.txt', encoding='utf-8', mode='r')
    pp = f.read()
    f.close()

    f = open('static\intro_3.txt', encoding='utf-8', mode='r')
    intro_3 = f.read()
    f.close()

    return render_template('private-policy.html', pp=pp, intro_3=intro_3)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)