from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class UserInfo(Parsable):
    # [0 - Not activated, 1 - Activated, 2 - Pending, 4 - Auto generated]
    activation_status: Optional[int] = None
    # Birthday
    birth_date: Optional[datetime.datetime] = None
    # The checkActivation property
    check_activation: Optional[bool] = None
    # List of contacts in the string format
    contacts: Optional[str] = None
    # List of contacts
    contacts_list: Optional[List[str]] = None
    # Creation date
    create_date: Optional[datetime.datetime] = None
    # The createdBy property
    created_by: Optional[UUID] = None
    # Language
    culture_name: Optional[str] = None
    # Email
    email: Optional[str] = None
    # First name
    first_name: Optional[str] = None
    # ID
    id: Optional[UUID] = None
    # Spceifies if the user is active or not
    is_active: Optional[bool] = None
    # Last modified date
    last_modified: Optional[datetime.datetime] = None
    # Last name
    last_name: Optional[str] = None
    # LDAP user quota attribute
    ldap_qouta: Optional[int] = None
    # Location
    location: Optional[str] = None
    # Mobile phone
    mobile_phone: Optional[str] = None
    # [0 - Not activated, 1 - Activated]
    mobile_phone_activation_status: Optional[int] = None
    # Notes
    notes: Optional[str] = None
    # Specifies if the user account was removed or not
    removed: Optional[bool] = None
    # Sex (male or female)
    sex: Optional[bool] = None
    # LDAP user identificator
    sid: Optional[str] = None
    # The spam property
    spam: Optional[bool] = None
    # SSO SAML user identificator
    sso_name_id: Optional[str] = None
    # SSO SAML user session identificator
    sso_session_id: Optional[str] = None
    # [1 - Active, 2 - Terminated, 4 - Pending, 5 - Default, 7 - All]
    status: Optional[int] = None
    # Tenant ID
    tenant_id: Optional[int] = None
    # The date and time when the user account was terminated
    terminated_date: Optional[datetime.datetime] = None
    # Title
    title: Optional[str] = None
    # Username
    user_name: Optional[str] = None
    # Registration date
    work_from_date: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "activationStatus": lambda n : setattr(self, 'activation_status', n.get_int_value()),
            "birthDate": lambda n : setattr(self, 'birth_date', n.get_datetime_value()),
            "checkActivation": lambda n : setattr(self, 'check_activation', n.get_bool_value()),
            "contacts": lambda n : setattr(self, 'contacts', n.get_str_value()),
            "contactsList": lambda n : setattr(self, 'contacts_list', n.get_collection_of_primitive_values(str)),
            "createDate": lambda n : setattr(self, 'create_date', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_uuid_value()),
            "cultureName": lambda n : setattr(self, 'culture_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "lastModified": lambda n : setattr(self, 'last_modified', n.get_datetime_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "ldapQouta": lambda n : setattr(self, 'ldap_qouta', n.get_int_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "mobilePhone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "mobilePhoneActivationStatus": lambda n : setattr(self, 'mobile_phone_activation_status', n.get_int_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "removed": lambda n : setattr(self, 'removed', n.get_bool_value()),
            "sex": lambda n : setattr(self, 'sex', n.get_bool_value()),
            "sid": lambda n : setattr(self, 'sid', n.get_str_value()),
            "spam": lambda n : setattr(self, 'spam', n.get_bool_value()),
            "ssoNameId": lambda n : setattr(self, 'sso_name_id', n.get_str_value()),
            "ssoSessionId": lambda n : setattr(self, 'sso_session_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_int_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_int_value()),
            "terminatedDate": lambda n : setattr(self, 'terminated_date', n.get_datetime_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "workFromDate": lambda n : setattr(self, 'work_from_date', n.get_datetime_value()),
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
        writer.write_int_value("activationStatus", self.activation_status)
        writer.write_datetime_value("birthDate", self.birth_date)
        writer.write_str_value("contacts", self.contacts)
        writer.write_collection_of_primitive_values("contactsList", self.contacts_list)
        writer.write_datetime_value("createDate", self.create_date)
        writer.write_uuid_value("createdBy", self.created_by)
        writer.write_str_value("cultureName", self.culture_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_uuid_value("id", self.id)
        writer.write_datetime_value("lastModified", self.last_modified)
        writer.write_str_value("lastName", self.last_name)
        writer.write_int_value("ldapQouta", self.ldap_qouta)
        writer.write_str_value("location", self.location)
        writer.write_str_value("mobilePhone", self.mobile_phone)
        writer.write_int_value("mobilePhoneActivationStatus", self.mobile_phone_activation_status)
        writer.write_str_value("notes", self.notes)
        writer.write_bool_value("removed", self.removed)
        writer.write_bool_value("sex", self.sex)
        writer.write_str_value("sid", self.sid)
        writer.write_bool_value("spam", self.spam)
        writer.write_str_value("ssoNameId", self.sso_name_id)
        writer.write_str_value("ssoSessionId", self.sso_session_id)
        writer.write_int_value("status", self.status)
        writer.write_int_value("tenantId", self.tenant_id)
        writer.write_datetime_value("terminatedDate", self.terminated_date)
        writer.write_str_value("title", self.title)
        writer.write_str_value("userName", self.user_name)
        writer.write_datetime_value("workFromDate", self.work_from_date)
    

