# Tax Calculator
# My tax brackets:
#   $0 to $20,000: 15%
#   Above $20,000 to $50,000: 25%
#   Above $50,000: 35%

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    income_text = request.form.get("income", "")
    if income_text == "":
        return render_template('error.html', message="Please enter an income"), 400
    income = float(income_text)

    if income < 0:
        return render_template('error.html', message="Income cannot be negative"), 400

    if income <= 20000:
        tax = income * 0.15
    elif income <= 50000:
        tax = (20000 * 0.15) + ((income - 20000) * 0.25)
    else:
        tax = (20000 * 0.15) + (30000 * 0.25) + ((income - 50000) * 0.35)

    return render_template('result.html', income=f"${income:,.2f}", tax=f"${tax:,.2f}")


if __name__ == '__main__':
    app.run(debug=True)