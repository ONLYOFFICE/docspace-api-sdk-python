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


class ConfirmType(str, Enum):
    """
    [EmpInvite - Emp invite, LinkInvite - Link invite, PortalSuspend - Portal suspend, PortalContinue - Portal continue, PortalRemove - Portal remove, DnsChange - Dns change, PortalOwnerChange - Portal owner change, Activation - Activation, EmailChange - Email change, EmailActivation - Email activation, PasswordChange - Password change, ProfileRemove - Profile remove, PhoneActivation - Phone activation, PhoneAuth - Phone auth, Auth - Auth, TfaActivation - Tfa activation, TfaAuth - Tfa auth, Wizard - Wizard, GuestShareLink - Guest share link]
    """

    """
    allowed enum values
    """
    EMPINVITE = 'EmpInvite'
    LINKINVITE = 'LinkInvite'
    PORTALSUSPEND = 'PortalSuspend'
    PORTALCONTINUE = 'PortalContinue'
    PORTALREMOVE = 'PortalRemove'
    DNSCHANGE = 'DnsChange'
    PORTALOWNERCHANGE = 'PortalOwnerChange'
    ACTIVATION = 'Activation'
    EMAILCHANGE = 'EmailChange'
    EMAILACTIVATION = 'EmailActivation'
    PASSWORDCHANGE = 'PasswordChange'
    PROFILEREMOVE = 'ProfileRemove'
    PHONEACTIVATION = 'PhoneActivation'
    PHONEAUTH = 'PhoneAuth'
    AUTH = 'Auth'
    TFAACTIVATION = 'TfaActivation'
    TFAAUTH = 'TfaAuth'
    WIZARD = 'Wizard'
    GUESTSHARELINK = 'GuestShareLink'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConfirmType from a JSON string"""
        return cls(json.loads(json_str))

