# IconRequest
The icon to set on a room group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **str** | The identifier of one of the built-in covers listed by `GET api/2.0/files/rooms/covers`. An empty string  clears the icon of the group, null or a missing member keeps the current one, and anything else is refused. | [optional] 

## Example

```python
from docspace_api_sdk.models.icon_request import IconRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IconRequest from a JSON string
icon_request_instance = IconRequest.from_json(json)
# print the JSON string representation of the object
print(IconRequest.to_json())

# convert the object into a dict
icon_request_dict = icon_request_instance.to_dict()
# create an instance of IconRequest from a dict
icon_request_from_dict = IconRequest.from_dict(icon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


