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

from docspace-api-sdk.models.migration_status_wrapper import MigrationStatusWrapper

class TestMigrationStatusWrapper(unittest.TestCase):
    """MigrationStatusWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MigrationStatusWrapper:
        """Test MigrationStatusWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MigrationStatusWrapper`
        """
        model = MigrationStatusWrapper()
        if include_optional:
            return MigrationStatusWrapper(
                response = docspace-api-sdk.models.migration_status_dto.MigrationStatusDto(
                    progress = 1, 
                    error = 'some text', 
                    parse_result = docspace-api-sdk.models.migration_api_info.MigrationApiInfo(
                        migrator_name = 'some text', 
                        operation = 'some text', 
                        failed_archives = ["some text"], 
                        users = [
                            docspace-api-sdk.models.migrating_api_user.MigratingApiUser(
                                should_import = True, 
                                key = 'some text', 
                                email = 'Sydney_Roberts4@hotmail.com', 
                                display_name = 'some text', 
                                first_name = 'Winfield', 
                                last_name = 'Wyman', 
                                user_type = 0, 
                                migrating_files = docspace-api-sdk.models.migrating_api_files.MigratingApiFiles(
                                    folders_count = 1234, 
                                    files_count = 1234, 
                                    bytes_total = 1234, ), )
                            ], 
                        without_email_users = [
                            docspace-api-sdk.models.migrating_api_user.MigratingApiUser(
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
                            docspace-api-sdk.models.migrating_api_group.MigratingApiGroup(
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
                    is_completed = True, ),
                count = 56,
                links = [
                    docspace-api-sdk.models.active_connections_wrapper_links_inner.ActiveConnectionsWrapper_links_inner(
                        href = '', 
                        action = '', )
                    ],
                status = 56,
                status_code = 56
            )
        else:
            return MigrationStatusWrapper(
        )
        """

    def testMigrationStatusWrapper(self):
        """Test MigrationStatusWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
