import requests


class BoardApi:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    def get_all_boards_by_org_id(self, org_id: str) -> dict:
        path = ("{trello}/organizations/{id}?boards=open&board_fields=all&fields=boards".
                format(trello=self.base_url, id=org_id))
        cookie = {"token": self.token}
        resp = requests.get(path, cookies=cookie)
        return resp.json()