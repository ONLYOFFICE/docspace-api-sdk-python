#
# (c) Copyright Ascensio System SIA 2026
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



from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class OperationType(int, Enum):
    """
    [0 - Any, 1 - Unknown, 2 - ServicePayment, 4 - PackagePayment, 8 - ServiceUsage, 16 - Deposit, 32 - ReceiveProviderInvoice, 64 - ProcessProviderInvoice, 128 - WriteOffServiceProfit, 256 - Profit, 512 - PartnerAccrual, 1024 - ProviderPayment, 2048 - PartnerPayment, 4096 - Refund, 8192 - BankDeposit, 16384 - BankWithdrawal, 32768 - GoodwillCredit, 65536 - WriteOffProfit, 131072 - WriteOffDifferenceCurrency]
    """

    """
    allowed enum values
    """
    Any = 0
    Unknown = 1
    ServicePayment = 2
    PackagePayment = 4
    ServiceUsage = 8
    Deposit = 16
    ReceiveProviderInvoice = 32
    ProcessProviderInvoice = 64
    WriteOffServiceProfit = 128
    Profit = 256
    PartnerAccrual = 512
    ProviderPayment = 1024
    PartnerPayment = 2048
    Refund = 4096
    BankDeposit = 8192
    BankWithdrawal = 16384
    GoodwillCredit = 32768
    WriteOffProfit = 65536
    WriteOffDifferenceCurrency = 131072

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OperationType from a JSON string"""
        return cls(json.loads(json_str))

