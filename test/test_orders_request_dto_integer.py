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

from docspace-api-sdk.models.orders_request_dto_integer import OrdersRequestDtoInteger

class TestOrdersRequestDtoInteger(unittest.TestCase):
    """OrdersRequestDtoInteger unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrdersRequestDtoInteger:
        """Test OrdersRequestDtoInteger
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrdersRequestDtoInteger`
        """
        model = OrdersRequestDtoInteger()
        if include_optional:
            return OrdersRequestDtoInteger(
                items = [
                    docspace-api-sdk.models.orders_item_request_dto_integer.OrdersItemRequestDtoInteger(
                        entry_id = 1234, 
                        entry_type = 1, 
                        order = 1234, )
                    ]
            )
        else:
            return OrdersRequestDtoInteger(
        )
        """

    def testOrdersRequestDtoInteger(self):
        """Test OrdersRequestDtoInteger"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
