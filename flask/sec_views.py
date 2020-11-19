from flask import request, jsonify
from flask.views import MethodView


lst = []


class SecondaryView(MethodView):

    def get(self):
        return jsonify({"messages": lst})

    def post(self):
        rep_message = request.get_json().get("rep_message")
        lst.append(rep_message)
        return jsonify({'description': 'Replication Success'}), 201
