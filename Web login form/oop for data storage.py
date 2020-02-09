class user():
    def __new__(cls, *args, **kwargs):
        print("New User!")
        instance = super(user, cls).__new__(cls, *args, **kwargs)
        return instance
    
    def __init__(self,name,pictures,feature):
        self._name = name
        self._pictures = [].append(pictures)
        self._features = [].append(feature)

    def get_name(self):
        return self._name
    
    def get_pictures(self):
        return self._pictures
    
    def get_feature_list(self):
        return self._features
    
    def add_feature(self,new_image,feature_list):
       self._pictures.append(new_image)
       self._features.append(feature_list)

    