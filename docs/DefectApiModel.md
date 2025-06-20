# DefectApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_url** | **str** | Link to created issue | 

## Example

```python
from testit_api_client.models.defect_api_model import DefectApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of DefectApiModel from a JSON string
defect_api_model_instance = DefectApiModel.from_json(json)
# print the JSON string representation of the object
print(DefectApiModel.to_json())

# convert the object into a dict
defect_api_model_dict = defect_api_model_instance.to_dict()
# create an instance of DefectApiModel from a dict
defect_api_model_from_dict = DefectApiModel.from_dict(defect_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


