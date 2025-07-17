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

from docspace-api-python.api.people_password_api import PeoplePasswordApi


class TestPeoplePasswordApi(unittest.TestCase):
    """PeoplePasswordApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PeoplePasswordApi()

    def tearDown(self) -> None:
        pass

    def test_change_user_password(self) -> None:
        """Test case for change_user_password

        Change a user password
        """
        pass

    def test_send_user_password(self) -> None:
        """Test case for send_user_password

        Remind a user password
        """
        pass


if __name__ == '__main__':
    unittest.main()
