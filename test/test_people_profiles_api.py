#
# (c) Copyright Ascensio System SIA 2025
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



import unittest

from docspace-api-python.api.people_profiles_api import PeopleProfilesApi


class TestPeopleProfilesApi(unittest.TestCase):
    """PeopleProfilesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PeopleProfilesApi()

    def tearDown(self) -> None:
        pass

    def test_add_member(self) -> None:
        """Test case for add_member

        Add a user
        """
        pass

    def test_delete_member(self) -> None:
        """Test case for delete_member

        Delete a user
        """
        pass

    def test_delete_profile(self) -> None:
        """Test case for delete_profile

        Delete my profile
        """
        pass

    def test_get_all_profiles(self) -> None:
        """Test case for get_all_profiles

        Get profiles
        """
        pass

    def test_get_claims(self) -> None:
        """Test case for get_claims

        Returns the user claims.
        """
        pass

    def test_get_profile_by_email(self) -> None:
        """Test case for get_profile_by_email

        Get a profile by user email
        """
        pass

    def test_get_profile_by_user_id(self) -> None:
        """Test case for get_profile_by_user_id

        Get a profile by user name
        """
        pass

    def test_get_self_profile(self) -> None:
        """Test case for get_self_profile

        Get my profile
        """
        pass

    def test_invite_users(self) -> None:
        """Test case for invite_users

        Invite users
        """
        pass

    def test_remove_users(self) -> None:
        """Test case for remove_users

        Delete users
        """
        pass

    def test_resend_user_invites(self) -> None:
        """Test case for resend_user_invites

        Resend activation emails
        """
        pass

    def test_send_email_change_instructions(self) -> None:
        """Test case for send_email_change_instructions

        Send instructions to change email
        """
        pass

    def test_update_member(self) -> None:
        """Test case for update_member

        Update a user
        """
        pass

    def test_update_member_culture(self) -> None:
        """Test case for update_member_culture

        Update a user culture code
        """
        pass


if __name__ == '__main__':
    unittest.main()
