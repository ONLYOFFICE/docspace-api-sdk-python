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

from docspace.models.sso_settings_v2_wrapper import SsoSettingsV2Wrapper

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
                response = docspace.models.sso_settings_v2.SsoSettingsV2(
                    last_modified = '2008-04-10T06:30+04:00', 
                    enable_sso = True, 
                    idp_settings = docspace.models.sso_idp_settings.SsoIdpSettings(
                        entity_id = 'some text', 
                        sso_url = 'some text', 
                        sso_binding = 'some text', 
                        slo_url = 'some text', 
                        slo_binding = 'some text', 
                        name_id_format = 'some text', ), 
                    idp_certificates = [
                        docspace.models.sso_certificate.SsoCertificate(
                            self_signed = True, 
                            crt = 'some text', 
                            key = 'some text', 
                            action = 'some text', 
                            domain_name = 'some text', 
                            start_date = '2008-04-10T06:30+04:00', 
                            expired_date = '2008-04-10T06:30+04:00', )
                        ], 
                    idp_certificate_advanced = docspace.models.sso_idp_certificate_advanced.SsoIdpCertificateAdvanced(
                        verify_algorithm = 'some text', 
                        verify_auth_responses_sign = True, 
                        verify_logout_requests_sign = True, 
                        verify_logout_responses_sign = True, 
                        decrypt_algorithm = 'some text', 
                        decrypt_assertions = True, ), 
                    sp_login_label = 'some text', 
                    sp_certificates = [
                        docspace.models.sso_certificate.SsoCertificate(
                            self_signed = True, 
                            crt = 'some text', 
                            key = 'some text', 
                            action = 'some text', 
                            domain_name = 'some text', 
                            start_date = '2008-04-10T06:30+04:00', 
                            expired_date = '2008-04-10T06:30+04:00', )
                        ], 
                    sp_certificate_advanced = docspace.models.sso_sp_certificate_advanced.SsoSpCertificateAdvanced(
                        signing_algorithm = 'some text', 
                        sign_auth_requests = True, 
                        sign_logout_requests = True, 
                        sign_logout_responses = True, 
                        encrypt_algorithm = 'some text', 
                        decrypt_algorithm = 'some text', 
                        encrypt_assertions = True, ), 
                    field_mapping = docspace.models.sso_field_mapping.SsoFieldMapping(
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
                    docspace.models.active_connections_wrapper_links_inner.ActiveConnectionsWrapper_links_inner(
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
