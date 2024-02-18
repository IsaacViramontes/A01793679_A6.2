"""Modulo para creacion de clientes con clase Customer"""

import json
import os

class Customer:
    """Clase Customer para los clientes de un hotel"""

    def __init__(self, customer_id, first_name, last_name, phone):
        """Metodo de inicializacion"""
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.filename = f"customer_{customer_id}.json"

    def save_file(self):
        """Metodo para salvar cliente en archivo json"""
        info = {
            'customer_id': self.customer_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone
        }
        with open(self.filename, 'w', encoding = 'utf-8') as f:
            json.dump(info, f)

    #pylint: disable=no-self-argument
    def create_customer(customer_id, first_name, last_name, phone):
        """Metodo para creacion de cliente"""
        customer = Customer(customer_id, first_name, last_name, phone)
        customer.save_file()
        return customer

    def load_customer(customer_id):
        """Metodo para la carga de cliente desde archivo json"""
        filename = f"customer_{customer_id}.json"
        with open(filename, 'r', encoding = 'utf-8') as f:
            info = json.load(f)

        c_id = info['customer_id']
        first_name = info['first_name']
        last_name = info['last_name']
        phone = info['phone']

        return Customer(c_id, first_name, last_name, phone)

    def delete_customer(customer_id):
        """Metodo para eliminar archivo de cliente"""
        filename = f"customer_{customer_id}.json"
        os.remove(filename)

    def display_customer(self):
        """Metodo para visualzar informacion del cliente"""
        customer_id = self.customer_id
        first_name = self.first_name
        last_name = self.last_name
        phone = self.phone

        #pylint: disable=line-too-long
        print(f"""Customer ID: {customer_id}, First Name: {first_name}, Last Name: {last_name}, Phone Number: {phone}""")

    def update_customer(self, first_name = None, last_name = None, phone = None):
        """Metodo para actualizar informacion del cliente"""
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if phone:
            self.phone = phone
        self.save_file()
