# ContactPayload

An additional contact from a user's profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The kind of contact as stored in the profile, such as &#x60;mail&#x60;, &#x60;phone&#x60; or &#x60;facebook&#x60;. | [optional] 
**value** | **str** | The contact itself: an address, a number or a profile link, as the user entered it. | [optional] 

## Example

```python
from docspace_webhooks_sdk.models.contact_payload import ContactPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ContactPayload from a JSON string
contact_payload_instance = ContactPayload.from_json(json)
# print the JSON string representation of the object
print(ContactPayload.to_json())

# convert the object into a dict
contact_payload_dict = contact_payload_instance.to_dict()
# create an instance of ContactPayload from a dict
contact_payload_from_dict = ContactPayload.from_dict(contact_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


