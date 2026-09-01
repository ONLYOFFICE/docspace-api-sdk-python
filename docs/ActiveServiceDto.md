# ActiveServiceDto
Represents an active wallet service (quota) of the current portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** | The name of the service. | [optional] 
**service_unit** | **str** | The unit of measurement for the service. | [optional] 
**subscription** | **bool** | Indicates whether the service is subscription-based. | [optional] 
**title** | **str** | The title of the service. | [optional] 
**limit** | **int** | The service limit. Populated only for the subscription-based services. | [optional] 
**used** | **int** | The current service usage. Populated only for the subscription-based services. | [optional] 

## Example

```python
from docspace_api_sdk.models.active_service_dto import ActiveServiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveServiceDto from a JSON string
active_service_dto_instance = ActiveServiceDto.from_json(json)
# print the JSON string representation of the object
print(ActiveServiceDto.to_json())

# convert the object into a dict
active_service_dto_dict = active_service_dto_instance.to_dict()
# create an instance of ActiveServiceDto from a dict
active_service_dto_from_dict = ActiveServiceDto.from_dict(active_service_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


