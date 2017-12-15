import requests
import json


def eth_call(url):
	headers = {'content-type': 'application/json'}
	payload = {
		"jsonrpc": "2.0",
		"method": "eth_call",
		"params":[{"to":"0x48c80F1f4D53D5951e5D5438B54Cba84f29F32a5",
				   "data":"0x70a08231000000000000000000000000<Mywallet>"},
				   "latest"],
		"id": 0
	}
	print("Token Balance")
	response = requests.post(url, data=json.dumps(payload), headers=headers).json()
	i=int(response["result"],16)
	i=i/pow(10,18)
	print(response)
	print("eth_blockNumber:",i)
if __name__ == "__main__":
	url = "http://localhost:8545"
	eth_call(url)
