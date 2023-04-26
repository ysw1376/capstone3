from todolist import create_app
from flask import Flask
from flask import request, render_template, jsonify
import json

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)







