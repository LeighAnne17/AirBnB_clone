import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        json_dict = {}
        for key, obj in self.__objects.items():
            json_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                json_dict = json.load(f)
                for key, val in json_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    obj = cls(**val)
                    self.new(obj)
        except FileNotFoundError:
            pass
