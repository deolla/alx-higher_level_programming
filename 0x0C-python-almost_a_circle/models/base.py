#!/usr/bin/python3

"""
This class will be the “base” of all other classes in this project.
"""
import json
import csv
import turtle


class Base:
    """
    This class is "base" of all classes in this project.

    Attribute:
        __nb_object: private class attribute.
        id:  public instance attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialise the "base" instance with an optional id.

        Args:
            id (int): This is a unique identifier of the base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns:
            returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries: a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs: a list of instances who inherits of Base.
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            json_string = cls.to_json_string([
                    obj.to_dictionary() for obj in list_objs
                ])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns:
            returns the list of the JSON string representation json_string.

        Args:
            json_string: a string representing a list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns:
            returns an instance with all attributes already set.

        Args:
            dictionary: a dictionary that contains a key/value.
        """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        else:
            new_instance = None

        if new_instance is not None:
            new_instance.update(**dictionary)

        return new_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns:
            returns a list of instances.
            If the file doesn’t exist, return an empty list.

        Raises:
            Execeptions: file not found
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes in CVS.

        Args:
            list_objs[list]: lists object.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes in CSV.

        Raises:
            Exceptions: file not found.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                instance = csv.DictReader(f, fieldnames=fieldnames)
                instance = [
                    dict([m, int(n)] for m, n in d.items())
                    for d in instance
                ]
                return [cls.create(**d) for d in instance]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares.

        Args:
            list_rectangles(list): A list of Rectangle objects.
            list_squares(list): A list of Square objects.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
                turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(4):
                turt.forward(sq.size)
                turt.left(90)
                turt.hideturtle()

        turtle.exitonclick()
