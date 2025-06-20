# TestPlanTestPointsInquiryApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**List[Order]**](Order.md) |  | 
**page** | [**Page**](Page.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_plan_test_points_inquiry_api_model import TestPlanTestPointsInquiryApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanTestPointsInquiryApiModel from a JSON string
test_plan_test_points_inquiry_api_model_instance = TestPlanTestPointsInquiryApiModel.from_json(json)
# print the JSON string representation of the object
print TestPlanTestPointsInquiryApiModel.to_json()

# convert the object into a dict
test_plan_test_points_inquiry_api_model_dict = test_plan_test_points_inquiry_api_model_instance.to_dict()
# create an instance of TestPlanTestPointsInquiryApiModel from a dict
test_plan_test_points_inquiry_api_model_from_dict = TestPlanTestPointsInquiryApiModel.from_dict(test_plan_test_points_inquiry_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


