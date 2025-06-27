# (c) Copyright Ascensio System SIA 2009-2025
# 
# This program is a free software product.
# You can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License (AGPL) version 3 as published by the Free Software
# Foundation. In accordance with Section 7(a) of the GNU AGPL its Section 15 shall be amended
# to the effect that Ascensio System SIA expressly excludes the warranty of non-infringement of
# any third-party rights.
# 
# This program is distributed WITHOUT ANY WARRANTY, without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE. For details, see
# the GNU AGPL at: http://www.gnu.org/licenses/agpl-3.0.html
# 
# You can contact Ascensio System SIA at Lubanas st. 125a-25, Riga, Latvia, EU, LV-1021.
# 
# The  interactive user interfaces in modified source and object code versions of the Program must
# display Appropriate Legal Notices, as required under Section 5 of the GNU AGPL version 3.
# 
# Pursuant to Section 7(b) of the License you must retain the original Product logo when
# distributing the program. Pursuant to Section 7(e) we decline to grant you any rights under
# trademark law for use of our trademarks.
# 
# All the Product's GUI elements, including illustrations and icon sets, as well as technical writing
# content are licensed under the terms of the Creative Commons Attribution-ShareAlike 4.0
# International. See the License terms at http://creativecommons.org/licenses/by-sa/4.0/legalcode



import unittest

from docspace.api.people_profiles_api import PeopleProfilesApi


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
