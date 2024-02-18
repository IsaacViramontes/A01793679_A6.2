"""Modulo para creacion de reservaciones con clase Reservation"""

import json
import os

class Reservation:
    """Clase Reservation para las reservaciones de un hotel"""

    def __init__(self, reservation_id, customer_id, hotel_name, room):
        """Metodo de inicializacion"""
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_name = hotel_name
        self.room = room
        self.filename = f"reservation_{reservation_id}.json"

    def save_file(self):
        """Metodo para salvar reservacion en archivo json"""
        info = {
            'reservation_id': self.reservation_id,
            'customer_id': self.customer_id,
            'hotel_name': self.hotel_name,
            'room': self.room
        }
        with open(self.filename, 'w', encoding = 'utf-8') as f:
            json.dump(info, f)

    #pylint: disable=no-self-argument
    def create_reservation(reservation_id, customer_id, hotel_name, room):
        """Metodo para creacion de reservacion"""
        reservation = Reservation(reservation_id, customer_id, hotel_name, room)
        reservation.save_file()
        return reservation

    def delete_reservation(reservation_id):
        """Metodo para eliminar archivo de reservacion"""
        filename = f"reservation_{reservation_id}.json"
        os.remove(filename)
