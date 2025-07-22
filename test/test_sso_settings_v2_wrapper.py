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

from docspace-api-sdk.models.sso_settings_v2_wrapper import SsoSettingsV2Wrapper

class TestSsoSettingsV2Wrapper(unittest.TestCase):
    """SsoSettingsV2Wrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SsoSettingsV2Wrapper:
        """Test SsoSettingsV2Wrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SsoSettingsV2Wrapper`
        """
        model = SsoSettingsV2Wrapper()
        if include_optional:
            return SsoSettingsV2Wrapper(
                response = docspace-api-sdk.models.sso_settings_v2.SsoSettingsV2(
                    last_modified = '2008-04-10T06:30+04:00', 
                    enable_sso = True, 
                    idp_settings = docspace-api-sdk.models.sso_idp_settings.SsoIdpSettings(
                        entity_id = 'some text', 
                        sso_url = 'some text', 
                        sso_binding = 'some text', 
                        slo_url = 'some text', 
                        slo_binding = 'some text', 
                        name_id_format = 'some text', ), 
                    idp_certificates = [
                        docspace-api-sdk.models.sso_certificate.SsoCertificate(
                            self_signed = True, 
                            crt = 'some text', 
                            key = 'some text', 
                            action = 'some text', 
                            domain_name = 'some text', 
                            start_date = '2008-04-10T06:30+04:00', 
                            expired_date = '2008-04-10T06:30+04:00', )
                        ], 
                    idp_certificate_advanced = docspace-api-sdk.models.sso_idp_certificate_advanced.SsoIdpCertificateAdvanced(
                        verify_algorithm = 'some text', 
                        verify_auth_responses_sign = True, 
                        verify_logout_requests_sign = True, 
                        verify_logout_responses_sign = True, 
                        decrypt_algorithm = 'some text', 
                        decrypt_assertions = True, ), 
                    sp_login_label = 'some text', 
                    sp_certificates = [
                        docspace-api-sdk.models.sso_certificate.SsoCertificate(
                            self_signed = True, 
                            crt = 'some text', 
                            key = 'some text', 
                            action = 'some text', 
                            domain_name = 'some text', 
                            start_date = '2008-04-10T06:30+04:00', 
                            expired_date = '2008-04-10T06:30+04:00', )
                        ], 
                    sp_certificate_advanced = docspace-api-sdk.models.sso_sp_certificate_advanced.SsoSpCertificateAdvanced(
                        signing_algorithm = 'some text', 
                        sign_auth_requests = True, 
                        sign_logout_requests = True, 
                        sign_logout_responses = True, 
                        encrypt_algorithm = 'some text', 
                        decrypt_algorithm = 'some text', 
                        encrypt_assertions = True, ), 
                    field_mapping = docspace-api-sdk.models.sso_field_mapping.SsoFieldMapping(
                        first_name = 'Winfield', 
                        last_name = 'Wyman', 
                        email = 'Sydney_Roberts4@hotmail.com', 
                        title = 'legacy_1080p_small_wooden_mouse', 
                        location = '001 Schroeder Run, New Tabithaport, Colombia', 
                        phone = 'some text', ), 
                    hide_auth_page = True, 
                    users_type = 1234, 
                    disable_email_verification = True, ),
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
            return SsoSettingsV2Wrapper(
        )
        """

    def testSsoSettingsV2Wrapper(self):
        """Test SsoSettingsV2Wrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
