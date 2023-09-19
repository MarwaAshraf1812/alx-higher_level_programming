#!/usr/bin/python3
"""
Defines unittests for base.py.
"""
import unittest
import os
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class test_pycodestyle(unittest.TestCase):
    "test that we conform to PEP-8"
    def test_checking(self):
        style = pycodestyle.StyleGuide(quit=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")
        print(result)

class test__init__(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_number_arg(self):
        """Test 'id' attribute incrementation in the 'Base' class."""
        base_1 = Base()
        base_2 = Base()
        self.assertEqual(base_1.id, base_2.id - 1)

    def test_three_bases(self):
        base_1 = Base()
        base_2 = Base()
        base_3 = Base()
        self.assertEqual(base_1.id, base_3.id - 2)

    def test_nb_instances_after_unique_id(self):
        base_1 = Base()
        base_2 = Base(20)
        base_3 = Base()
        self.assertEqual(base_1.id, base_3.id - 1)

    def test_None_id(self):
        """
        Tests that an id is not assigned to a 
        new instance if one isn't provided as input.
        """
        base_1 = Base(None)
        base_2 = Base(None)
        self.assertEqual(base_1.id, base_2.id - 1)

    def test_give_id(self):
        """
        Tests that an id can be given when instantiating 
        a new object from the Base Class.
        """
        base_r = Rectangle(10, 5, 6, 6, 90)
        base_s = Square(3, 5, 10, 200)
        base_t = Base(20)
        self.assertEqual(base_r.id, 90)
        self.assertEqual(base_s.id, 200)
        self.assertEqual(base_t.id, 20)

    def test_direct_id(self):
        """Tests that direct assignment of ids works correctly."""
        base_i = Base()
        base_i.id = 18
        self.assertEqual(base_i.id, 18)

    def test_string_id(self):
        """Tests that assigning string values """
        base = Square(8, 10, 4, "Test")
        self.assertEqual(base.id, "Test")

    def test_for_key(self):
        """Tests that assigning Keys and Values """
        base = Base()
        dict = {"key": "Value"}
        base.id = dict
        self.assertEqual(base.id, dict)
        
    def test_for_bool_T(self):
        """Tests that assigning boollen value"""
        Base = Square(2, 3, 4, True)
        self.assertEqual(Base.id, 1)

    def test_for_list(self):
        """Tests that assigning list"""
        base_list = [3, 4, 5, 6]
        base_o = Base(base_list)
        self.assertEqual(base_o.id, base_list)

    def test_for_set(self):
        """Tests that assigning set"""
        base_set = {2, 7, 4}
        base_o = Base(base_set)
        self.assertEqual(base_o.id, base_set)

    def test_for_tuble(self):
        """Tests that assigning Tuble"""
        base_tub = (1, 8, 2)
        base_o = Base(base_tub)
        self.assertEqual(base_o.id, base_tub)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

class Test_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        """Type comparison"""
        rect = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([rect.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        """Length comparison"""
        rect = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([rect.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        """convert string to json and return dict - Length comparison"""
        rect1 = Rectangle(2, 3, 5, 19, 2)
        rect2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [rect1.to_dictionary(), rect2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        """Type comparison"""
        seq = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([seq.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        """length comparison"""
        seq = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([seq.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        """convert string to json and return dict - Length comparison"""
        seq1 = Square(10, 2, 3, 4)
        seq2 = Square(4, 5, 21, 2)
        list_dicts = [seq1.to_dictionary(), seq2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        """Testing Empty List"""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        """Testing None Value"""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        """Testing Passing No Arguments"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        """Testing More Than One Arguments"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    def test_save_to_file_1rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_2rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_1square(self):
        seq = Square(10, 7, 2, 8)
        Square.save_to_file([seq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_2squares(self):
        seq1 = Square(10, 7, 2, 8)
        seq2 = Square(8, 1, 2, 3)
        Square.save_to_file([seq1, seq2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_fn(self):
        seq = Square(10, 7, 2, 8)
        Base.save_to_file([seq])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_ow(self):
        seq = Square(9, 2, 39, 2)
        Square.save_to_file([seq])
        seq = Square(10, 7, 2, 8)
        Square.save_to_file([seq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_1arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)

class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        seq1 = Square(5, 1, 3, 3)
        seq2 = Square(9, 5, 2, 3)
        Square.save_to_file([seq1, seq2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        seq1 = Square(5, 1, 3, 3)
        seq2 = Square(9, 5, 2, 3)
        Square.save_to_file([seq1, seq2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(seq2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        seq1 = Square(5, 1, 3, 3)
        seq2 = Square(9, 5, 2, 3)
        Square.save_to_file([seq1, seq2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        seq1 = Square(10, 7, 2, 8)
        seq2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([seq1, seq2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        seq = Square(10, 7, 2, 8)
        Base.save_to_file_csv([seq])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        seq = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        seq = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)

class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)

if __name__ == '__main__':
    unittest.TestCase()