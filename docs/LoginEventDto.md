# LoginEventDto
One entry of the portal login history: a sign-in, a sign-out or a failed attempt, and where it came from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the recorded sign-in. When the entry is a successful sign-in that is still open, this is also  the value `GET api/2.0/security/activeconnections` reports as the connection's `id`. | [optional] 
**var_date** | [**ApiDateTime**](ApiDateTime.md) | When the attempt was made, in the portal time zone. The `from` and `to` filters are read as UTC instants,  so the two do not line up on a portal that is not on UTC. | [optional] 
**user** | **str** | The display name of the account the attempt was made against, taken from the account as it stands now  rather than as it stood at the time. A localised placeholder stands in when there is no account to read,  which is the usual case for a failed attempt on an address nobody owns. | [optional] 
**user_id** | **UUID** | The ID of that account, which is what the `userId` filter of this operation matches on. It is the empty  GUID when the attempt could not be tied to an account. | [optional] 
**login** | **str** | The login string as it was typed - normally the email address. It is the only field that survives a failed  attempt against an unknown account, which makes it the one to read when `user` is a placeholder. | [optional] 
**action** | **str** | The event as a readable sentence in the portal language. On `GET api/2.0/security/audit/login/last` each  substituted value is cut to 50 characters; the filtered operation substitutes them in full. | [optional] 
**action_id** | [**MessageAction**](MessageAction.md) | What happened, as the `action` filter of this operation spells it: a successful sign-in, a failed one, a  sign-out. Use this rather than parsing `action`, which is prose and changes with the portal language. | [optional] 
**ip** | **str** | The IP address the attempt came from, with the port stripped off. | [optional] 
**country** | **str** | The English name of the country the IP address is located in, empty when the address cannot be located -  the normal outcome for private and loopback addresses. | [optional] 
**city** | **str** | The city the IP address is located in, empty under the same conditions as `country`. | [optional] 
**browser** | **str** | The browser and its version as parsed from the user agent of the attempt, empty when the client sent none  that could be parsed. | [optional] 
**platform** | **str** | The operating system as parsed from the same user agent, empty under the same conditions as `browser`. | [optional] 
**page** | **str** | Where in the portal the attempt was made from: the referrer of the request, or that request's own path  when it carried no referrer. Long values are cut off at 512 characters. | [optional] 

## Example

```python
from docspace_api_sdk.models.login_event_dto import LoginEventDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginEventDto from a JSON string
login_event_dto_instance = LoginEventDto.from_json(json)
# print the JSON string representation of the object
print(LoginEventDto.to_json())

# convert the object into a dict
login_event_dto_dict = login_event_dto_instance.to_dict()
# create an instance of LoginEventDto from a dict
login_event_dto_from_dict = LoginEventDto.from_dict(login_event_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


