import time
import openapi_client
from pprint import pprint
from com.spoonacular import default_api
from openapi_client.model.analyze_recipe_request import AnalyzeRecipeRequest
from openapi_client.model.analyze_recipe_request1 import AnalyzeRecipeRequest1
from openapi_client.model.search_restaurants200_response import SearchRestaurants200Response
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    analyze_recipe_request = AnalyzeRecipeRequest(
        language="en",
        include_nutrition=False,
        include_taste=False,
    ) # AnalyzeRecipeRequest | Example request body.
    language = "en" # str | The input language, either \"en\" or \"de\". (optional)
    include_nutrition = False # bool | Whether nutrition data should be added to correctly parsed ingredients. (optional)
    include_taste = False # bool | Whether taste data should be added to correctly parsed ingredients. (optional)

    try:
        # Analyze Recipe
        api_response = api_instance.analyze_recipe(analyze_recipe_request, language=language, include_nutrition=include_nutrition, include_taste=include_taste)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->analyze_recipe: %s\n" % e)