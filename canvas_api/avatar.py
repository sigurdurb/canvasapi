from canvas_api.canvas_object import CanvasObject


class Avatar(CanvasObject):

    def __str__(self):  # pragma: no cover
        return str(self.display_name)