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

from docspace-api-sdk.api.group_api import GroupApi


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GroupApi()

    def tearDown(self) -> None:
        pass

    def test_add_group(self) -> None:
        """Test case for add_group

        Add a new group
        """
        pass

    def test_add_members_to(self) -> None:
        """Test case for add_members_to

        Add group members
        """
        pass

    def test_delete_group(self) -> None:
        """Test case for delete_group

        Delete a group
        """
        pass

    def test_get_group(self) -> None:
        """Test case for get_group

        Get a group
        """
        pass

    def test_get_group_by_user_id(self) -> None:
        """Test case for get_group_by_user_id

        Get user groups
        """
        pass

    def test_get_groups(self) -> None:
        """Test case for get_groups

        Get groups
        """
        pass

    def test_move_members_to(self) -> None:
        """Test case for move_members_to

        Move group members
        """
        pass

    def test_remove_members_from(self) -> None:
        """Test case for remove_members_from

        Remove group members
        """
        pass

    def test_set_group_manager(self) -> None:
        """Test case for set_group_manager

        Set a group manager
        """
        pass

    def test_set_members_to(self) -> None:
        """Test case for set_members_to

        Replace group members
        """
        pass

    def test_update_group(self) -> None:
        """Test case for update_group

        Update a group
        """
        pass


if __name__ == '__main__':
    unittest.main()
