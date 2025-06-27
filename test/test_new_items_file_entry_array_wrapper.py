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

from docspace.models.new_items_file_entry_array_wrapper import NewItemsFileEntryArrayWrapper

class TestNewItemsFileEntryArrayWrapper(unittest.TestCase):
    """NewItemsFileEntryArrayWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewItemsFileEntryArrayWrapper:
        """Test NewItemsFileEntryArrayWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewItemsFileEntryArrayWrapper`
        """
        model = NewItemsFileEntryArrayWrapper()
        if include_optional:
            return NewItemsFileEntryArrayWrapper(
                response = [
                    docspace.models.new_items_dto_file_entry_dto.NewItemsDtoFileEntryDto(
                        date = docspace.models.api_date_time.ApiDateTime(
                            utc_time = '2008-04-10T06:30+04:00', 
                            time_zone_offset = '00:00:00', ), 
                        items = [
                            docspace.models.file_entry_dto.FileEntryDto(
                                title = 'Some titile.txt/ Some title', 
                                access = 0, 
                                shared = False, 
                                created = docspace.models.api_date_time.ApiDateTime(
                                    utc_time = '2008-04-10T06:30+04:00', 
                                    time_zone_offset = '00:00:00', ), 
                                created_by = docspace.models.employee_dto.EmployeeDto(
                                    id = '', 
                                    display_name = 'Mike Zanyatski', 
                                    title = 'Manager', 
                                    avatar = 'some text', 
                                    avatar_original = 'some text', 
                                    avatar_max = 'some text', 
                                    avatar_medium = 'some text', 
                                    avatar_small = 'url to small avatar', 
                                    profile_url = 'some text', 
                                    has_avatar = True, 
                                    is_anonim = True, ), 
                                updated = , 
                                auto_delete = , 
                                root_folder_type = 0, 
                                parent_room_type = 0, 
                                updated_by = docspace.models.employee_dto.EmployeeDto(
                                    id = '', 
                                    display_name = 'Mike Zanyatski', 
                                    title = 'Manager', 
                                    avatar = 'some text', 
                                    avatar_original = 'some text', 
                                    avatar_max = 'some text', 
                                    avatar_medium = 'some text', 
                                    avatar_small = 'url to small avatar', 
                                    profile_url = 'some text', 
                                    has_avatar = True, 
                                    is_anonim = True, ), 
                                provider_item = True, 
                                provider_key = 'some text', 
                                provider_id = 1234, 
                                order = 'some text', 
                                file_entry_type = 1, )
                            ], )
                    ],
                count = 56,
                links = [
                    docspace.models.active_connections_wrapper_links_inner.ActiveConnectionsWrapper_links_inner(
                        href = '', 
                        action = '', )
                    ],
                status = 56,
                status_code = 56
            )
        else:
            return NewItemsFileEntryArrayWrapper(
        )
        """

    def testNewItemsFileEntryArrayWrapper(self):
        """Test NewItemsFileEntryArrayWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
