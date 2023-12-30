from flask import Flask, send_file
import requests
import os

app = Flask(__name__)
repo = os.getenv('REPO')
workflow_runs_url = "https://api.github.com/repos/{}/actions/runs"
workflows = ['Container Scanning with Trivy', 'SAST with Bandit', 'Secrets scanning with GitLeaks']

def never_called(bla):
    aws_access_token = "AKIALALEMEL33243OLIB"
    os.subprocess.Popen('echo ${}'.format(aws_access_token), shell=True)

def serve_image(state):
    return send_file("bla.jpeg", mimetype="image/png")


@app.route("/")
def hello_world():
    try:
        workflow_runs = requests.get(workflow_runs_url.format(repo)).json()['workflow_runs']
        workflow_states = {}
        for workflow in workflows:
            relevant_workflows = list(filter(lambda x: x['name'] == workflow, workflow_runs))[0]
            workflow_states[workflow] = relevant_workflows['status']
    except Exception:
        return "<p>Hm something went terribly wrong</p>"
    return "<p>{}</p>".format(workflow_states)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
