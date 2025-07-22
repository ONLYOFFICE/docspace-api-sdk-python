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

from docspace-api-sdk.models.quota_array_wrapper import QuotaArrayWrapper

class TestQuotaArrayWrapper(unittest.TestCase):
    """QuotaArrayWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuotaArrayWrapper:
        """Test QuotaArrayWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuotaArrayWrapper`
        """
        model = QuotaArrayWrapper()
        if include_optional:
            return QuotaArrayWrapper(
                response = [
                    docspace-api-sdk.models.quota_dto.QuotaDto(
                        id = 9846, 
                        title = 'legacy_1080p_small_wooden_mouse', 
                        price = docspace-api-sdk.models.price_dto.PriceDto(
                            value = 10, 
                            currency_symbol = 'some text', 
                            iso_currency_symbol = 'some text', ), 
                        non_profit = True, 
                        free = True, 
                        trial = True, 
                        features = [
                            docspace-api-sdk.models.tenant_quota_feature_dto.TenantQuotaFeatureDto(
                                id = '9846', 
                                title = 'legacy_1080p_small_wooden_mouse', 
                                image = 'some text', 
                                value = {"int":1234,"string":"some text","boolean":true}, 
                                type = 'some text', 
                                used = docspace-api-sdk.models.feature_used_dto.FeatureUsedDto(
                                    value = {"int":1234,"string":"some text","boolean":true}, 
                                    title = 'legacy_1080p_small_wooden_mouse', ), 
                                price_title = 'some text', )
                            ], 
                        users_quota = docspace-api-sdk.models.tenant_entity_quota_settings.TenantEntityQuotaSettings(
                            enable_quota = True, 
                            default_quota = 1234, 
                            last_recalculate_date = '2008-04-10T06:30+04:00', ), 
                        rooms_quota = docspace-api-sdk.models.tenant_entity_quota_settings.TenantEntityQuotaSettings(
                            enable_quota = True, 
                            default_quota = 1234, 
                            last_recalculate_date = '2008-04-10T06:30+04:00', ), 
                        tenant_custom_quota = docspace-api-sdk.models.tenant_quota_settings.TenantQuotaSettings(
                            enable_quota = True, 
                            quota = 1234, 
                            last_recalculate_date = '2008-04-10T06:30+04:00', 
                            last_modified = '2008-04-10T06:30+04:00', ), 
                        due_date = '2008-04-10T06:30+04:00', )
                    ],
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
            return QuotaArrayWrapper(
        )
        """

    def testQuotaArrayWrapper(self):
        """Test QuotaArrayWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
