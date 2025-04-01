import requests

import conf


def fetch_data(cfg: conf.Config, skip: int = 0, limit: int = 1):
    result = []
    err = None
    url = cfg.qualys_url
    headers = {
        "token": cfg.api_token,
    }
    req = requests.post(url, params={"skip": skip, "limit": limit}, headers=headers)
    if req.status_code != 200:
        err = req.text
        if ">number of hosts" in err:
            err = "less_limit"
    else:
        result = req.json()
    return result, err, limit