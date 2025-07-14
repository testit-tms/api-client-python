# GuidExtractionModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**exclude** | **List[str]** |  | [optional] 

## Example

```python
from testit_api_client.models.guid_extraction_model import GuidExtractionModel

# TODO update the JSON string below
json = "{}"
# create an instance of GuidExtractionModel from a JSON string
guid_extraction_model_instance = GuidExtractionModel.from_json(json)
# print the JSON string representation of the object
print GuidExtractionModel.to_json()

# convert the object into a dict
guid_extraction_model_dict = guid_extraction_model_instance.to_dict()
# create an instance of GuidExtractionModel from a dict
guid_extraction_model_from_dict = GuidExtractionModel.from_dict(guid_extraction_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


