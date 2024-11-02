from flask import Flask, request
from src.api.route_controllers.StatusHistoryController import StatusHistoryController
from os import getenv


debug = getenv("DEBUG_MODE")
app = Flask(__name__)


@app.route("/issue/status_history", methods=['GET'])
def issue_status_history():
    issue_key = request.args.get('issue_key')
    time_format = request.args.get('time_format')
    return StatusHistoryController.get_issue_status_history(issue_key=issue_key, time_format=time_format), 200


if __name__ == '__main__':
    app.run(debug=True)
