import aiohttp

import conf


async def fetch_data(cfg: conf.Config, skip: int = 0, limit: int = 1):
    """
    Fetch data from Qualis.
    :param cfg: Config
    :param skip: How many records to skip
    :param limit: How many records to fetch
    :return: list of dicts with data
    """
    result = []
    err = None
    url = cfg.qualys_url
    headers = {
        "token": cfg.api_token,
    }
    params = {"skip": skip, "limit": limit}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, params=params, headers=headers) as resp:
            if resp.status != 200:
                err = await resp.text()
                if ">number of hosts" in err:
                    err = "less_limit"
            else:
                result = await resp.json()
            return result, err, limit