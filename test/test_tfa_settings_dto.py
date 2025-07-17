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

from docspace-api-python.models.tfa_settings_dto import TfaSettingsDto

class TestTfaSettingsDto(unittest.TestCase):
    """TfaSettingsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TfaSettingsDto:
        """Test TfaSettingsDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TfaSettingsDto`
        """
        model = TfaSettingsDto()
        if include_optional:
            return TfaSettingsDto(
                id = '9846',
                title = 'legacy_1080p_small_wooden_mouse',
                enabled = True,
                avaliable = True,
                trusted_ips = ["some text"],
                mandatory_users = ["75a5f745-f697-4418-b38d-0fe0d277e258"],
                mandatory_groups = ["75a5f745-f697-4418-b38d-0fe0d277e258"]
            )
        else:
            return TfaSettingsDto(
        )
        """

    def testTfaSettingsDto(self):
        """Test TfaSettingsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
