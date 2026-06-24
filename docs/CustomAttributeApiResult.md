# CustomAttributeApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the attribute | 
**options** | [**[CustomAttributeOptionApiResult]**](CustomAttributeOptionApiResult.md) | Collection of the attribute options   Available for attributes of type &#x60;options&#x60; and &#x60;multiple options&#x60; only | 
**type** | [**CustomAttributeType**](CustomAttributeType.md) |  | 
**is_deleted** | **bool** | Indicates if the attribute is deleted | 
**name** | **str** | Name of the attribute | 
**is_enabled** | **bool** | Indicates if the attribute is enabled | 
**is_required** | **bool** | Indicates if the attribute value is mandatory to specify | 
**is_global** | **bool** | Indicates if the attribute is available across all projects | 
**is_system** | **bool** | Indicates if the attribute is system | 
**targets** | **[str]** | Collection of the attribute targets   Defines where the attribute can be used (e.g., TestCases, AutoTestCases, TestPlans) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


