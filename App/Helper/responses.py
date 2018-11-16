from flask import jsonify

class responses:

	Taxcode = {	1: {
					"name": "Food",
					"refund": True,
					"tax": 0.10
				}, 
				2: {
					"name": "Tobacco",
					"refund": False,
					"tax": 0.02
				}, 
				3: {
					"name": "Entertainment",
					"refund": False,
					"tax": 0.01
				}
			}
	

	def data_structure(alldata):
		response = []

		for value in alldata:
			taxcode = responses.Taxcode[value.tax_code]
			tax = sum_tax(value.price, taxcode, value.tax_code)
			amount = tax + value.price
			
			if tax == 0:
				tax = "tax-free"
			i = {
				"id": value.id,
				"name": value.name,
				"tax_code": value.tax_code,
				"type": taxcode['name'],
				"refundable": taxcode['refund'],
				"price": value.price,
				"tax": tax,
				"amount": amount
			}
			response.append(i)
		return jsonify({"data": response, 
						"status": True,
						"message": "Success"
					})


	def one_data(res):
		print(res.name)
		taxcode = responses.Taxcode[res.tax_code]
		tax = sum_tax(res.price, taxcode, res.tax_code)
		amount = tax + res.price
		if tax == 0:
			tax = "tax-free"
		response = {
			"id": res.id,
			"name": res.name,
			"tax_code": res.tax_code,
			"type": taxcode['name'],
			"refundable": taxcode['refund'],
			"price": res.price,
			"tax": tax,
			"amount": amount
		}
		return jsonify({"status": True,
					"message": "",
					"data": response
				})



def sum_tax(price, taxcode, taxcode_id):
	tax = ""
	if taxcode_id == 1:
		tax = price * taxcode['tax']
	elif taxcode_id == 2:
		tax = 10 + (taxcode['tax'] * price)
	elif taxcode_id == 3:
		if 0 < price and price < 100:
			tax = 0
		elif price >= 100:
			tax = price - 100
			tax = tax * taxcode['tax']

	return tax
