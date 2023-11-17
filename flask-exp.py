from flask import Flask, Response
from main import crontab, subscriber_message
from flask_apscheduler import APScheduler
import requests
app = Flask(__name__)

def request_app(url):

    try:
        response_token = requests.get(url=url)
    except Exception as e:
        return e, 401

    return response_token, 200


def hacer_suma():
    print('hace suma')
    return 1


@app.route('/')
def saludo():
    import os
    url = os.getenv('URL_1', 'http://app_candidate:3000/candidate/ping/')
    print(url)
    import logging
    logging.warning(f'PROJECT! {url}')
    a, b = request_app(url=url)
    return f'Mi primer programa Flask!{a.text} {b}'

@app.route('/stream')
def stream():

    return Response(subscriber_message(app),
                          mimetype="text/event-stream")




if __name__ == '__main__':
    # import threading
    #
    # def funcion_1():
    #     app.test_client().get('/stream')
    #
    # threading_emails = threading.Thread(target=funcion_1)
    #
    #
    # threading_emails.start()
    # app.debug = True
    app.run(threaded=True, port=5000)




