# ContactsRequest

Parameters for updating user contacts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**List[Contact]**](Contact.md) | List of user contacts | [optional] 

## Example

```python
from docspace.models.contacts_request import ContactsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContactsRequest from a JSON string
contacts_request_instance = ContactsRequest.from_json(json)
# print the JSON string representation of the object
print(ContactsRequest.to_json())

# convert the object into a dict
contacts_request_dict = contacts_request_instance.to_dict()
# create an instance of ContactsRequest from a dict
contacts_request_from_dict = ContactsRequest.from_dict(contacts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


