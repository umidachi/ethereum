import requests
import json
import csv

#Json-rpcでeth_callを呼び出す
def eth_call(url,to,data):
	headers = {'content-type': 'application/json'}
	payload = {
		"jsonrpc": "2.0",
		"method": "eth_call",
		"params":[{"to":to,
				   "data":data},
				   "latest"],
		"id": 0
	}

	response = requests.post(url, data=json.dumps(payload), headers=headers).json()
	print(response)
	return response['result']

def numBets():
	contract_address={"vdice":"0x7DA90089A73edD14c75B0C827cb54f4248D47eCc"}
	numBets_abi="0xdf06f906"
	result=eth_call(url,contract_address['vdice'],numBets_abi)
	i=int(result,16)
	return i

def getBet(bet_id):
	contract_address={"vdice":"0x7DA90089A73edD14c75B0C827cb54f4248D47eCc"}
	b="0x061e494f" #getBet(uint256)
	d="{0:064x}".format((bet_id))
	getBet_abi=b+d
	print(getBet_abi)
	result=eth_call(url,contract_address['vdice'],getBet_abi)

	d=result[2:194]	   #先頭0xの表記を省略
	#print(d)
	playerAddress=d[24:64]
	#print("PlayerAddress:",playerAddress)
	AmountBet=int(d[64:128],16)
	#print("AmountBet:",AmountBet)
	numRoll=int(d[129:193],16)
	#print("numRoll:",numRoll)

	return(bet_id,playerAddress,AmountBet,numRoll)

if __name__ == "__main__":
	url = "http://localhost:8545"
	betnum=numBets()

	f = open('output_.csv', 'a')
	writer = csv.writer(f, lineterminator='\n') 

	print("---betnum:",betnum)
	for i in range(1553,betnum):#
		n=getBet(i-1)
		print(n[0],n[1],n[2],n[3])
		writer.writerow(n)    

	f.close()
