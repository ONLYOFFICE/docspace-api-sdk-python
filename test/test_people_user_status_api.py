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

from docspace-api-python.api.people_user_status_api import PeopleUserStatusApi


class TestPeopleUserStatusApi(unittest.TestCase):
    """PeopleUserStatusApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PeopleUserStatusApi()

    def tearDown(self) -> None:
        pass

    def test_get_by_status(self) -> None:
        """Test case for get_by_status

        Get profiles by status
        """
        pass

    def test_update_user_activation_status(self) -> None:
        """Test case for update_user_activation_status

        Set an activation status to the users
        """
        pass

    def test_update_user_status(self) -> None:
        """Test case for update_user_status

        Change a user status
        """
        pass


if __name__ == '__main__':
    unittest.main()
