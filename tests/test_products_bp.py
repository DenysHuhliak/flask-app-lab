import unittest
from app import app

class ProductsBPTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_list(self):
        """Перевірка сторінки зі списком продуктів"""
        r = self.client.get("/products")
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"Laptop", r.data)
        self.assertIn(b"Phone", r.data)
        self.assertIn(b"PC", r.data)

    def test_detail_ok(self):
        """Перевірка сторінки одного продукту"""
        r = self.client.get("/product/1")
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"Laptop", r.data)
        self.assertIn(b"Product", r.data)

    def test_detail_not_found(self):
        """Перевірка помилки 404 для неіснуючого ID"""
        r = self.client.get("/product/999")
        self.assertEqual(r.status_code, 404)

if __name__ == "__main__":
    unittest.main()