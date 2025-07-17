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

from docspace-api-python.models.wizard_requests_dto import WizardRequestsDto

class TestWizardRequestsDto(unittest.TestCase):
    """WizardRequestsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WizardRequestsDto:
        """Test WizardRequestsDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WizardRequestsDto`
        """
        model = WizardRequestsDto()
        if include_optional:
            return WizardRequestsDto(
                email = 'Sydney_Roberts4@hotmail.com',
                password_hash = 'some text',
                lng = 'some text',
                time_zone = 'some text',
                ami_id = 'some text',
                subscribe_from_site = True
            )
        else:
            return WizardRequestsDto(
                email = 'Sydney_Roberts4@hotmail.com',
                password_hash = 'some text',
        )
        """

    def testWizardRequestsDto(self):
        """Test WizardRequestsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
