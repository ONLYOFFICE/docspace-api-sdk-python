# AmazonS3RegionArrayWrapper
The successful API response containing the list of AmazonS3RegionDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[AmazonS3RegionDto]**](AmazonS3RegionDto.md) | The list of AmazonS3RegionDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.amazon_s3_region_array_wrapper import AmazonS3RegionArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonS3RegionArrayWrapper from a JSON string
amazon_s3_region_array_wrapper_instance = AmazonS3RegionArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(AmazonS3RegionArrayWrapper.to_json())

# convert the object into a dict
amazon_s3_region_array_wrapper_dict = amazon_s3_region_array_wrapper_instance.to_dict()
# create an instance of AmazonS3RegionArrayWrapper from a dict
amazon_s3_region_array_wrapper_from_dict = AmazonS3RegionArrayWrapper.from_dict(amazon_s3_region_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


