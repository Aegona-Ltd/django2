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

    def update(self, object, **kwargs):
        object.update(**kwargs)
        object.save()
        return object

    def delete(self, object):
        try:
            object.delete()
            return object
        except:
            return False

    def getAllOrderByIdDesc(self):
        return self.model.objects.order_by("-id").all()
