# test_app.py

from website import create_app
from flask_sqlalchemy import SQLAlchemy
import unittest

db = SQLAlchemy()

app = create_app()

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app_ctxt = self.app.app_context()
        self.app_ctxt.push()

    def tearDown(self):
        self.app_ctxt.pop()
        self.app = None
        self.app_ctxt = None

    def test_app(self):
        assert self.app is not None
        assert app == self.app


class TestProductModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the test environment (create tables, etc.)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory SQLite for testing
        db.init_app(app)
        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Clean up the test environment (remove tables, etc.)
        with app.app_context():
            db.drop_all()

    def setUp(self):
        # Create sample products for each test
        with app.app_context():
            self.test_product = Product(
                name="TestProduct1",
                quantity=10,
                price=25.0
            )
            db.session.add(self.test_product)

            self.test_product2 = Product2(
                name="TestProduct2",
                quantity=20,
                price=30.0
            )
            db.session.add(self.test_product2)

            db.session.commit()

    def tearDown(self):
        # Remove sample products after each test
        with app.app_context():
            db.session.delete(self.test_product)
            db.session.delete(self.test_product2)
            db.session.commit()

    def test_create_product(self):
        # Test creating a product
        with app.app_context():
            new_product = Product(
                name="NewProduct1",
                quantity=15,
                price=10.0
            )
            db.session.add(new_product)
            db.session.commit()
            retrieved_product = Product.query.filter_by(name="NewProduct1").first()
            self.assertIsNotNone(retrieved_product)

    def test_read_product(self):
        # Test reading product data
        with app.app_context():
            retrieved_product = Product.query.filter_by(name="TestProduct1").first()
            self.assertEqual(retrieved_product.quantity, 10)

    def test_update_product(self):
        # Test updating product data
        with app.app_context():
            self.test_product.quantity = 50
            db.session.commit()
            updated_product = Product.query.filter_by(name="TestProduct1").first()
            self.assertEqual(updated_product.quantity, 50)

    def test_delete_product(self):
        # Test deleting product
        with app.app_context():
            db.session.delete(self.test_product2)
            db.session.commit()
            deleted_product = Product2.query.filter_by(name="TestProduct2").first()
            self.assertIsNone(deleted_product)