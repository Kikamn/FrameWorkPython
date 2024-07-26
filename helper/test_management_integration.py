import requests
from helper.config import *


def push_result(case_id, status):
    payload = {
        "case_id": case_id,
        "status": status
    }

    head = {
        "accept": "application/json",
        "content-type": "application/json",
        "Token": TOKEN_QASE_IO
    }

    resp = requests.post(f"{host_QaseIO}{project_ID}/{test_run_id}", json=payload, headers=head)