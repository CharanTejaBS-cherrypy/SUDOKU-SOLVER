from flask import Flask, render_template, request, jsonify
from solver import solve_sudoku, is_valid_sudoku

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/solve', methods=['POST'])
def solve():
    grid = request.json['grid']
    if is_valid_sudoku(grid):
        solution = solve_sudoku(grid)
        return jsonify({'solution': solution, 'valid': True})
    else:
        return jsonify({'message': 'Invalid input', 'valid': False})


if __name__ == '__main__':
    app.run(debug=True)
