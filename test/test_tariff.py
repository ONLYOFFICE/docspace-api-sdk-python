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

from docspace-api-python.models.tariff import Tariff

class TestTariff(unittest.TestCase):
    """Tariff unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Tariff:
        """Test Tariff
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Tariff`
        """
        model = Tariff()
        if include_optional:
            return Tariff(
                id = 9846,
                state = 0,
                due_date = '2008-04-10T06:30+04:00',
                delay_due_date = '2008-04-10T06:30+04:00',
                license_date = '2008-04-10T06:30+04:00',
                customer_id = 'some text',
                quotas = [
                    docspace-api-python.models.quota.Quota(
                        id = 9846, 
                        quantity = 1234, 
                        wallet = True, 
                        due_date = '2008-04-10T06:30+04:00', 
                        next_quantity = 1234, 
                        state = 0, )
                    ],
                overdue_quotas = [
                    docspace-api-python.models.quota.Quota(
                        id = 9846, 
                        quantity = 1234, 
                        wallet = True, 
                        due_date = '2008-04-10T06:30+04:00', 
                        next_quantity = 1234, 
                        state = 0, )
                    ]
            )
        else:
            return Tariff(
        )
        """

    def testTariff(self):
        """Test Tariff"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
