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

from docspace-api-python.models.cdn_storage_settings_wrapper import CdnStorageSettingsWrapper

class TestCdnStorageSettingsWrapper(unittest.TestCase):
    """CdnStorageSettingsWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CdnStorageSettingsWrapper:
        """Test CdnStorageSettingsWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CdnStorageSettingsWrapper`
        """
        model = CdnStorageSettingsWrapper()
        if include_optional:
            return CdnStorageSettingsWrapper(
                response = docspace-api-python.models.cdn_storage_settings.CdnStorageSettings(
                    module = 'some text', 
                    props = [{"key":"some text","value":"some text"}], 
                    last_modified = '2008-04-10T06:30+04:00', ),
                count = 56,
                links = [
                    docspace-api-python.models.active_connections_wrapper_links_inner.ActiveConnectionsWrapper_links_inner(
                        href = '', 
                        action = '', )
                    ],
                status = 56,
                status_code = 56
            )
        else:
            return CdnStorageSettingsWrapper(
        )
        """

    def testCdnStorageSettingsWrapper(self):
        """Test CdnStorageSettingsWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
