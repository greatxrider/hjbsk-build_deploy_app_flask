"""This is a module for mathematics functions"""
from flask import Flask, render_template, request
from Maths.mathematics import summation, subtraction, multiplication
# Import the Maths package here

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    """sum_route is a function that returns the sum of two numbers"""
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    result = summation(num1, num2)
    return str(result)

@app.route("/sub")
def sub_route():
    """sub_route is a function that returns the difference of two numbers"""
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    result = subtraction(num1, num2)
    return str(result)

@app.route("/mul")
def mul_route():
    """mul_route is a function that returns the product of two numbers"""
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    result = multiplication(num1, num2)
    return str(result)

@app.route("/")
def render_index_page():
    """render_index_page is a function that renders the index.html page"""
    # Write your code here
    return render_template("index.html")

@app.errorhandler(404)
def api_not_found(error):
    """Error handler for 404"""
    return {"message": "API not found"}, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
