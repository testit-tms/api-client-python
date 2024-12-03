# FailureClassModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**failure_category** | [**FailureCategoryModel**](FailureCategoryModel.md) |  | 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**failure_class_regexes** | [**List[FailureClassRegexModel]**](FailureClassRegexModel.md) |  | [optional] 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 

## Example

```python
from testit_api_client.models.failure_class_model import FailureClassModel

# TODO update the JSON string below
json = "{}"
# create an instance of FailureClassModel from a JSON string
failure_class_model_instance = FailureClassModel.from_json(json)
# print the JSON string representation of the object
print(FailureClassModel.to_json())

# convert the object into a dict
failure_class_model_dict = failure_class_model_instance.to_dict()
# create an instance of FailureClassModel from a dict
failure_class_model_from_dict = FailureClassModel.from_dict(failure_class_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


