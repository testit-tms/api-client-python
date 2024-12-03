# CustomAttributeTestPlanProjectRelationPutModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Custom attribute internal unique identifier | 
**is_enabled** | **bool** | Flag that defines if custom attribute is enabled | 
**is_required** | **bool** | Flag that defines if custom attribute is required | 

## Example

```python
from testit_api_client.models.custom_attribute_test_plan_project_relation_put_model import CustomAttributeTestPlanProjectRelationPutModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeTestPlanProjectRelationPutModel from a JSON string
custom_attribute_test_plan_project_relation_put_model_instance = CustomAttributeTestPlanProjectRelationPutModel.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeTestPlanProjectRelationPutModel.to_json())

# convert the object into a dict
custom_attribute_test_plan_project_relation_put_model_dict = custom_attribute_test_plan_project_relation_put_model_instance.to_dict()
# create an instance of CustomAttributeTestPlanProjectRelationPutModel from a dict
custom_attribute_test_plan_project_relation_put_model_from_dict = CustomAttributeTestPlanProjectRelationPutModel.from_dict(custom_attribute_test_plan_project_relation_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


