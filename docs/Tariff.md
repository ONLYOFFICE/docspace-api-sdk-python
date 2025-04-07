# Tariff


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**state** | [**TariffState**](TariffState.md) |  | [optional] 
**due_date** | **datetime** | Due date | [optional] 
**delay_due_date** | **datetime** | Delay due date | [optional] 
**license_date** | **datetime** | License date | [optional] 
**customer_id** | **str** | Customer ID | [optional] 
**quotas** | [**List[Quota]**](Quota.md) | List of quotas | [optional] 

## Example

```python
from docspace.models.tariff import Tariff

# TODO update the JSON string below
json = "{}"
# create an instance of Tariff from a JSON string
tariff_instance = Tariff.from_json(json)
# print the JSON string representation of the object
print(Tariff.to_json())

# convert the object into a dict
tariff_dict = tariff_instance.to_dict()
# create an instance of Tariff from a dict
tariff_from_dict = Tariff.from_dict(tariff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


