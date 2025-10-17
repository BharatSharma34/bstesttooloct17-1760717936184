from tapestrysdk import image_to_text
import json

"""
testToolbs2oct17 - Custom Lambda Tool
Description: test

IMPORTANT: Only edit the code in the main() function below.
The Lambda handler will be automatically appended during deployment.
DO NOT add lambda_handler code here - it will be added automatically.
"""

token = "sk-25v4vpy1z-mgv3j044"

def main(user_prompt, document, name):
    try:
        # result = image_to_text(token, user_prompt, document, name, "describe this image in detail")
        return "response"
    except Exception as e:
        return e
