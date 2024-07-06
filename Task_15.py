
class Material:
    def make(self):
        pass
    def use(self):
        pass


class MaterialContainer:
    pass

class EmptyMaterialContainer(MaterialContainer):
    pass

class PETContainer(MaterialContainer):
    pass

class GlassContainer(MaterialContainer):
    pass


class DisposableMaterial(Material):
    def __init__(self):
        self.container = EmptyMaterialContainer()

    def dispose(self):
        pass


class PET(DisposableMaterial): 
    def dispose(self):
        self.container = PETContainer()

class Glass(DisposableMaterial):
    def dispose(self):
        self.container = GlassContainer()


def disposableMaterialLifecycle(material:DisposableMaterial):
    material.make()
    material.use()
    material.dispose()

disposableMaterialLifecycle(PET())
disposableMaterialLifecycle(Glass())
