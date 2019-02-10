from functools import reduce

from flask import Flask, render_template, request

from number_tool import get_prime_multipliers

app = Flask(__name__)


@app.route("/")
def main():
    """
    Main page
    :return: rendered html
    """
    return render_template('index.html')


@app.route("/getprimes", methods=["GET"])
def getprimes():
    """
    Page with results
    :return: rendered html
    """
    number = int(request.args.get("number"))
    # list of prime multipliers and index
    prime_numbers = [(i, x) for i, x in enumerate(get_prime_multipliers(number), 1)]
    return render_template('primes.html', number=number, prime_numbers=prime_numbers)


if __name__ == "__main__":
    app.run()
