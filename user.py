class User:
    '''
    Class that generates new instances of users
    '''
    def __init__(self,user_name,password):

        self.user_name = user_name
        self.password = password

    user_list = []

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)