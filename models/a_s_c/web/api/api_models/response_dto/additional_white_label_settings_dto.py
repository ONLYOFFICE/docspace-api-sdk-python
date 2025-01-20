from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AdditionalWhiteLabelSettingsDto(Parsable):
    # URL to pay for the portal
    buy_url: Optional[str] = None
    # Specifies if feedback and support are available or not
    feedback_and_support_enabled: Optional[bool] = None
    # Feedback and support URL
    feedback_and_support_url: Optional[str] = None
    # Specifies if the help center is enabled or not
    help_center_enabled: Optional[bool] = None
    # Specifies if these settings are default or not
    is_default: Optional[bool] = None
    # Specifies if the license agreements are enabled or not
    license_agreements_enabled: Optional[bool] = None
    # License agreements URL
    license_agreements_url: Optional[str] = None
    # Sales email
    sales_email: Optional[str] = None
    # Specifies if the start document is enabled or not
    start_docs_enabled: Optional[bool] = None
    # Specifies if the user forum is enabled or not
    user_forum_enabled: Optional[bool] = None
    # User forum URL
    user_forum_url: Optional[str] = None
    # Specifies if the video guides are enabled or not
    video_guides_enabled: Optional[bool] = None
    # Video guides URL
    video_guides_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AdditionalWhiteLabelSettingsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdditionalWhiteLabelSettingsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AdditionalWhiteLabelSettingsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "buyUrl": lambda n : setattr(self, 'buy_url', n.get_str_value()),
            "feedbackAndSupportEnabled": lambda n : setattr(self, 'feedback_and_support_enabled', n.get_bool_value()),
            "feedbackAndSupportUrl": lambda n : setattr(self, 'feedback_and_support_url', n.get_str_value()),
            "helpCenterEnabled": lambda n : setattr(self, 'help_center_enabled', n.get_bool_value()),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "licenseAgreementsEnabled": lambda n : setattr(self, 'license_agreements_enabled', n.get_bool_value()),
            "licenseAgreementsUrl": lambda n : setattr(self, 'license_agreements_url', n.get_str_value()),
            "salesEmail": lambda n : setattr(self, 'sales_email', n.get_str_value()),
            "startDocsEnabled": lambda n : setattr(self, 'start_docs_enabled', n.get_bool_value()),
            "userForumEnabled": lambda n : setattr(self, 'user_forum_enabled', n.get_bool_value()),
            "userForumUrl": lambda n : setattr(self, 'user_forum_url', n.get_str_value()),
            "videoGuidesEnabled": lambda n : setattr(self, 'video_guides_enabled', n.get_bool_value()),
            "videoGuidesUrl": lambda n : setattr(self, 'video_guides_url', n.get_str_value()),
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
        writer.write_str_value("buyUrl", self.buy_url)
        writer.write_bool_value("feedbackAndSupportEnabled", self.feedback_and_support_enabled)
        writer.write_str_value("feedbackAndSupportUrl", self.feedback_and_support_url)
        writer.write_bool_value("helpCenterEnabled", self.help_center_enabled)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("licenseAgreementsEnabled", self.license_agreements_enabled)
        writer.write_str_value("licenseAgreementsUrl", self.license_agreements_url)
        writer.write_str_value("salesEmail", self.sales_email)
        writer.write_bool_value("startDocsEnabled", self.start_docs_enabled)
        writer.write_bool_value("userForumEnabled", self.user_forum_enabled)
        writer.write_str_value("userForumUrl", self.user_forum_url)
        writer.write_bool_value("videoGuidesEnabled", self.video_guides_enabled)
        writer.write_str_value("videoGuidesUrl", self.video_guides_url)
    

