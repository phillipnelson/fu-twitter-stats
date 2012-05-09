import twitter2
from config.twitter import CREDENTIALS


class MyTwitterApi(twitter2.Api):
    def GetFriendIDs(self,user=None,cursor=None):
        try:
            return super(MyTwitterApi, self).GetFriendIDs(user=user,cursor=cursor)
        except twitter2.TwitterError as exc:
            if not 'Not authorized' in str(exc):
                self.rotateCredentials()
                return self.GetFriendIDs(user=user,cursor=cursor)
            else:
                raise exc
    
    def GetFollowerIDs(self,userid=None,cursor=None):
        try:
            return super(MyTwitterApi, self).GetFollowerIDs(userid=userid,cursor=cursor)
        except twitter2.TwitterError as exc:
            if not 'Not authorized' in str(exc):
                self.rotateCredentials()
                return self.GetFriendIDs(userid=userid,cursor=cursor)
            else:
                raise exc
            
    def GetUser(self,username):
        try:
            return super(MyTwitterApi, self).GetUser(username)
        except:
            self.rotateCredentials()
            return self.GetUser(username)
            
    def rotateCredentials(self):
        print "Rotating Credentials."
        self = MyTwitterApi(**CREDENTIALS.pop())


twitter_api = MyTwitterApi(**CREDENTIALS.pop())