from notion.client import NotionClient
import notion.collection


class NotionAutomation:

    def __init__(self, _user_url, _database_url):
        """
        initiates a new object holding the user info and the specific database
        :param _user_url: user's info
        :param _database_url: database
        """
        self.client = NotionClient(token_v2=_user_url)
        self.collection = self.client.get_collection(_database_url).collection
        print(type(self.collection))

    def add_row(self, content):
        new_row = self.collection.add_row()
        new_row.Task = content


