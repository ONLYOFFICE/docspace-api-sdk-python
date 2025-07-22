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

from docspace-api-sdk.api.portal_users_api import PortalUsersApi


class TestPortalUsersApi(unittest.TestCase):
    """PortalUsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PortalUsersApi()

    def tearDown(self) -> None:
        pass

    def test_get_invitation_link(self) -> None:
        """Test case for get_invitation_link

        Get an invitation link
        """
        pass

    def test_get_portal_users_count(self) -> None:
        """Test case for get_portal_users_count

        Get a number of portal users
        """
        pass

    def test_get_user_by_id(self) -> None:
        """Test case for get_user_by_id

        Get a user by ID
        """
        pass

    def test_mark_gift_message_as_read(self) -> None:
        """Test case for mark_gift_message_as_read

        Mark a gift message as read
        """
        pass

    def test_send_congratulations(self) -> None:
        """Test case for send_congratulations

        Send congratulations
        """
        pass


if __name__ == '__main__':
    unittest.main()
