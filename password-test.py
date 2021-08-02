import unittest
from user import User

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

if __name__ == '__main__':
    unittest.main()