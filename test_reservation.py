"""Modulo para UnitTest de modulo reservation"""

import unittest
import os
from reservation import Reservation

class TestReservation(unittest.TestCase):
    """Clase para realizar pruebas de Reservation"""
    def setUp(self):
        """Meotodo de setup"""
        self.reservation = Reservation(reservation_id = 'setup',
                                       customer_id = 'Cesar',
                                       hotel_name = 'Bugambilias',
                                       room = 404)

    def test_reservation_init(self):
        """Metodo de verificacion de iniciatilzacion"""
        self.assertEqual(self.reservation.reservation_id, 'setup')
        self.assertEqual(self.reservation.customer_id, 'Cesar')
        self.assertEqual(self.reservation.hotel_name, 'Bugambilias')
        self.assertEqual(self.reservation.room, 404)

    def test_create_reservation(self):
        """Metodo de verificacion de creacion de reservacion"""
        Reservation.create_reservation('create_test', 'Create', 'Holiday', 2)
        expected_filename = "reservation_create_test.json"
        self.assertTrue(os.path.exists(expected_filename), "Reservation file should exist")

        os.remove("reservation_create_test.json")

    def test_delete_reservation(self):
        """Metodo de verificacion de eliminacion de reservacion"""
        Reservation.create_reservation('delete_test', 'Delete', 'Hotel', 3)
        expected_filename = "reservation_delete_test.json"
        self.assertTrue(os.path.exists(expected_filename), "Reservation file should exist")

        Reservation.delete_reservation('delete_test')
        self.assertFalse(os.path.exists(expected_filename), "Reservation file should not exist")

    if __name__ == '__main__':
        unittest.main()
