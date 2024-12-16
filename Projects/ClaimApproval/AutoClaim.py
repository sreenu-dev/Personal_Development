import datetime
import json
import requests
import uuid
import secrets

get_claim_user_url = "https://fasalrin.gov.in/application/getISPriClaimAppDetailsForAdd?financialYear=2023-2024&loanFinancialDetailsID="
save_claim_user_url = "https://fasalrin.gov.in/application/saveNewSeprateIsPriClaimDetails"
update_user_claim_url = "https://fasalrin.gov.in/application/updateNewSeprateIsPriClaimWorkflowStatus"

def getDaysBetweenDate(date1, date2):
    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    return float((date2 - date1).days)

def calculateISAmount(amt, startdate, enddate):
    return round((amt * 1.5 / 100) / 366 * getDaysBetweenDate(startdate, enddate), 2)

def generate_random_hex(length):
    # Generate a random hexadecimal string of the specified length
    return secrets.token_hex(length // 2)

# Read and parse the JSON file
with open('E:\\Personal_Development\\Personal_Development\\Projects\\ClaimApproval\\claims.json', 'r') as file:
    claims_list = json.load(file)

# Open a file to save the responses and logs
with open('E:\\Personal_Development\\Personal_Development\\Projects\\ClaimApproval\\response2.txt', 'w') as response_file:
    for claim in claims_list['data']['list']:
        try:
            loanFinancialDetailsID = claim['loanFinancialDetailsID']
            response_file.write(f"Processing loanFinancialDetailsID: {loanFinancialDetailsID}\n")
            response_file.write("Name:" + claim['beneficiaryName'] + "\n")
            response_file.write("Mobile:" + claim['mobile'] + "\n")
            response_file.write("Account Number:" + claim['accountNumber'] + "\n")
            response_file.write("Application Number:" + claim['applicationNo'] + "\n")
            headers = {'Cookie': 'connect.sid=s%3A6EgUU7EkG0RH-erfn-9IM2QiVMgf2Cam.zdM14jrdAKoMEDNUNafCN20hIDNKYnOj2ePNMtB9CiU','Content-Type': 'application/json'}
            
            # Make the API call to get claim user details
            claim_user_response = requests.get(get_claim_user_url + loanFinancialDetailsID, headers=headers)
            claim_user_response.raise_for_status()  # Raise an error for bad status codes
            claim_user_response_output = claim_user_response.json()
            response_file.write(f"Claim user details: {json.dumps(claim_user_response_output, indent=4)}\n")
            claim_user_activity = claim_user_response_output['data']['activityDetails']
            print("ActivityID Response:", claim_user_response_output['data']['activityDetails'][0]['activityTypeID'])

            # Generate a random hex ID of length 36
            random_hex_id = generate_random_hex(36)

            save_user_claims_payload = json.dumps({
                "data": {
                    "financialYear": "2023-2024",
                    "loanFinancialDetailsID": loanFinancialDetailsID,
                    "activityDetails": [
                        {
                            "activityTypeID": claim_user_response_output['data']['activityDetails'][0]['activityTypeID'],
                            "eligibleLoanAmount": float(claim_user_response_output['data']['activityDetails'][0]['loanSanctionedAmount']),
                            "loanSanctionedAmount": float(claim_user_response_output['data']['activityDetails'][0]['loanSanctionedAmount']),
                            "loanSanctionedDate": claim_user_response_output['data']['activityDetails'][0]['loanSanctionedDate'],
                            "maxEligibleLoanAmount": 300000
                        }
                    ],
                    "applicationNo": claim['applicationNo'],
                    "beneficiaryName": claim['beneficiaryName'],
                    "accountNumber": claim['accountNumber'],
                    "mobile": claim['mobile'],
                    "drawingLimit": claim_user_response_output['data']['drawingLimit'],
                    "earliestLoanSanctionedDate": claim_user_response_output['data']['activityDetails'][0]['loanSanctionedDate'],
                    "sumLoanSanctionedAmount": float(claim_user_response_output['data']['activityDetails'][0]['loanSanctionedAmount']),
                    "eligibleForIS": 1,
                    "loanDisbursalDate": claim_user_response_output['data']['activityDetails'][0]['loanSanctionedDate'],
                    "loanClosureDate": "2024-03-31",
                    "maxWithdrawalAmount": float(claim_user_response_output['data']['activityDetails'][0]['loanSanctionedAmount']),
                    "maxAllowedISAmount": calculateISAmount(float(claim_user_response_output['data']['activityDetails'][0]['loanSanctionedAmount']), claim_user_response_output['data']['activityDetails'][0]['loanSanctionedDate'], "2024-03-31"),
                    "applicableISAmount": calculateISAmount(float(claim_user_response_output['data']['activityDetails'][0]['loanSanctionedAmount']), claim_user_response_output['data']['activityDetails'][0]['loanSanctionedDate'], "2024-03-31"),
                    "priSubmissionTypeName": "COMPLETE",
                    "priSubmissionTypeID": 1,
                    "claimType": 1,
                    "financialDetailsID": claim_user_response_output['data']['financialDetailsID'],
                    "beneficiaryID": claim_user_response_output['data']['beneficiaryID'],
                    "messageID": random_hex_id
                }
            })
            print("Save Claim Payload:", save_user_claims_payload)

            # Make the API call to save user claims
            save_claim_response = requests.post(save_claim_user_url, headers=headers, data=save_user_claims_payload)
            save_claim_response.raise_for_status()  # Raise an error for bad status codes
            save_claim_response_output = save_claim_response.json()
            response_file.write(f"Save claim response: {json.dumps(save_claim_response_output, indent=4)}\n")
            print("Save Claim Response Successful")
            print(save_claim_response_output)

            submit_claim_payload = json.dumps({
                "data": {
                    "financialYear": "2023-2024",
                    "claimID": save_claim_response_output['data'] ['claimID'],
                    "actionType": "SUBMIT",
                    "claimType": save_claim_response_output['data']['claimType']
                }
            })

            # Make the API call to submit the claim
            submit_claim_response = requests.put(update_user_claim_url, headers=headers, data=submit_claim_payload)
            submit_claim_response.raise_for_status()  # Raise an error for bad status codes
            print("Submit Claim Response Successful")
            response_file.write(f"Submit claim response: {submit_claim_response.text}\n")
            response_file.write('-----------------------------------\n')
            response_file.write('*************************************************\n')
            response_file.write('-----------------------------------\n')
            response_file.write('\n')
            response_file.write('\n')
            response_file.write('\n')

        except requests.exceptions.RequestException as e:
            print("Error processing loanFinancialDetailsID", loanFinancialDetailsID, ":", e)
            response_file.write(f"Error processing loanFinancialDetailsID {loanFinancialDetailsID}: {e}\n")
            response_file.write('-----------------------------------\n')
            raise  # Re-raise the caught exception
        except Exception as e:
            print("Unexpected error processing loanFinancialDetailsID", loanFinancialDetailsID, ":", e)
            response_file.write(f"Unexpected error processing loanFinancialDetailsID {loanFinancialDetailsID}: {e}\n")
            response_file.write('-----------------------------------\n')
            # raise  # Re-raise the caught exception