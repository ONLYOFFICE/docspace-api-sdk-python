# TenantDomainValidator

The domain validator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regex** | **str** | The regex string to validate a domain. | [optional] [readonly] 
**min_length** | **int** | The minimum length of the valid domain. | [optional] [readonly] 
**max_length** | **int** | The maximum length of the valid domain. | [optional] [readonly] 

## Example

```python
from docspace.models.tenant_domain_validator import TenantDomainValidator

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDomainValidator from a JSON string
tenant_domain_validator_instance = TenantDomainValidator.from_json(json)
# print the JSON string representation of the object
print(TenantDomainValidator.to_json())

# convert the object into a dict
tenant_domain_validator_dict = tenant_domain_validator_instance.to_dict()
# create an instance of TenantDomainValidator from a dict
tenant_domain_validator_from_dict = TenantDomainValidator.from_dict(tenant_domain_validator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


