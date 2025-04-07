# RoomSecurityWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**RoomSecurityDto**](RoomSecurityDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.room_security_wrapper import RoomSecurityWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of RoomSecurityWrapper from a JSON string
room_security_wrapper_instance = RoomSecurityWrapper.from_json(json)
# print the JSON string representation of the object
print(RoomSecurityWrapper.to_json())

# convert the object into a dict
room_security_wrapper_dict = room_security_wrapper_instance.to_dict()
# create an instance of RoomSecurityWrapper from a dict
room_security_wrapper_from_dict = RoomSecurityWrapper.from_dict(room_security_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


