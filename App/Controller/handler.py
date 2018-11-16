from flask import jsonify
from App.Model.data import data
from App.Helper.responses import responses
from main import db
from App.Model.data import data

class handler:

	def index(self):
		alldata = data.query.all()
		return responses.data_structure(alldata)

	def add(self):
		tax_code = tax_code_checker(self["tax_code"])

		if tax_code == False:
			return jsonify({"status": False, "message": "Tax code not found", "data": {}})
		else:
			response = input_process(self)
			return responses.one_data(response)

def tax_code_checker(tax_code):
	if tax_code in responses.Taxcode:
		status = True
	else:
		status = False

	return status


def input_process(req):
	data_ = data(req['name'], req['tax_code'], req['price'])
	#data_.price = req['price']
	#data_.tax_code = req['tax_code']
	#data_.name = req['name']
	db.session.add(data_)
	db.session.commit()
	return data_