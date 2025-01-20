from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .....api.core.api_date_time import ApiDateTime

@dataclass
class AuditEventDto(Parsable):
    # Action
    action: Optional[str] = None
    # [1000 - Login success, 1001 - Login success via social account, 1002 - Login fail invalid combination, 1003 - Login fail social account not found, 1004 - Login fail disabled profile, 1005 - Login fail, 1006 - Logout, 1007 - Login success via sms, 1008 - Login fail via sms, 1009 - Login fail ip security, 1010 - Login success via api, 1011 - Login success via social app, 1012 - Login success via api sms, 1013 - Login fail via api, 1014 - Login fail via api sms, 1015 - Login success via SSO, 1016 - Session started, 1017 - Session completed, 1018 - Login fail via SSO, 1019 - Login success via api social account, 1020 - Login fail via api social account, 1021 - Login succes via tfa app, 1022 - Login fail via Tfa app, 1023 - Login fail brute force, 1024 - Login success via api tfa, 1025 - Login fail via api tfa, 1026 - Login fail recaptcha, 4000 - User created, 4001 - Guest created, 4002 - User created via invite, 4003 - Guest created via invite, 4004 - User activated, 4005 - Guest activated, 4006 - User updated, 4007 - User updated language, 4008 - User added avatar, 4009 - User deleted avatar, 4010 - User updated avatar thumbnails, 4011 - User linked social account, 4012 - User unlinked social account, 4013 - User sent activation instructions, 4014 - User sent email change instructions, 4015 - User sent password change instructions, 4016 - User sent delete instructions, 4017 - User updated password, 4018 - User deleted, 4019 - Users updated type, 4020 - Users updated status, 4021 - Users sent activation instructions, 4022 - Users deleted, 4023 - Sent invite instructions, 4024 - User imported, 4025 - Guest imported, 4026 - Group created, 4027 - Group updated, 4028 - Group deleted, 4029 - User updated mobile number, 4030 - User data reassigns, 4031 - User data removing, 4032 - User connected tfa app, 4033 - User disconnected tfa app, 4034 - User logout active connections, 4035 - User logout active connection, 4036 - User logout active connections for user, 4037 - Send join invite, 5000 - File created, 5001 - File renamed, 5002 - File updated, 5003 - File created version, 5004 - File deleted version, 5005 - File updated revision comment, 5006 - File locked, 5007 - File unlocked, 5008 - File updated access, 5009 - File downloaded, 5010 - File downloaded as, 5011 - File uploaded, 5012 - File imported, 5013 - File copied, 5014 - File copied with overwriting, 5015 - File moved, 5016 - File moved with overwriting, 5017 - File moved to trash, 5018 - File deleted, 5019 - Folder created, 5020 - Folder renamed, 5021 - Folder updated access, 5022 - Folder copied, 5023 - Folder copied with overwriting, 5024 - Folder moved, 5025 - Folder moved with overwriting, 5026 - Folder moved to trash, 5027 - Folder deleted, 5028 - ThirdParty created, 5029 - ThirdParty updated, 5030 - ThirdParty deleted, 5031 - Documents ThirdParty settings updated, 5032 - Documents overwriting settings updated, 5033 - Documents uploading formats settings updated, 5034 - User file updated, 5035 - File converted, 5036 - File send access link, 5037 - Document service location setting, 5038 - Authorization keys setting, 5039 - Full text search setting, 5040 - Start transfer setting, 5041 - Start backup setting, 5042 - License key uploaded, 5043 - File change owner, 5044 - File restore version, 5045 - Document send to sign, 5046 - Document sign complete, 5047 - User updated email, 5048 - Documents store forcesave, 5049 - Documents forcesave, 5050 - Start storage encryption, 5051 - Privacy room enable, 5052 - Privacy room disable, 5053 - Start storage decryption, 5054 - File opened for change, 5055 - File marked as favorite, 5056 - File removed from favorite, 5057 - Folder downloaded, 5058 - File removed from list, 5059 - Folder removed from list, 5060 - File external link access updated, 5061 - Trash emptied, 5062 - File revision downloaded, 5063 - File marked as read, 5064 - File readed, 5065 - Folder marked as read, 5066 - Folder updated access for, 5068 - File updated access for, 5069 - Documents external share settings updated, 5070 - Room created, 5071 - Room renamed, 5072 - Room archived, 5073 - Room unarchived, 5074 - Room deleted, 5075 - Room update access for user, 5076 - Tag created, 5077 - Tags deleted, 5078 - Added room tags, 5079 - Deleted room tags, 5080 - Room logo created, 5081 - Room logo deleted, 5082 - Room invitation link updated, 5083 - Documents keep new file name settings updated, 5084 - Room remove user, 5085 - Room create user, 5086 - Room invitation link created, 5087 - Room invitation link deleted, 5088 - Room external link created, 5089 - Room external link updated, 5090 - Room external link deleted, 5091 - File external link created, 5092 - File external link updated, 5093 - File external link deleted, 5094 - Room group added, 5095 - Room update access for group, 5096 - Room group remove, 5097 - Room external link revoked, 5098 - Room external link renamed, 5099 - File uploaded with overwriting, 5100 - Room copied, 5101 - Documents display file extension updated, 5102 - Room color changed, 5103 - Room cover changed, 5104 - Room indexing changed, 5105 - Room deny download changed, 5106 - Room index export saved, 5107 - Folder index changed, 5108 - Folder index reordered, 5109 - Room deny download enabled, 5110 - Room deny download disabled, 5111 - File index changed, 5112 - Room watermark set, 5113 - Room watermark disabled, 5114 - Room index export saved, 5115 - Room indexing disabled, 5116 - Room life time set, 5117 - Room life time disabled, 5118 - Room invite resend, 6000 - Language settings updated, 6001 - Time zone settings updated, 6002 - Dns settings updated, 6003 - Trusted mail domain settings updated, 6004 - Password strength settings updated, 6005 - Two factor authentication settings updated, 6006 - Administrator message settings updated, 6007 - Default start page settings updated, 6008 - Products list updated, 6009 - Administrator added, 6010 - Administrator opened full access, 6011 - Administrator deleted, 6012 - Users opened product access, 6013 - Groups opened product access, 6014 - Product access opened, 6015 - Product access restricted, 6016 - Product added administrator, 6017 - Product deleted administrator, 6018 - Greeting settings updated, 6019 - Team template changed, 6020 - Color theme changed, 6021 - Owner sent change owner instructions, 6022 - Owner updated, 6023 - Owner sent portal deactivation instructions, 6024 - Owner sent portal delete instructions, 6025 - Portal deactivated, 6026 - Portal deleted, 6027 - Login history report downloaded, 6028 - Audit trail report downloaded, 6029 - SSO enabled, 6030 - SSO disabled, 6031 - Portal access settings updated, 6032 - Cookie settings updated, 6033 - Mail service settings updated, 6034 - Custom navigation settings updated, 6035 - Audit settings updated, 6036 - Two factor authentication disabled, 6037 - Two factor authentication enabled by sms, 6038 - Two factor authentication enabled by tfa app, 6039 - Portal renamed, 6040 - Quota per room changed, 6041 - Quota per room disabled, 6042 - Quota per user changed, 6043 - Quota per user disabled, 6044 - Quota per portal changed, 6045 - Quota per portal disabled, 6046 - Form submit, 6047 - Form opened for filling, 6048 - Custom quota per room default, 6049 - Custom quota per room changed, 6050 - Custom quota per room disabled, 6051 - Custom quota per user default, 6052 - Custom quota per user changed, 6053 - Custom quota per user disabled, 7000 - Contact admin mail sent, 7001 - Room invite link used, 7002 - User created and added to room, 7003 - Guest created and added to room, 7004 - Contact sales mail sent, 9901 - Create client, 9902 - Update client, 9903 - Regenerate secret, 9904 - Delete client, 9905 - Change client activation, 9906 - Change client visibility, 9907 - Revoke user client, 9908 - Generate authorization code token, 9909 - Generate personal access token, -1 - None]
    action_id: Optional[int] = None
    # [0 - None, 1 - Create, 2 - Update, 3 - Delete, 4 - Link, 5 - Unlink, 6 - Attach, 7 - Detach, 8 - Send, 9 - Import, 10 - Export, 11 - Update access, 12 - Download, 13 - Upload, 14 - Copy, 15 - Move, 16 - Reassigns, 17 - Follow, 18 - Unfollow, 19 - Logout]
    action_type: Optional[int] = None
    # Browser
    browser: Optional[str] = None
    # City
    city: Optional[str] = None
    # Context
    context: Optional[str] = None
    # Country
    country: Optional[str] = None
    # The date property
    date: Optional[ApiDateTime] = None
    # List of entry types
    entries: Optional[List[int]] = None
    # ID
    id: Optional[int] = None
    # IP
    ip: Optional[str] = None
    # [0 - None, 1 - Files, 2 - Folders, 3 - Documents settings, 4 - Companies, 5 - Persons, 6 - Contacts, 7 - Crm tasks, 8 - Opportunities, 9 - Invoices, 10 - Cases, 11 - Common crm settings, 12 - Contacts settings, 13 - Contact types, 14 - Invoice settings, 15 - Other crm settings, 16 - Users, 17 - Groups, 18 - Projects, 19 - Milestones, 20 - Tasks, 21 - Discussions, 22 - Time tracking, 23 - Reports, 24 - Projects settings, 25 - General, 26 - Products, 27 - Rooms, 28 - OAuth]
    module: Optional[int] = None
    # Page
    page: Optional[str] = None
    # Platform
    platform: Optional[str] = None
    # [0 - None, 2 - Documents, 3 - Login, 4 - Others, 5 - People, 7 - Settings]
    product: Optional[int] = None
    # List of targets
    target: Optional[List[str]] = None
    # User
    user: Optional[str] = None
    # User ID
    user_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuditEventDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditEventDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuditEventDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....api.core.api_date_time import ApiDateTime

        from .....api.core.api_date_time import ApiDateTime

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_str_value()),
            "actionId": lambda n : setattr(self, 'action_id', n.get_int_value()),
            "actionType": lambda n : setattr(self, 'action_type', n.get_int_value()),
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "context": lambda n : setattr(self, 'context', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "date": lambda n : setattr(self, 'date', n.get_object_value(ApiDateTime)),
            "entries": lambda n : setattr(self, 'entries', n.get_collection_of_primitive_values(int)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "ip": lambda n : setattr(self, 'ip', n.get_str_value()),
            "module": lambda n : setattr(self, 'module', n.get_int_value()),
            "page": lambda n : setattr(self, 'page', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_str_value()),
            "product": lambda n : setattr(self, 'product', n.get_int_value()),
            "target": lambda n : setattr(self, 'target', n.get_collection_of_primitive_values(str)),
            "user": lambda n : setattr(self, 'user', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_uuid_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from .....api.core.api_date_time import ApiDateTime

        writer.write_str_value("action", self.action)
        writer.write_int_value("actionId", self.action_id)
        writer.write_int_value("actionType", self.action_type)
        writer.write_str_value("browser", self.browser)
        writer.write_str_value("city", self.city)
        writer.write_str_value("context", self.context)
        writer.write_str_value("country", self.country)
        writer.write_object_value("date", self.date)
        writer.write_collection_of_primitive_values("entries", self.entries)
        writer.write_int_value("id", self.id)
        writer.write_str_value("ip", self.ip)
        writer.write_int_value("module", self.module)
        writer.write_str_value("page", self.page)
        writer.write_str_value("platform", self.platform)
        writer.write_int_value("product", self.product)
        writer.write_collection_of_primitive_values("target", self.target)
        writer.write_str_value("user", self.user)
        writer.write_uuid_value("userId", self.user_id)
    

