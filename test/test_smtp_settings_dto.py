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

from docspace-api-sdk.models.smtp_settings_dto import SmtpSettingsDto

class TestSmtpSettingsDto(unittest.TestCase):
    """SmtpSettingsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SmtpSettingsDto:
        """Test SmtpSettingsDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SmtpSettingsDto`
        """
        model = SmtpSettingsDto()
        if include_optional:
            return SmtpSettingsDto(
                host = 'mail.example.com',
                port = 25,
                sender_address = 'notify@example.com',
                sender_display_name = 'Postman',
                credentials_user_name = 'notify@example.com',
                credentials_user_password = '{password}',
                enable_ssl = False,
                enable_auth = True,
                use_ntlm = False,
                is_default_settings = False
            )
        else:
            return SmtpSettingsDto(
        )
        """

    def testSmtpSettingsDto(self):
        """Test SmtpSettingsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
