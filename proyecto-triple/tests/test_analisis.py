import unittest
from app import create_app, db
from app.analisis.models import AnalysisData  # Assuming there's a model for analysis data

class AnalysisTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_analysis_data_creation(self):
        # Example test for creating analysis data
        data = AnalysisData(field1='value1', field2='value2')  # Adjust fields as necessary
        db.session.add(data)
        db.session.commit()
        self.assertIsNotNone(data.id)

    def test_analysis_data_retrieval(self):
        # Example test for retrieving analysis data
        data = AnalysisData(field1='value1', field2='value2')
        db.session.add(data)
        db.session.commit()
        retrieved_data = AnalysisData.query.get(data.id)
        self.assertEqual(retrieved_data.field1, 'value1')

    def test_analysis_data_deletion(self):
        # Example test for deleting analysis data
        data = AnalysisData(field1='value1', field2='value2')
        db.session.add(data)
        db.session.commit()
        db.session.delete(data)
        db.session.commit()
        self.assertIsNone(AnalysisData.query.get(data.id))

if __name__ == '__main__':
    unittest.main()