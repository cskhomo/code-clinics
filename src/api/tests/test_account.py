from unittest.mock import patch, MagicMock, Mock, mock_open
from unittest import TestCase, main
from src.api.account import *
from os import environ
from json import dumps, load

class TestLogin(TestCase):
    """Tests for the login function."""

    def setUpMocks(self, mock_build, mock_credentials, mock_path_exists):
        """Sets up mocks for the login tests."""
        mock_path_exists.return_value = True
        mock_creds = MagicMock(valid=True)
        mock_creds.to_json.return_value = 'token_json'

        mock_credentials.from_authorized_user_file.return_value = mock_creds
        mock_service = MagicMock()

        mock_build.return_value = mock_service
        mock_service.calendarList().get().execute.return_value = {'id': 'user_id'}


    @patch('src.api.account.path.exists')
    @patch('src.api.account.Credentials')
    @patch('src.api.account.build')
    def test_login_service_student(self, mock_build, mock_credentials, mock_path_exists):
        """Tests login as a student."""

        self.setUpMocks(mock_build, mock_credentials, mock_path_exists)
        with patch.dict(environ, {'CREDENTIALS': 'credentials.json', 'IDENTITY': 'identity.json', 'TOKEN': 'token.json'}):
            service = login('student')
            self.assertIsNotNone(service)


    @patch('src.api.account.path.exists')
    @patch('src.api.account.Credentials')
    @patch('src.api.account.build')
    def test_login_service_volunteer(self, mock_build, mock_credentials, mock_path_exists):
        """Tests login as a volunteer."""

        self.setUpMocks(mock_build, mock_credentials, mock_path_exists)
        with patch.dict(environ, {'CREDENTIALS': 'credentials.json', 'IDENTITY': 'identity.json', 'TOKEN': 'token.json'}):
            service = login('volunteer')
            self.assertIsNotNone(service)


    @patch('src.api.account.path.exists')
    @patch('src.api.account.Credentials')
    @patch('src.api.account.build')
    def test_login_service_invalid_role(self, mock_build, mock_credentials, mock_path_exists):
        """Tests login with an invalid role."""

        self.setUpMocks(mock_build, mock_credentials, mock_path_exists)
        with patch.dict(environ, {'CREDENTIALS': 'credentials.json', 'IDENTITY': 'identity.json', 'TOKEN': 'token.json'}):
            with self.assertRaises(ValueError):
                login('guest')


class TestLogout(TestCase):
    """Tests for the logout function."""

    @patch('src.api.account.path.exists')
    @patch('src.api.account.unlink')
    def test_logout(self, mock_unlink, mock_path_exists):
        """Tests logout."""

        mock_path_exists.return_value = True
        with patch.dict(environ, {'TOKEN': 'token.json', 'IDENTITY': 'identity.json'}):
            logout()
            mock_unlink.assert_called()


class TestSecrets(TestCase):
    """Tests for the secrets functions."""

    def test_store_secrets(self):
        """Tests storing secrets."""

        mock_token = Mock()
        mock_token.to_json.return_value = '{"token": "abc-123"}'

        write_secrets('student', 'email', mock_token)
        self.assertTrue(path.exists(TOKEN))
        self.assertTrue(path.exists(IDENTITY))
        logout()
    
    def test_identity_contents(self):
        """Tests the contents of the identity file."""
        
        mock_token = Mock()
        mock_token.to_json.return_value = '{"token": "abc-123"}'

        write_secrets('student', 'email@test.py', mock_token)

        with open(IDENTITY, 'r') as file:
            identity = load(file)

        self.assertEqual(identity['role'], 'Student')
        self.assertEqual(identity['user'], 'email@test.py')
        logout()


class TestStatus(TestCase):
    """Tests for the status function."""

    @patch('src.api.account.path.exists')
    def test_logged_in_student(self, mock_path_exists):
        """Tests status when logged in as a student."""

        mock_path_exists.return_value = True
        with patch('builtins.open', mock_open(read_data=dumps({'role': 'Student'}))):
            with patch.dict(environ, {'IDENTITY': 'identity.json'}):
                self.assertEqual(status(), "✅ Logged in as Student")
    

    @patch('src.api.account.path.exists')
    def test_logged_in_volunteer(self, mock_path_exists):
        """Tests status when logged in as a volunteer."""

        mock_path_exists.return_value = True
        with patch('builtins.open', mock_open(read_data=dumps({'role': 'Volunteer'}))):
            with patch.dict(environ, {'IDENTITY': 'identity.json'}):
                self.assertEqual(status(), "✅ Logged in as Volunteer")


    @patch('src.api.account.path.exists')
    def test_logged_out(self, mock_path_exists):
        """Tests status when logged out."""

        mock_path_exists.return_value = False
        with patch.dict(environ, {'IDENTITY': 'identity.json'}):
            self.assertEqual(status(), "❌ Not logged in")


class TestRole(TestCase):
    """Tests for the role function."""

    @patch('src.api.account.path.exists')
    def test_role_student(self, mock_path_exists):
        """Tests role when logged in."""

        mock_path_exists.return_value = True
        with patch('builtins.open', mock_open(read_data=dumps({'role': 'Student'}))):
            with patch.dict(environ, {'IDENTITY': 'identity.json'}):
                self.assertEqual(role(), "Student")
    

    @patch('src.api.account.path.exists')
    def test_role_volunteer(self, mock_path_exists):
        """Tests role when logged in."""

        mock_path_exists.return_value = True
        with patch('builtins.open', mock_open(read_data=dumps({'role': 'Volunteer'}))):
            with patch.dict(environ, {'IDENTITY': 'identity.json'}):
                self.assertEqual(role(), "Volunteer")


    @patch('src.api.account.path.exists')
    def test_role_invalid(self, mock_path_exists):
        """Tests role when logged out."""

        mock_path_exists.return_value = False
        with patch.dict(environ, {'IDENTITY': 'identity.json'}):
            self.assertEqual(role(), "Unidentified User.")


if __name__ == '__main__':
    main()