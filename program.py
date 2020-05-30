import requests
import time


class Program:
    def __init__(self, token):
        self.token = token

    def get_friends(self, user_id):
        js = self.get_response("friends.get", user_id)
        data = js["response"]
        friends = data["items"]
        res = "Количество друзей - {}\n".format(data["count"])
        for friend in friends:
            res += self.get_name(friend) + "\n"
            time.sleep(0.2)
        return res

    def get_albums(self, user_id):
        js = self.get_response("photos.getAlbums", user_id)
        res = js["response"]
        count = res["count"]
        albums = ""
        for item in res["items"]:
            albums += item["title"] + "\n"
        return "Количество альбомов - {}\n{}".format(count, albums)

    def get_name(self, user_id):
        js = self.get_response("users.get", user_id)
        data = js["response"][0]
        first_name = data["first_name"]
        last_name = data["last_name"]
        return "{} {}".format(first_name, last_name)

    def get_count_gifts(self, user_id):
        js = self.get_response("gifts.get", user_id)
        res = js["response"]
        count = res["count"]
        return "Количество подарков - {}".format(count)

    def get_followers(self, user_id):
        js = self.get_response("users.getFollowers", user_id)
        data = js["response"]
        followers = data["items"]
        res = "Количество подписчиков - {}\n".format(data["count"])
        for follower in followers:
            res += self.get_name(follower) + "\n"
            time.sleep(0.2)
        return res

    def get_count_videos(self, user_id):
        js = self.get_response("video.get", user_id)
        res = js["response"]
        count = res["count"]
        return "Количество видео - {}".format(count)

    def get_response(self, method, user_id):
        url = "https://api.vk.com/method/"
        a = requests.get(url + method + "?user_id={}".format(user_id)
                         + "&access_token={}".format(self.token) + "&v=5.107")
        return a.json()
