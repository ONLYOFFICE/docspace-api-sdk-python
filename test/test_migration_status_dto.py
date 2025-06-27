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

from docspace.models.migration_status_dto import MigrationStatusDto

class TestMigrationStatusDto(unittest.TestCase):
    """MigrationStatusDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MigrationStatusDto:
        """Test MigrationStatusDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MigrationStatusDto`
        """
        model = MigrationStatusDto()
        if include_optional:
            return MigrationStatusDto(
                progress = 1,
                error = 'some text',
                parse_result = docspace.models.migration_api_info.MigrationApiInfo(
                    migrator_name = 'some text', 
                    operation = 'some text', 
                    failed_archives = ["some text"], 
                    users = [
                        docspace.models.migrating_api_user.MigratingApiUser(
                            should_import = True, 
                            key = 'some text', 
                            email = 'Sydney_Roberts4@hotmail.com', 
                            display_name = 'some text', 
                            first_name = 'Winfield', 
                            last_name = 'Wyman', 
                            user_type = 0, 
                            migrating_files = docspace.models.migrating_api_files.MigratingApiFiles(
                                folders_count = 1234, 
                                files_count = 1234, 
                                bytes_total = 1234, ), )
                        ], 
                    without_email_users = [
                        docspace.models.migrating_api_user.MigratingApiUser(
                            should_import = True, 
                            key = 'some text', 
                            email = 'Sydney_Roberts4@hotmail.com', 
                            display_name = 'some text', 
                            first_name = 'Winfield', 
                            last_name = 'Wyman', )
                        ], 
                    exist_users = [
                        
                        ], 
                    groups = [
                        docspace.models.migrating_api_group.MigratingApiGroup(
                            should_import = True, 
                            group_name = 'some text', 
                            module_name = 'some text', 
                            user_uid_list = ["some text"], )
                        ], 
                    import_personal_files = True, 
                    import_shared_files = True, 
                    import_shared_folders = True, 
                    import_common_files = True, 
                    import_project_files = True, 
                    import_groups = True, 
                    successed_users = 1234, 
                    failed_users = 1234, 
                    files = ["some text"], 
                    errors = ["some text"], ),
                is_completed = True
            )
        else:
            return MigrationStatusDto(
        )
        """

    def testMigrationStatusDto(self):
        """Test MigrationStatusDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
