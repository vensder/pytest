# AWS Lambda Function for 2 and 3 versions of Python
import sys

def lambda_handler(event, context):
    mod_list = sorted(sys.modules.keys())
    return(len(mod_list), mod_list)
