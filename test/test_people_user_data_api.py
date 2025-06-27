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

from docspace.api.people_user_data_api import PeopleUserDataApi


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
