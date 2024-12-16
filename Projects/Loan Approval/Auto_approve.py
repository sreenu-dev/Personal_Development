import requests
import json

url = "https://fasalrin.gov.in/application/approveLoanApplication"

# Read and parse the JSON file
with open('request_list_for_approval.json', 'r') as file:
    request_list = json.load(file)

# Open a file to save the responses
with open('responses.txt', 'w') as response_file:
    for requesti in request_list['data']['list']:
        print(requesti['loanFinancialDetailsID'])
        print(requesti['financialYear'])
        payload = json.dumps({
            "data": {
                "financialYear": requesti['financialYear'],
                "loanFinancialDetailsID": requesti['loanFinancialDetailsID'],
                "actionType": "APPROVE"
            }
        })
        headers = {
            'Cookie': 'connect.sid=s%3AiZYkr1CO-ga8Yn0sgLYzGRkaokPbKkJP.0oDDobPXRTJCn3iW0GHPUaKFfmY%2FQ31hoKZM0yf1xc4',
            'Host': 'fasalrin.gov.in',
            'Origin': 'https://fasalrin.gov.in',
            'Referer': 'https://fasalrin.gov.in/applicationpreview',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        # Write the response to the file
        response_file.write(f"Response for loanFinancialDetailsID {requesti['loanFinancialDetailsID']}:\n")
        response_file.write(response.text + "\n")
        response_file.write(f"Beneficiary Name: {requesti['beneficiaryName']}\n")
        response_file.write(f"Mobile: {requesti['mobile']}\n")
        response_file.write(f"Account Number: {requesti['accountNumber']}\n")
        response_file.write(f"Application No: {requesti['applicationNo']}\n")
        response_file.write('-----------------------------------\n')

        # Print the response to the console
        print(response.text)
        print(requesti['beneficiaryName'])
        print(requesti['mobile'])
        print(requesti['accountNumber'])
        print(requesti['applicationNo'])
        print('-----------------------------------')