import requests
import json

def eth_syncing(url):
	headers = {'content-type': 'application/json'}
	payload = {
		"jsonrpc": "2.0",
		"method": "eth_syncing",
		"params": [],
		"id": 0
	}
	response = requests.post(url, data=json.dumps(payload), headers=headers).json()
	print("--eth_syncing---")
	print(response)
	if response["result"]:
		f=int(response["result"]["startingBlock"],16)
		g=int(response["result"]["knownStates"],16)
		h=int(response["result"]["pulledStates"],16)
		i=int(response["result"]["currentBlock"],16)
		j=int(response["result"]["highestBlock"],16)
		print("startingBlcok:",f)
		print("knownStates:",g)
		print("pulledStates:",h)
		print("currentBlock:",i)
		print("highestBlock:",j)

def eth_getBalance(url,addr):
	headers = {'content-type': 'application/json'}
	payload = {
		"jsonrpc": "2.0",
	    "method": "eth_getBalance",
		"params": [addr,"latest"],
		"id": 0
	}
	response = requests.post(url, data=json.dumps(payload), headers=headers).json()
	print("--eth_getBalance---")
	print(response)
	i=int(response["result"],16)
	print("getBalance:",i)

def net_peerCount(url):
	headers = {'content-type': 'application/json'}
	payload = {
		"jsonrpc": "2.0",
	        "method": "net_peerCount",
	        "params": [],
		"id": 0
	}
	print("--eth_peerCount---")
	response = requests.post(url, data=json.dumps(payload), headers=headers).json()
	print(response)
	i=int(response["result"],16)
	print("peerCount:",i)

def eth_coinbase(url):
	headers = {'content-type': 'application/json'}
	payload = {
		"jsonrpc": "2.0",
		"method": "eth_coinbase",
	    "params": [],
		"id": 0
	}
	print("--eth_coinbase---")
	response = requests.post(url, data=json.dumps(payload), headers=headers).json()
	print(response["result"])

def eth_hashrate(url):

	headers = {'content-type': 'application/json'}
	payload = {
		"jsonrpc": "2.0",
		"method": "eth_hashrate",
	    "params": [],
		"id": 0
	}
	print("--eth_hashrate---")
	response = requests.post(url, data=json.dumps(payload), headers=headers).json()
	print(response["result"])

def eth_blockNumber(url):
	headers = {'content-type': 'application/json'}
	payload = {
		"jsonrpc": "2.0",
		"method": "eth_blockNumber",
	    "params": [],
		"id": 0
	}
	print("--eth_blocknumber---")
	response = requests.post(url, data=json.dumps(payload), headers=headers).json()
	i=int(response["result"],16)
	print(response)
	print("eth_blockNumber:",i)

if __name__ == "__main__":
	url = "http://localhost:8545"
	eth_syncing(url)
	eth_getBalance(url,"<MYWALLET>")
	eth_getBalance(url,"<MYWALLET>")
	net_peerCount(url)
	eth_coinbase(url)
	eth_blockNumber(url)
