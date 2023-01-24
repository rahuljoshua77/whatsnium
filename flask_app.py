import time,json,os
from urllib.parse import quote
from flask import Flask, request, jsonify,render_template,redirect,url_for
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
app = Flask(__name__)
cwd = os.getcwd()
opts = Options()
opts.add_argument("--headless=chrome")

opts.add_argument('--disable-dev-shm-usage')
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-gpu")
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=opts)

@app.route("/")
def index():
    driver.get("https://web.whatsapp.com")
    return render_template('index.html')

@app.route("/qr")
def qr():
    try:
        element_qr = wait(driver,5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="landing-window"]')))
        element_qr.screenshot(f"mysite/static/qr_code.png")
        return render_template('qr.html')
    except Exception as e:
        try:
            check_login = driver.find_elements_by_xpath('//header[@data-testid="chatlist-header"]')
            if len(check_login) > 0:
                return redirect(url_for('login'))
            else:
                pass
        except Exception as e:
            return e

@app.route("/login")
def login():
    try:
        check = wait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//header[@data-testid="chatlist-header"]')))
        return render_template('logged.html')
    except Exception as e:
        return render_template('err.html')

@app.route("/docs")
def docs():
    return render_template('docs.html')

@app.route("/wait")
def waiting():
    return render_template('wait.html')

@app.route('/logout', methods=['POST'])
def logout():
    wait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//span[@data-testid="menu"]'))).click()
    try:
        wait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//li[@data-testid="mi-logout menu-item"]'))).click()
    except:
        wait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//li[@data-testid="mi-logout menu-item"]/div'))).click()
    time.sleep(1)
    wait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="popup-controls-ok"]'))).click()
    time.sleep(5)
    return redirect(url_for('index'))

@app.route('/send_message', methods=['POST'])
def send_message():
    # Get data from the request
    data = request.get_json()
    contact = data['contact']
    message = data['message']
    # Encode the URL
    encoded_url = quote(message)
    driver.get(f'https://web.whatsapp.com/send?phone=${contact}&text={encoded_url}')
    time.sleep(2)
    wait(driver,35).until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="conversation-compose-box-input"]'))).send_keys(Keys.ENTER)
    return jsonify({'status': 'success'})

@app.route("/check_login")
def check_login():
    try:
        check_login = driver.find_elements_by_xpath('//header[@data-testid="chatlist-header"]')
        if len(check_login) > 0:
            return jsonify({'status': 'logged in'})
        else:
            return jsonify({'status': 'not logged in'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=False)