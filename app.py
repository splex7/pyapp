from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello~! CI/CD 파이프라인에 오신 것을 진심으로 환영합니다!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
