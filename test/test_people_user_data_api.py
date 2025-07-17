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

from docspace-api-python.api.people_user_data_api import PeopleUserDataApi


class TestPeopleUserDataApi(unittest.TestCase):
    """PeopleUserDataApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PeopleUserDataApi()

    def tearDown(self) -> None:
        pass

    def test_get_delete_personal_folder_progress(self) -> None:
        """Test case for get_delete_personal_folder_progress

        Get the progress of deleting the personal folder
        """
        pass

    def test_get_reassign_progress(self) -> None:
        """Test case for get_reassign_progress

        Get the reassignment progress
        """
        pass

    def test_get_remove_progress(self) -> None:
        """Test case for get_remove_progress

        Get the deletion progress
        """
        pass

    def test_necessary_reassign(self) -> None:
        """Test case for necessary_reassign

        Check the data reassignment need
        """
        pass

    def test_send_instructions_to_delete(self) -> None:
        """Test case for send_instructions_to_delete

        Send the deletion instructions
        """
        pass

    def test_start_delete_personal_folder(self) -> None:
        """Test case for start_delete_personal_folder

        Delete the personal folder
        """
        pass

    def test_start_reassign(self) -> None:
        """Test case for start_reassign

        Start the data reassignment
        """
        pass

    def test_start_remove(self) -> None:
        """Test case for start_remove

        Start the data deletion
        """
        pass

    def test_terminate_reassign(self) -> None:
        """Test case for terminate_reassign

        Terminate the data reassignment
        """
        pass

    def test_terminate_remove(self) -> None:
        """Test case for terminate_remove

        Terminate the data deletion
        """
        pass


if __name__ == '__main__':
    unittest.main()
