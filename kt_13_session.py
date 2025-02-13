# # 1. Python - URL Processing
# # 1.1 Improve your skills in web scraping, fetching data, and managing URLs with Python using urllib
#
# from urllib.parse import urlparse
#
# url = "https://example.com/employees/name/?salary>=25000"
# parsed_url = urlparse(url)
# print(type(parsed_url))
# print("Scheme:", parsed_url.scheme)
# print("netloc:", parsed_url.netloc)
# print("path:", parsed_url.path)
# print("params:", parsed_url.params)
# print("Query string:", parsed_url.query)
# print("Frgment:", parsed_url.fragment)
#
# # 1.2 Dict info
# from urllib.parse import urlparse, parse_qs
#
# url = "https://example.com/employees?name=Anand&salary=25000"
# parsed_url = urlparse(url)
# dct = parse_qs(parsed_url.query)
# print("Query parameters:", dct)
#
# # 1.3 Download image
# from urllib.request import urlopen
#
# obj = urlopen("https://www.tutorialspoint.com/images/logo.png")
# data = obj.read()
# img = open("img.jpg", "wb")
# img.write(data)
# img.close()
#
# # 2. Request Object
# """
# urllib.request.Request(url, data, headers, origin_req_host, method=None)
# """
# from urllib.request import Request, urlopen
#
# obj = Request("https://www.tutorialspoint.com/")
# print(f"Request obj: {obj}")
# resp = urlopen(obj)
# data = resp.read()
# print(f"Request Data: {data}")

# 3. Argument Parsing (argparse)
r"""
Step-1: Use -h command
C:\Users\muthukus\Documents\Python_scripts\Python_KT>python kt_13_session.py -h
usage: Argument Parsing Example [-h] [--os-type {Windows,Linux}] --test-run-type PROVIDE TEST RUN TYPE

options:
  -h, --help            show this help message and exit
  --os-type {Windows,Linux}
                        Default as Windows, Run only Windows Script if argument as "Windows", Otherwise run the given
                        OS type of Script
  --test-run-type PROVIDE TEST RUN TYPE
                        Like Selenium or REST API test or Normal test case

Step-1.1: Use --help command
C:\Users\muthukus\Documents\Python_scripts\Python_KT>python kt_13_session.py --help
usage: Argument Parsing Example [-h] [--os-type {Windows,Linux}] --test-run-type TEST_RUN_TYPE

options:
  -h, --help            show this help message and exit
  --os-type {Windows,Linux}
                        Default as Windows, Run only Windows Script if argument as "Windows", Otherwise run the given
                        OS type of Script
  --test-run-type TEST_RUN_TYPE
                        Like Selenium or REST API test or Normal test case

C:\Users\muthukus\Documents\Python_scripts\Python_KT>

Step-2: Run script without any argument(s)
C:\Users\muthukus\Documents\Python_scripts\Python_KT>python kt_13_session.py
usage: Argument Parsing Example [-h] [--os-type {Windows,Linux}] --test-run-type TEST_RUN_TYPE
Argument Parsing Example: error: the following arguments are required: --test-run-type

C:\Users\muthukus\Documents\Python_scripts\Python_KT>

Step-3: Run script with argument(s)
C:\Users\muthukus\Documents\Python_scripts\Python_KT>python kt_13_session.py --test-run-type REST
Get Namespace: Namespace(os_type='Windows', test_run_type='REST')
Display (Args Value): Windows, REST

C:\Users\muthukus\Documents\Python_scripts\Python_KT>
"""
import argparse

arg_obj = argparse.ArgumentParser("Argument Parsing Example")
arg_obj.add_argument('--os-type', type=str, choices=['Windows', 'Linux'],
                     dest='os_type', required=False, default='Windows',
                     help='Default as Windows, Run only Windows Script if argument as "Windows", '
                          'Otherwise run the given OS type of Script')
arg_obj.add_argument('--test-run-type', type=str,
                     dest='test_run_type', required=True,
                     help='Like Selenium or REST API test or Normal test case')
get_parse = arg_obj.parse_args()
print(f"Get Namespace: {get_parse}")
final_os_type = get_parse.os_type
final_test_run_type = get_parse.test_run_type
print(f"Display (Args Value): {final_os_type}, {final_test_run_type}")

