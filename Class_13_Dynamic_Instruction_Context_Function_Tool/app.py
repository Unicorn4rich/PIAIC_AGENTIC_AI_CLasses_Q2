import json
from function_schema import get_function_schema


def dynamic_instruction(valueeee: str = "azlaan")-> str: # ye us data ki tanki ka null hai jis se data nikalty hain.
    """ This is a function of dynamic_instruction """  # dock string hmara descrption ban jata hai.
    return f"you are a {valueeee} helpful assistant" # function schema sab uthaa leta hai but ye return nahi uthata apne object mein.


schema = get_function_schema(dynamic_instruction)
print(json.dumps(schema, indent=2))



# 3. @function_tool # ye agent ko ye wala function schema bana kar bhejta hai
# 4. uv add function_schema => install this  
# is tarhn pass hota hai ye function schema ban kar agent ko or isme function mein lgai hui sari propertys object ki shakal meinpass hoti hain.

# {
#   "name": "dynamic_instruction",
#   "description": "This is a function of dynamic_instruction ",
#   "parameters": {
#     "type": "object",
#     "properties": {
#       "valueeee": {
#         "type": "string",
#         "description": "The valueeee parameter",
#         "default": "azlaan"
#       }
#     },
#     "required": []
#   }
# }