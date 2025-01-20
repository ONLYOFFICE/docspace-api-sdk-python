from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.success_api_response_of_a_s_c.web.api.api_model.response_dto.settings_dto import SettingsDto
    from .authservice.authservice_request_builder import AuthserviceRequestBuilder
    from .closeadminhelper.closeadminhelper_request_builder import CloseadminhelperRequestBuilder
    from .colortheme.colortheme_request_builder import ColorthemeRequestBuilder
    from .companywhitelabel.companywhitelabel_request_builder import CompanywhitelabelRequestBuilder
    from .cookiesettings.cookiesettings_request_builder import CookiesettingsRequestBuilder
    from .cultures.cultures_request_builder import CulturesRequestBuilder
    from .customnavigation.customnavigation_request_builder import CustomnavigationRequestBuilder
    from .customschemas.customschemas_request_builder import CustomschemasRequestBuilder
    from .dns.dns_request_builder import DnsRequestBuilder
    from .emailactivation.emailactivation_request_builder import EmailactivationRequestBuilder
    from .enablewhitelabel.enablewhitelabel_request_builder import EnablewhitelabelRequestBuilder
    from .encryption.encryption_request_builder import EncryptionRequestBuilder
    from .greetingsettings.greetingsettings_request_builder import GreetingsettingsRequestBuilder
    from .iprestrictions.iprestrictions_request_builder import IprestrictionsRequestBuilder
    from .license.license_request_builder import LicenseRequestBuilder
    from .logo.logo_request_builder import LogoRequestBuilder
    from .machine.machine_request_builder import MachineRequestBuilder
    from .maildomainsettings.maildomainsettings_request_builder import MaildomainsettingsRequestBuilder
    from .messagesettings.messagesettings_request_builder import MessagesettingsRequestBuilder
    from .notification.notification_request_builder import NotificationRequestBuilder
    from .owner.owner_request_builder import OwnerRequestBuilder
    from .payment.payment_request_builder import PaymentRequestBuilder
    from .push.push_request_builder import PushRequestBuilder
    from .rebranding.rebranding_request_builder import RebrandingRequestBuilder
    from .roomquotasettings.roomquotasettings_request_builder import RoomquotasettingsRequestBuilder
    from .security.security_request_builder import SecurityRequestBuilder
    from .sendadmmail.sendadmmail_request_builder import SendadmmailRequestBuilder
    from .sendjoininvite.sendjoininvite_request_builder import SendjoininviteRequestBuilder
    from .socket.socket_request_builder import SocketRequestBuilder
    from .ssov2.ssov2_request_builder import Ssov2RequestBuilder
    from .statistics.statistics_request_builder import StatisticsRequestBuilder
    from .storage.storage_request_builder import StorageRequestBuilder
    from .tenantquotasettings.tenantquotasettings_request_builder import TenantquotasettingsRequestBuilder
    from .tfaapp.tfaapp_request_builder import TfaappRequestBuilder
    from .tfaappcodes.tfaappcodes_request_builder import TfaappcodesRequestBuilder
    from .tfaappnewapp.tfaappnewapp_request_builder import TfaappnewappRequestBuilder
    from .tfaappnewcodes.tfaappnewcodes_request_builder import TfaappnewcodesRequestBuilder
    from .tfaappwithlink.tfaappwithlink_request_builder import TfaappwithlinkRequestBuilder
    from .timezones.timezones_request_builder import TimezonesRequestBuilder
    from .tips.tips_request_builder import TipsRequestBuilder
    from .userquotasettings.userquotasettings_request_builder import UserquotasettingsRequestBuilder
    from .webhook.webhook_request_builder import WebhookRequestBuilder
    from .webhooks.webhooks_request_builder import WebhooksRequestBuilder
    from .webplugins.webplugins_request_builder import WebpluginsRequestBuilder
    from .whitelabel.whitelabel_request_builder import WhitelabelRequestBuilder
    from .wizard.wizard_request_builder import WizardRequestBuilder

class SettingsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new SettingsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings{?withpassword*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SettingsRequestBuilderGetQueryParameters]] = None) -> Optional[SettingsDto]:
        """
        Returns a list of all the available portal settings with the current values for each parameter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SettingsDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.success_api_response_of_a_s_c.web.api.api_model.response_dto.settings_dto import SettingsDto

        return await self.request_adapter.send_async(request_info, SettingsDto, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SettingsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of all the available portal settings with the current values for each parameter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> SettingsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SettingsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SettingsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def authservice(self) -> AuthserviceRequestBuilder:
        """
        The authservice property
        """
        from .authservice.authservice_request_builder import AuthserviceRequestBuilder

        return AuthserviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def closeadminhelper(self) -> CloseadminhelperRequestBuilder:
        """
        The closeadminhelper property
        """
        from .closeadminhelper.closeadminhelper_request_builder import CloseadminhelperRequestBuilder

        return CloseadminhelperRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def colortheme(self) -> ColorthemeRequestBuilder:
        """
        The colortheme property
        """
        from .colortheme.colortheme_request_builder import ColorthemeRequestBuilder

        return ColorthemeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def companywhitelabel(self) -> CompanywhitelabelRequestBuilder:
        """
        The companywhitelabel property
        """
        from .companywhitelabel.companywhitelabel_request_builder import CompanywhitelabelRequestBuilder

        return CompanywhitelabelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cookiesettings(self) -> CookiesettingsRequestBuilder:
        """
        The cookiesettings property
        """
        from .cookiesettings.cookiesettings_request_builder import CookiesettingsRequestBuilder

        return CookiesettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cultures(self) -> CulturesRequestBuilder:
        """
        The cultures property
        """
        from .cultures.cultures_request_builder import CulturesRequestBuilder

        return CulturesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customnavigation(self) -> CustomnavigationRequestBuilder:
        """
        The customnavigation property
        """
        from .customnavigation.customnavigation_request_builder import CustomnavigationRequestBuilder

        return CustomnavigationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customschemas(self) -> CustomschemasRequestBuilder:
        """
        The customschemas property
        """
        from .customschemas.customschemas_request_builder import CustomschemasRequestBuilder

        return CustomschemasRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dns(self) -> DnsRequestBuilder:
        """
        The dns property
        """
        from .dns.dns_request_builder import DnsRequestBuilder

        return DnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def emailactivation(self) -> EmailactivationRequestBuilder:
        """
        The emailactivation property
        """
        from .emailactivation.emailactivation_request_builder import EmailactivationRequestBuilder

        return EmailactivationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enablewhitelabel(self) -> EnablewhitelabelRequestBuilder:
        """
        The enablewhitelabel property
        """
        from .enablewhitelabel.enablewhitelabel_request_builder import EnablewhitelabelRequestBuilder

        return EnablewhitelabelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def encryption(self) -> EncryptionRequestBuilder:
        """
        The encryption property
        """
        from .encryption.encryption_request_builder import EncryptionRequestBuilder

        return EncryptionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def greetingsettings(self) -> GreetingsettingsRequestBuilder:
        """
        The greetingsettings property
        """
        from .greetingsettings.greetingsettings_request_builder import GreetingsettingsRequestBuilder

        return GreetingsettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def iprestrictions(self) -> IprestrictionsRequestBuilder:
        """
        The iprestrictions property
        """
        from .iprestrictions.iprestrictions_request_builder import IprestrictionsRequestBuilder

        return IprestrictionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def license(self) -> LicenseRequestBuilder:
        """
        The license property
        """
        from .license.license_request_builder import LicenseRequestBuilder

        return LicenseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logo(self) -> LogoRequestBuilder:
        """
        The logo property
        """
        from .logo.logo_request_builder import LogoRequestBuilder

        return LogoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def machine(self) -> MachineRequestBuilder:
        """
        The machine property
        """
        from .machine.machine_request_builder import MachineRequestBuilder

        return MachineRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def maildomainsettings(self) -> MaildomainsettingsRequestBuilder:
        """
        The maildomainsettings property
        """
        from .maildomainsettings.maildomainsettings_request_builder import MaildomainsettingsRequestBuilder

        return MaildomainsettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def messagesettings(self) -> MessagesettingsRequestBuilder:
        """
        The messagesettings property
        """
        from .messagesettings.messagesettings_request_builder import MessagesettingsRequestBuilder

        return MessagesettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notification(self) -> NotificationRequestBuilder:
        """
        The notification property
        """
        from .notification.notification_request_builder import NotificationRequestBuilder

        return NotificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owner(self) -> OwnerRequestBuilder:
        """
        The owner property
        """
        from .owner.owner_request_builder import OwnerRequestBuilder

        return OwnerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payment(self) -> PaymentRequestBuilder:
        """
        The payment property
        """
        from .payment.payment_request_builder import PaymentRequestBuilder

        return PaymentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def push(self) -> PushRequestBuilder:
        """
        The push property
        """
        from .push.push_request_builder import PushRequestBuilder

        return PushRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rebranding(self) -> RebrandingRequestBuilder:
        """
        The rebranding property
        """
        from .rebranding.rebranding_request_builder import RebrandingRequestBuilder

        return RebrandingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def roomquotasettings(self) -> RoomquotasettingsRequestBuilder:
        """
        The roomquotasettings property
        """
        from .roomquotasettings.roomquotasettings_request_builder import RoomquotasettingsRequestBuilder

        return RoomquotasettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security(self) -> SecurityRequestBuilder:
        """
        The security property
        """
        from .security.security_request_builder import SecurityRequestBuilder

        return SecurityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sendadmmail(self) -> SendadmmailRequestBuilder:
        """
        The sendadmmail property
        """
        from .sendadmmail.sendadmmail_request_builder import SendadmmailRequestBuilder

        return SendadmmailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sendjoininvite(self) -> SendjoininviteRequestBuilder:
        """
        The sendjoininvite property
        """
        from .sendjoininvite.sendjoininvite_request_builder import SendjoininviteRequestBuilder

        return SendjoininviteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def socket(self) -> SocketRequestBuilder:
        """
        The socket property
        """
        from .socket.socket_request_builder import SocketRequestBuilder

        return SocketRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ssov2(self) -> Ssov2RequestBuilder:
        """
        The ssov2 property
        """
        from .ssov2.ssov2_request_builder import Ssov2RequestBuilder

        return Ssov2RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def statistics(self) -> StatisticsRequestBuilder:
        """
        The statistics property
        """
        from .statistics.statistics_request_builder import StatisticsRequestBuilder

        return StatisticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def storage(self) -> StorageRequestBuilder:
        """
        The storage property
        """
        from .storage.storage_request_builder import StorageRequestBuilder

        return StorageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenantquotasettings(self) -> TenantquotasettingsRequestBuilder:
        """
        The tenantquotasettings property
        """
        from .tenantquotasettings.tenantquotasettings_request_builder import TenantquotasettingsRequestBuilder

        return TenantquotasettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tfaapp(self) -> TfaappRequestBuilder:
        """
        The tfaapp property
        """
        from .tfaapp.tfaapp_request_builder import TfaappRequestBuilder

        return TfaappRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tfaappcodes(self) -> TfaappcodesRequestBuilder:
        """
        The tfaappcodes property
        """
        from .tfaappcodes.tfaappcodes_request_builder import TfaappcodesRequestBuilder

        return TfaappcodesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tfaappnewapp(self) -> TfaappnewappRequestBuilder:
        """
        The tfaappnewapp property
        """
        from .tfaappnewapp.tfaappnewapp_request_builder import TfaappnewappRequestBuilder

        return TfaappnewappRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tfaappnewcodes(self) -> TfaappnewcodesRequestBuilder:
        """
        The tfaappnewcodes property
        """
        from .tfaappnewcodes.tfaappnewcodes_request_builder import TfaappnewcodesRequestBuilder

        return TfaappnewcodesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tfaappwithlink(self) -> TfaappwithlinkRequestBuilder:
        """
        The tfaappwithlink property
        """
        from .tfaappwithlink.tfaappwithlink_request_builder import TfaappwithlinkRequestBuilder

        return TfaappwithlinkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def timezones(self) -> TimezonesRequestBuilder:
        """
        The timezones property
        """
        from .timezones.timezones_request_builder import TimezonesRequestBuilder

        return TimezonesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tips(self) -> TipsRequestBuilder:
        """
        The tips property
        """
        from .tips.tips_request_builder import TipsRequestBuilder

        return TipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def userquotasettings(self) -> UserquotasettingsRequestBuilder:
        """
        The userquotasettings property
        """
        from .userquotasettings.userquotasettings_request_builder import UserquotasettingsRequestBuilder

        return UserquotasettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def webhook(self) -> WebhookRequestBuilder:
        """
        The webhook property
        """
        from .webhook.webhook_request_builder import WebhookRequestBuilder

        return WebhookRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def webhooks(self) -> WebhooksRequestBuilder:
        """
        The webhooks property
        """
        from .webhooks.webhooks_request_builder import WebhooksRequestBuilder

        return WebhooksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def webplugins(self) -> WebpluginsRequestBuilder:
        """
        The webplugins property
        """
        from .webplugins.webplugins_request_builder import WebpluginsRequestBuilder

        return WebpluginsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def whitelabel(self) -> WhitelabelRequestBuilder:
        """
        The whitelabel property
        """
        from .whitelabel.whitelabel_request_builder import WhitelabelRequestBuilder

        return WhitelabelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wizard(self) -> WizardRequestBuilder:
        """
        The wizard property
        """
        from .wizard.wizard_request_builder import WizardRequestBuilder

        return WizardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SettingsRequestBuilderGetQueryParameters():
        """
        Returns a list of all the available portal settings with the current values for each parameter.
        """
        # Specifies if the password hasher settings will be returned or not
        withpassword: Optional[bool] = None

    
    @dataclass
    class SettingsRequestBuilderGetRequestConfiguration(RequestConfiguration[SettingsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

