from unittest import TestCase
import unittest
import pymssql 
import xmlrunner
import io

conn = pymssql.connect(server="LENA\\sqlexpress",  user="sa", password="sa", database='AdventureWorks2012')
cursor = conn.cursor()

out = io.BytesIO()

class TryTesting(TestCase):
    def test_city_count(self):
        cursor.execute('SELECT COUNT(DISTINCT [City]) AS city_count FROM [Person].[Address];')
        value = cursor.fetchone()
        self.assertTrue(value[0] == 575)

    def test_max_year(self):
        cursor.execute('SELECT MAX(YEAR([ModifiedDate])) AS max_year FROM [Person].[Address]')
        value = cursor.fetchone()
        self.assertTrue(value[0] <= 2023)

    def test_count_without_file_extension(self):
        cursor.execute('SELECT COUNT(*) AS count_without_file_extension FROM [Production].[Document] WHERE len(FileExtension) = 0;')
        value = cursor.fetchone()
        self.assertTrue(value[0] == 0)

    def test_count_unnormal_level(self):
        cursor.execute('SELECT COUNT(*) AS count_unnormal_level FROM [Production].[Document] WHERE [DocumentLevel] > 2;')
        value = cursor.fetchone()
        self.assertTrue(value[0] == 0)

    def test_count_incorrect_code(self):
        cursor.execute('SELECT COUNT(*) AS count_incorrect_code FROM [Production].[UnitMeasure] WHERE SUBSTRING ([UnitMeasureCode] ,0 , 1) <> SUBSTRING ([Name],0 , 1);')
        value = cursor.fetchone()
        self.assertTrue(value[0] == 0)

    def test_rows_count(self):
        cursor.execute('SELECT COUNT(*) AS rows_count FROM [Production].[UnitMeasure];')
        value = cursor.fetchone()
        self.assertTrue(value[0] == 38)
        
if __name__ == '__main__':
    with open('test-reports.xml', 'wb') as output:
        runner = unittest.runner.XMLTestRunner(output=output)
        unittest.main(testRunner=runner)
