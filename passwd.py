class User:
    '''
    Class that generates new instances of users
    '''
    def __init__(self,user_name,password):

        self.user_name = user_name
        self.password = password

    user_list = []

    def save_user(self):
        '''
        function to save a new to our list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        function to delete an instance from the list
        '''
        User.user_list.remove(self)

    @classmethod
    def display_user(cls):
        return cls.user_list


class Credential:
    '''
    class that generate new instances of user

    '''
    def __init__( self,site,username,password):

        self.site = site
        self.username = username
        self.password = password
    
    credential_list = []

    def save_credentials(self):

        Credential.credential_list.append(self)

    def delete_credential(self):
        
        Credential.credential_list.remove(self)    
