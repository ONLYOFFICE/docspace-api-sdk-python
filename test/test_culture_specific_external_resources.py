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

from docspace-api-sdk.models.culture_specific_external_resources import CultureSpecificExternalResources

class TestCultureSpecificExternalResources(unittest.TestCase):
    """CultureSpecificExternalResources unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CultureSpecificExternalResources:
        """Test CultureSpecificExternalResources
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CultureSpecificExternalResources`
        """
        model = CultureSpecificExternalResources()
        if include_optional:
            return CultureSpecificExternalResources(
                api = docspace-api-sdk.models.culture_specific_external_resource.CultureSpecificExternalResource(
                    domain = 'some text', 
                    entries = [{"key":"some text","value":"some text"}], ),
                common = docspace-api-sdk.models.culture_specific_external_resource.CultureSpecificExternalResource(
                    domain = 'some text', 
                    entries = [{"key":"some text","value":"some text"}], ),
                forum = docspace-api-sdk.models.culture_specific_external_resource.CultureSpecificExternalResource(
                    domain = 'some text', 
                    entries = [{"key":"some text","value":"some text"}], ),
                helpcenter = docspace-api-sdk.models.culture_specific_external_resource.CultureSpecificExternalResource(
                    domain = 'some text', 
                    entries = [{"key":"some text","value":"some text"}], ),
                integrations = docspace-api-sdk.models.culture_specific_external_resource.CultureSpecificExternalResource(
                    domain = 'some text', 
                    entries = [{"key":"some text","value":"some text"}], ),
                site = docspace-api-sdk.models.culture_specific_external_resource.CultureSpecificExternalResource(
                    domain = 'some text', 
                    entries = [{"key":"some text","value":"some text"}], ),
                social_networks = docspace-api-sdk.models.culture_specific_external_resource.CultureSpecificExternalResource(
                    domain = 'some text', 
                    entries = [{"key":"some text","value":"some text"}], ),
                support = docspace-api-sdk.models.culture_specific_external_resource.CultureSpecificExternalResource(
                    domain = 'some text', 
                    entries = [{"key":"some text","value":"some text"}], ),
                videoguides = docspace-api-sdk.models.culture_specific_external_resource.CultureSpecificExternalResource(
                    domain = 'some text', 
                    entries = [{"key":"some text","value":"some text"}], )
            )
        else:
            return CultureSpecificExternalResources(
        )
        """

    def testCultureSpecificExternalResources(self):
        """Test CultureSpecificExternalResources"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
