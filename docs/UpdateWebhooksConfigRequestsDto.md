# UpdateWebhooksConfigRequestsDto
The webhook subscription being changed, with the parameters it is to have afterwards.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The label the subscription is listed under. It is for the administrator reading the list and is never sent to  the target; it does not have to be unique. | 
**uri** | **str** | The address the portal posts the event payload to. It has to be an absolute `http` or `https` address outside  the installation own network, and it is probed before anything is stored: it must answer a HEAD request with  a success code, and a redirect does not count as one. | 
**secret_key** | **str** | The shared secret the payload signature is computed with, so the receiver can tell a genuine call from a  forged one. It has to satisfy the portal password rules published by  `GET api/2.0/settings/security/password`, and it is never echoed back by any operation. On an update an empty  value keeps the secret already stored. | [optional] 
**enabled** | **bool** | Whether the subscription delivers at all. While it is off the matching events are dropped rather than queued,  so nothing from that period arrives once it is switched on again. | [optional] 
**ssl** | **bool** | Whether the target certificate is verified. Setting it demands an `https` target with a valid certificate;  leaving it off delivers without checking the certificate at all. | [optional] 
**triggers** | [**WebhookTrigger**](WebhookTrigger.md) | The events the subscription listens for, as a bitmask combining the flags; 0 subscribes to all of them. Take  the flags the caller role is allowed to use from `GET api/2.0/settings/webhook/triggers`, since a flag beyond  that set is refused with 400. A subscription still only fires for events its creator may see. | [optional] 
**target_id** | **str** | The single entity the subscription is narrowed to, by its identifier - a room or a file, for instance.  Leaving it out delivers events about every entity the subscribed triggers cover. | [optional] 
**id** | **int** | The subscription to act on, by the `id` that `GET api/2.0/settings/webhook` reports. It travels in the body  rather than in the path, and an id that exists in no portal subscription answers 404. | 

## Example

```python
from docspace_api_sdk.models.update_webhooks_config_requests_dto import UpdateWebhooksConfigRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhooksConfigRequestsDto from a JSON string
update_webhooks_config_requests_dto_instance = UpdateWebhooksConfigRequestsDto.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhooksConfigRequestsDto.to_json())

# convert the object into a dict
update_webhooks_config_requests_dto_dict = update_webhooks_config_requests_dto_instance.to_dict()
# create an instance of UpdateWebhooksConfigRequestsDto from a dict
update_webhooks_config_requests_dto_from_dict = UpdateWebhooksConfigRequestsDto.from_dict(update_webhooks_config_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


