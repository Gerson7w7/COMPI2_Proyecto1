from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin": "*"}})

@app.route("/")
def hello_world():
    return "HOLAAA"


# @app.route('/api/interpretar', methods=['POST'])
# def interpretar():
#     if request.method == 'POST':
#         result = parser.parse('2 * 3 + 4 * (5 - 4)')
#         return {
#             'resultado': result
#         }

if __name__=='__main__':
    app.run(debug = True, port = 5000)