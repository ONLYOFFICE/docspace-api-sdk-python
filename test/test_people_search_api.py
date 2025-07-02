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

from docspace-api-python.api.people_search_api import PeopleSearchApi


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
