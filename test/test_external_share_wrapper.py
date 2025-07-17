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

from docspace-api-python.models.external_share_wrapper import ExternalShareWrapper

class TestExternalShareWrapper(unittest.TestCase):
    """ExternalShareWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExternalShareWrapper:
        """Test ExternalShareWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExternalShareWrapper`
        """
        model = ExternalShareWrapper()
        if include_optional:
            return ExternalShareWrapper(
                response = docspace-api-python.models.external_share_dto.ExternalShareDto(
                    status = 0, 
                    id = '9846', 
                    title = 'legacy_1080p_small_wooden_mouse', 
                    tenant_id = 1234, 
                    entity_id = 'some text', 
                    entry_title = 'some text', 
                    shared = True, 
                    link_id = '75a5f745-f697-4418-b38d-0fe0d277e258', 
                    is_authenticated = True, ),
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
            return ExternalShareWrapper(
        )
        """

    def testExternalShareWrapper(self):
        """Test ExternalShareWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
