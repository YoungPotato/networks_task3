from program import Program


class Handler:
    def __init__(self, token):
        self.inf = Program(token)

    def requests_handler(self, request, user_id):
        if request == 'friends':
            return self.inf.get_friends(user_id)
        if request == 'albums':
            return self.inf.get_albums(user_id)
        if request == 'name':
            return self.inf.get_name(user_id)
        if request == 'followers':
            return self.inf.get_followers(user_id)
        if request == 'videos':
            return self.inf.get_count_videos(user_id)
        if request == 'gifts':
            return self.inf.get_count_gifts(user_id)
