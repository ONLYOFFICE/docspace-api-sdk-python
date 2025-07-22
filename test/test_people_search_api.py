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

from docspace-api-sdk.api.people_search_api import PeopleSearchApi


class TestPeopleSearchApi(unittest.TestCase):
    """PeopleSearchApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PeopleSearchApi()

    def tearDown(self) -> None:
        pass

    def test_get_accounts_entries_with_shared(self) -> None:
        """Test case for get_accounts_entries_with_shared

        Get account entries
        """
        pass

    def test_get_search(self) -> None:
        """Test case for get_search

        Search users
        """
        pass

    def test_get_simple_by_filter(self) -> None:
        """Test case for get_simple_by_filter

        Search users by extended filter
        """
        pass

    def test_get_users_with_room_shared(self) -> None:
        """Test case for get_users_with_room_shared

        Get users with room sharing settings
        """
        pass

    def test_search_users_by_extended_filter(self) -> None:
        """Test case for search_users_by_extended_filter

        Search users with detaailed information by extended filter
        """
        pass

    def test_search_users_by_query(self) -> None:
        """Test case for search_users_by_query

        Search users (using query parameters)
        """
        pass

    def test_search_users_by_status(self) -> None:
        """Test case for search_users_by_status

        Search users by status filter
        """
        pass


if __name__ == '__main__':
    unittest.main()
