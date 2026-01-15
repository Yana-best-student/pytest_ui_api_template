from api.BoardApi import BoardApi

def test_get_boards():
    api = BoardApi("https://api.trello.com/1")
    board_list = api.get_all_boards_by_org_id("1637459debd918533163db2dcc29733")
    print(board_list)

    def create_board(self, name, default_lists = True):
        body = {
            'defaultLists': default_lists,
            'name': name,
            'token': self.token}
        cookie = {"tiken": self.token}
        path = "{trello}/boards/".format(trello = self.base_url)
        resp = requests.post(path, json=body, cookies=cookie)
        return resp.json()