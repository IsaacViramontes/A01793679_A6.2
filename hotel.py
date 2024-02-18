"""Modulo para creacion de hoteles con clase Hotel"""

import json
import os

class Hotel:
    """Clase Hotel para los hoteles disponibles"""

    def __init__(self, name, rating, rooms):
        """Metodo de inicializacion"""
        self.name = name
        self.rating = rating
        self.rooms = rooms
        self.filename = f"hotel_{name}.json"

    def save_file(self):
        """Metodo para guardar hotel en archivo json"""
        info = {
            'name': self.name,
            'rating': self.rating,
            'rooms': self.rooms
        }
        with open(self.filename, 'w', encoding = 'utf-8') as f:
            json.dump(info, f)

    #pylint: disable=no-self-argument
    def create_hotel(name, rating, rooms):
        """Metodo para creacion de hotel"""
        hotel = Hotel(name, rating, rooms)
        hotel.save_file()
        return hotel

    def load_hotel(name):
        """Metodo para la carga de hotel desde archivo json"""
        filename = f"hotel_{name}.json"
        with open(filename, 'r', encoding = 'utf-8') as f:
            info = json.load(f)

        hotel_name = info['name']
        rating = info['rating']
        rooms = info['rooms']

        return Hotel(hotel_name, rating, rooms)

    def delete_hotel(name):
        """Metodo para eliminar archivo de hotel"""
        filename = f"hotel_{name}.json"
        os.remove(filename)

    def display_hotel(self):
        """Metodo para visualzar informacion del hotel"""
        name = self.name
        rating = self.rating
        rooms = self.rooms

        #pylint: disable=line-too-long
        print(f"""Hotel: {name}, Stars: {rating}, Rooms: {rooms}""")

    def update_hotel(self, name = None, rating = None):
        """Metodo para actualizar informacion del cliente"""
        if name:
            self.name = name
        if rating:
            self.rating = rating
        self.save_file()

    def reserve_room(self, room_id):
        """Metodo para reservar cuarto si esta disponible"""
        available = self.rooms.get(room_id)
        if available:
            self.rooms[room_id] = False

    def cancel_reservation(reservation_id):
        """Metodo para eliminar archivo de reservacion"""
        filename = f"reservation_{reservation_id}.json"
        os.remove(filename)
