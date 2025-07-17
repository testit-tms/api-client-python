# Inquiry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**CompositeFilter**](CompositeFilter.md) |  | [optional] 
**order** | [**List[Order]**](Order.md) |  | 
**page** | [**Page**](Page.md) |  | [optional] 

## Example

```python
from testit_api_client.models.inquiry import Inquiry

# TODO update the JSON string below
json = "{}"
# create an instance of Inquiry from a JSON string
inquiry_instance = Inquiry.from_json(json)
# print the JSON string representation of the object
print Inquiry.to_json()

# convert the object into a dict
inquiry_dict = inquiry_instance.to_dict()
# create an instance of Inquiry from a dict
inquiry_from_dict = Inquiry.from_dict(inquiry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


