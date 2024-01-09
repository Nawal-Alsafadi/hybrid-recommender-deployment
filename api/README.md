# The backend to chatbot application with the indexing form using ChatGpt

## requirements

```
langchain==0.0.167
llama_index==0.6.6
flask==2.3.2
flask_cors==3.0.10
scikit-learn==1.0.2
texthero==1.1.0
tensorflow==2.12.0
opencv-python==4.7.0.72
mlxtend==0.22.0
scikit-surprise==1.1.3
```

```
Note:
    Requires-Python >=3.9,
```

# Usage

###### Create an environment using Python 3.9, install the required packages.

```
pip install -r requirements.txt
```

# Storage

## chatbot services

### 1- chatbot vendor service:

```
data/chatbot_services/vendor_service
```

### Products Similarity:

```
data/recommendation/product_similarity/train.csv
```

### Image search:

```
data/image_search/data/
```

### Collaborative recommendation:

```
data/recommendation/collaborative/train.csv
```

### Popular recommendation:

```
data/recommendation/popularity/train.csv
```

# Routes


## chatbot services:

### chatbot vendor service:


##### - Chat with vendor:

```
 Url: /api/chat-vendor
 Method : POST
 Payload: { 
           "question": (String)*
         }

```

###### success response

```
{
        "message": "Response completed successfully.",
        "success": True,
        "result": string
},200
```

###### error response

```
{
    "message": "A problem occurred during the chat process !!!",
    "success": False
},500
```

##### - Train vendor chatbot service:

```
 Url: /api/train-chat-vendor
 Method: POST
 Payload: {
    "data_name" : (string)*,
    "data" :
    [
        {"question" : "answer"}
        ........................
        ........................
        ........................
    ]
    
}
```

###### success response

```
{
    "message": "Training completed successfully",
    "success": True
},201

```

###### error response

```
{
    "message": "something went wrong, we're working to solve it",
    "success": False
},500
```

### Products Similarity:

##### - Get products Similarity:

```
 Url: /api/products-similarity
 Method : GET
 Params: { 
           "item_id":(int)*,
           "num_recommendations": (int) - default 10
         }

```

###### success response

```
{
     "message": "Recommendation completed successfully.",
     "success": True,
     "products_ids": result
},200
```

###### error response

```
{
    "message": "something went wrong, we're working to solve it",
    "success": False
},500
```

##### - Train products Similarity:

```
 Url: /api/train-products-similarity
 Method: POST
```

###### success response

```
{
    "message": "Training completed successfully",
    "success": True
},201

```

###### error response

```
{
    "message": "something went wrong, we're working to solve it",
    "success": False
},500
```

### Products recommendation:

##### - Get products recommendation:

```
 Url: /api/recommendation/products
 Method : GET
 Params: { 
           "user_id":(int)*,
           "num_recommendations": (int) - default 10
         }

```

###### success response

```
{
     "message": "Recommendation completed successfully.",
     "success": True,
     "products_ids": <int>[]
},200
```

###### error response

```
{
    "message": "something went wrong, we're working to solve it",
    "success": False
},500
```

##### - Train products recommendation:

```
 Url: /api/recommendation/train-products
 Method: POST
```

###### success response

```
{
    "message": "Training completed successfully",
    "success": True
},201

```

###### error response

```
{
    "message": "something went wrong, we're working to solve it",
    "success": False
},500
```

### Collaborative recommendation:

##### - Get products recommendation:

```
 Url: /api/recommendation/collaborative
 Method : GET
 Params: { 
           "user_id":(int)*,
           "num_recommendations": (int) - default 10
         }

```

###### success response

```
{
     "message": "Recommendation completed successfully.",
     "success": True,
     "products_ids": <int>[]
},200
```

###### error response

```
{
    "message": "something went wrong, we're working to solve it",
    "success": False
},500
```

##### - Train products recommendation:

```
 Url: /api/recommendation/train-collaborative
 Method: POST
```

###### success response

```
{
    "message": "Training completed successfully",
    "success": True
},201

```

###### error response

```
{
    "message": "something went wrong, we're working to solve it",
    "success": False
},500
```

### Popular recommendation:

##### - Get products recommendation:

```
 Url: /api/recommendation/popularity
 Method : GET
 Params: { 
           "user_id":(int)*,
           "num_recommendations": (int) - default 10
         }

```

###### success response

```
{
     "message": "Recommendation completed successfully.",
     "success": True,
     "products_ids": <int>[]
},200
```

###### error response

```
{
    "message": "something went wrong, we're working to solve it",
    "success": False
},500
```

##### - Train products recommendation:

```
 Url: /api/recommendation/train-popularity
 Method: POST
```

###### success response

```
{
    "message": "Training completed successfully",
    "success": True
},201

```

###### error response

```
{
    "message": "something went wrong, we're working to solve it",
    "success": False
},500
```

### Image search:

##### - Get similarity images:

```
 Url: /api/image-search
 Method : POST
 Params: { 
           "image": (file)*,
           "num_results": (int) - default 10
         }

```

###### success response

```
{
     "message": "Similar images completed successfully.",
     "success": True,
     "results": <String>[]
},200
```

###### error response

```
{
    "message": "something went wrong, we're working to solve it",
    "success": False
},500
```

##### - Train Image search:

```
 Url: /api/train-image-search
 Method: POST
```

###### success response

```
{
    "message": "Training Image search model completed successfully",
    "success": True
},201

```

###### error response

```
{
    "message": "something went wrong, we're working to solve it",
    "success": False
},500
```

