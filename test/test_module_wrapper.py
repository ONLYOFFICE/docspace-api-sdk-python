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

from docspace-api-python.models.module_wrapper import ModuleWrapper

class TestModuleWrapper(unittest.TestCase):
    """ModuleWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModuleWrapper:
        """Test ModuleWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModuleWrapper`
        """
        model = ModuleWrapper()
        if include_optional:
            return ModuleWrapper(
                response = docspace-api-python.models.module.Module(
                    id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28', 
                    app_name = 'some text', 
                    title = 'legacy_1080p_small_wooden_mouse', 
                    link = 'some text', 
                    icon_url = 'some text', 
                    image_url = 'some text', 
                    help_url = 'some text', 
                    description = 'some text', 
                    is_primary = True, ),
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
            return ModuleWrapper(
        )
        """

    def testModuleWrapper(self):
        """Test ModuleWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
