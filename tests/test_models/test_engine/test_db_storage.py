import unittest
import os
from models import storage
from models.user import User
from models.state import State
from models.city import City


class TestDBStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Se ejecuta una vez al comienzo de todas las pruebas"""
        # Configura la variable de entorno para usar la base de datos de prueba
        os.environ['HBNB_ENV'] = 'test'
        os.environ['HBNB_MYSQL_USER'] = 'your_db_user'
        os.environ['HBNB_MYSQL_PWD'] = 'your_db_password'
        os.environ['HBNB_MYSQL_HOST'] = 'localhost'
        os.environ['HBNB_MYSQL_DB'] = 'your_test_db'

    @classmethod
    def tearDownClass(cls):
        """Se ejecuta una vez al finalizar todas las pruebas"""
        # Elimina las variables de entorno de prueba
        del os.environ['HBNB_ENV']
        del os.environ['HBNB_MYSQL_USER']
        del os.environ['HBNB_MYSQL_PWD']
        del os.environ['HBNB_MYSQL_HOST']
        del os.environ['HBNB_MYSQL_DB']

    def setUp(self):
        """Se ejecuta antes de cada prueba"""
        # Crea una instancia de DBStorage
        self.storage = storage.DBStorage()
        # Crea un objeto User de prueba
        self.user = User(email='test@example.com', password='password')
        # Inicializa la sesión de la base de datos
        self.storage.reload()

    def tearDown(self):
        """Se ejecuta después de cada prueba"""
        # Elimina el objeto de prueba de la base de datos
        self.storage.delete(self.user)
        # Limpia la sesión de la base de datos
        self.storage.save()
        self.storage.reload()

    def test_new(self):
        """Prueba el método new"""
        # Agrega el objeto User a la sesión de la base de datos
        self.storage.new(self.user)
        # Verifica que el objeto esté en la sesión
        self.assertIn(self.user, self.storage._DBStorage__session)

    def test_save(self):
        """Prueba el método save"""
        # Agrega el objeto User a la sesión de la base de datos
        self.storage.new(self.user)
        # Guarda los cambios en la base de datos
        self.storage.save()
        self.storage.reload()
        # Busca el objeto User en la sesión después de guardar
        user_from_db = self.storage.get(User, self.user.id)
        self.assertEqual(user_from_db, self.user)


if __name__ == '__main__':
    unittest.main()
