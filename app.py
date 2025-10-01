from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error = None
    if request.method == 'POST':
        binary = request.form.get('binary', '').strip()
        try:
            if not all(c in '01' for c in binary) or not binary:
                raise ValueError('Podaj poprawną liczbę binarną!')
            result = int(binary, 2)
        except Exception as e:
            error = str(e)
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Konwerter binarny &rarr; dziesiętny</title>
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
                font-size: 2.2rem;
                margin-bottom: 18px;
            }
            form {
                margin-bottom: 18px;
            }
            input[type="text"] {
                padding: 10px;
                font-size: 1.1rem;
                border-radius: 6px;
                border: none;
                margin-right: 10px;
                width: 180px;
            }
            button {
                padding: 10px 24px;
                font-size: 1.1rem;
                background: #fff;
                color: #0078D4;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: background 0.2s;
            }
            button:hover {
                background: #e6e6e6;
            }
            .result {
                font-size: 1.3rem;
                font-weight: bold;
                margin-top: 10px;
            }
            .error {
                color: #ffb3b3;
                font-weight: bold;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Konwerter binarny &rarr; dziesiętny</h1>
            <form method="post">
                <input type="text" name="binary" placeholder="np. 101101" autocomplete="off" required>
                <button type="submit">Przelicz</button>
            </form>
            {% if result is not none %}
                <div class="result">Wynik: {{ result }}</div>
            {% endif %}
            {% if error %}
                <div class="error">{{ error }}</div>
            {% endif %}
        </div>
    </body>
    </html>
    ''', result=result, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)