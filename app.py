from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Global Azure 2025</title>
        <style>
            body {
                background: linear-gradient(135deg, #0078D4 0%, #00B4FF 100%);
                color: #fff;
                font-family: 'Segoe UI', Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: rgba(0,0,0,0.3);
                padding: 40px 60px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0,0,0,0.2);
                text-align: center;
            }
            h1 {
                font-size: 2.8rem;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.3rem;
                margin-top: 0;
            }
            .btn {
                margin-top: 30px;
                padding: 12px 32px;
                font-size: 1.1rem;
                background: #fff;
                color: #0078D4;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: background 0.2s;
            }
            .btn:hover {
                background: #e6e6e6;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Witaj na Global Azure 2025!</h1>
            <p>Twoja aplikacja działa poprawnie.<br>Miłego kodowania!</p>
            <a href="https://globalazure.pl" target="_blank" class="btn">Dowiedz się więcej</a>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)