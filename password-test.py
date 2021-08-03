import unittest
from passwd import User
from passwd import Credential

class TestUser(unittest.TestCase):
    def setUp(self):
       
       self.new_user = User("Jerry", 12345678)

    def tearDown(self):
            User.user_list = []

    def test__init_(self):

        self.assertEqual(self.new_user.user_name,"Jerry")
        self.assertEqual(self.new_user.password,12345678)

    def test_save_user(self):

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_many_user(self):

        self.new_user.save_user()
        test_user = User("Kygo",7989790)
        test_user.save_user()

        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):

        self.new_user.save_user()
        test_user = User("Kygo",7989790)
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_display_user(self):

        self.assertEqual(User.display_user(),User.user_list)

class TestCredential(unittest.TestCase):
    def setUp(self):

        self.new_credential = Credential("Facebook","Skyles",45677)

    def test__init__(self):

        self.assertEqual(self.new_credential.site,"Facebook")
        self.assertEqual(self.new_credential.username,"Skyles")
        self.assertEqual(self.new_credential.password,45677)
    
    def test_save_credential(self):

        self.new_credential.save_credentials()
        self.assertEqual(len(Credential.credential_list),1)

    def tearDown(self):

        Credential.credential_list = []

    def test_save_multiple_user_accounts(self):

        self.new_credential.save_credentials()
        test_credential = Credential("Instagram","Jerry",3454546)
        test_credential.save_credentials()

        self.assertEqual(len(Credential.credential_list),2)

    def test_display_credential(self):

        self.assertEqual(Credential.display_credential(),Credential.credential_list)

    
            
        
          
          
          
          
          
          
          
if __name__ == "__main__":
    unittest.main()