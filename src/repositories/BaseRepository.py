class BaseRepository:
    def __init__(self, model):
        self.model = model

    def getModel(self):
        return self.model

    def getAll(self):
        return self.model.objects.all()

    def getOne(self, **kwargs):
        return self.model.objects.filter(**kwargs).first()

    def filter(self, **kwargs):
        return self.model.objects.filter(**kwargs)

    def create(self, **kwargs):
        object = self.model(**kwargs)
        object.save()
        return object

    def update(self, *args, **kwargs):
        object = self.model.objects.filter(*args).first()
        for attr in kwargs.keys():
            setattr(object, attr, kwargs.get(attr))
        object.save()
        return object

    def delete(self, **kwargs):
        try:
            object = self.model.objects.filter(**kwargs).first()
            object.delete()
            return object
        except:
            return False

    def getAllOrderByIdDesc(self):
        return self.model.objects.order_by("-id").all()

    def deleteAll(self):
        return self.model.objects.all().delete()

    def bulkCreate(self, listObject):
        return self.model.objects.bulk_create(listObject)

