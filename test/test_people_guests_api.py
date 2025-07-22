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

from docspace-api-sdk.api.people_guests_api import PeopleGuestsApi


class TestPeopleGuestsApi(unittest.TestCase):
    """PeopleGuestsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PeopleGuestsApi()

    def tearDown(self) -> None:
        pass

    def test_approve_guest_share_link(self) -> None:
        """Test case for approve_guest_share_link

        Approve a guest sharing link
        """
        pass

    def test_delete_guests(self) -> None:
        """Test case for delete_guests

        Delete guests
        """
        pass


if __name__ == '__main__':
    unittest.main()
