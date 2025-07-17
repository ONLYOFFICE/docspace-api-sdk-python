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

from docspace-api-python.api.files_quota_api import FilesQuotaApi


class TestFilesQuotaApi(unittest.TestCase):
    """FilesQuotaApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FilesQuotaApi()

    def tearDown(self) -> None:
        pass

    def test_reset_room_quota(self) -> None:
        """Test case for reset_room_quota

        Reset the room quota limit
        """
        pass

    def test_update_rooms_quota(self) -> None:
        """Test case for update_rooms_quota

        Change the room quota limit
        """
        pass


if __name__ == '__main__':
    unittest.main()
