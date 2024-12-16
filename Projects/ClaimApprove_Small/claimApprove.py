import requests
import json

# Read the claims list from the JSON file
with open('E:\\Personal_Development\\Personal_Development\\Projects\\ClaimApprove_Small\\claims_list.json', 'r') as file:
    claims_list = json.load(file)

# Define the headers for the requests
headers = {
    'Cookie': 'connect.sid=s%3AAHeSBnjAWLw65dIxEoJ4QSm2Wt-vY6CZ.nAvhAz0s%2Fxwmy0DcVxCiMF3IZkK%2BjK6usZ7yW7SCRW4; connect.sid=s%3AAHeSBnjAWLw65dIxEoJ4QSm2Wt-vY6CZ.nAvhAz0s%2Fxwmy0DcVxCiMF3IZkK%2BjK6usZ7yW7SCRW4',
    'Content-Type': 'application/json'
}

approve_claim_url="https://fasalrin.gov.in/application/updateNewSeprateIsPriClaimWorkflowStatus"

# Open the responses file to write the logs
with open('E:\\Personal_Development\\Personal_Development\\Projects\\ClaimApprove_Small\\responses.txt', 'w') as response_file:
    for claims in claims_list['data']['list']:
        beneficiary_name = claims['beneficiaryName']
        mobile_number = claims['mobile']
        account_number = claims['accountNumber']
        application_number = claims['applicationNo']
        claim_id = claims['claimID']

        # Print and log the claim details
        print(f"Beneficiary Name: {beneficiary_name}")
        print(f"Mobile Number: {mobile_number}")
        print(f"Account Number: {account_number}")
        print(f"Application Number: {application_number}")
        print(f"Claim ID: {claim_id}")

        response_file.write(f"Beneficiary Name: {beneficiary_name}\n")
        response_file.write(f"Mobile Number: {mobile_number}\n")
        response_file.write(f"Account Number: {account_number}\n")
        response_file.write(f"Application Number: {application_number}\n")
        response_file.write(f"Claim ID: {claim_id}\n")

        # Prepare the payload for approving the claim
        approve_claim_payload = json.dumps({
            "data": {
                "financialYear": "2023-2024",
                "claimID": claim_id,
                "actionType": "APPROVE",
                "claimType": 1
            }
        })

        # Make the API request to approve the claim
        claim_approve = requests.put(approve_claim_url, headers=headers, data=approve_claim_payload)
        claim_approve_response = claim_approve.json()

        # Log the response
        # response_file.write(f"Response: {json.dumps(claim_approve_response, indent=4)}\n")

        # Check the response status and log the result
        if claim_approve_response.get('status') == True:
            print("Claim Approved")
            response_file.write("Claim Approved\n")
        else:
            print("Claim Not Approved")
            response_file.write("Claim Not Approved\n")

        response_file.write('-----------------------------------\n')

print("All claims processed. Check responses.txt for details.")