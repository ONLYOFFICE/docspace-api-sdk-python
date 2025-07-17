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

from docspace-api-python.api.people_photos_api import PeoplePhotosApi


class TestPeoplePhotosApi(unittest.TestCase):
    """PeoplePhotosApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PeoplePhotosApi()

    def tearDown(self) -> None:
        pass

    def test_create_member_photo_thumbnails(self) -> None:
        """Test case for create_member_photo_thumbnails

        Create photo thumbnails
        """
        pass

    def test_delete_member_photo(self) -> None:
        """Test case for delete_member_photo

        Delete a user photo
        """
        pass

    def test_get_member_photo(self) -> None:
        """Test case for get_member_photo

        Get a user photo
        """
        pass

    def test_update_member_photo(self) -> None:
        """Test case for update_member_photo

        Update a user photo
        """
        pass

    def test_upload_member_photo(self) -> None:
        """Test case for upload_member_photo

        Upload a user photo
        """
        pass


if __name__ == '__main__':
    unittest.main()
