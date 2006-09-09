import goocanvas

from home.DonutItem import DonutItem
from home.MyIcon import MyIcon

class TasksItem(DonutItem):
	def __init__(self, shell):
		DonutItem.__init__(self, 250)

		self._items = {}

		self._shell = shell
		self._shell.connect('activity_opened', self.__activity_opened_cb)
		self._shell.connect('activity_closed', self.__activity_closed_cb)

	def __activity_opened_cb(self, shell, activity):
		self._add(activity)

	def __activity_closed_cb(self, shell, activity):
		self._remove(activity)
	
	def _remove(self, activity):
		item = self._items[activity.get_id()]
		self.remove_piece(item)
		del self._items[activity.get_id()]

	def _add(self, activity):
		icon_name = activity.get_icon_name()
		icon_color = activity.get_icon_color()

		item = self.add_piece(100 / 8, icon_name, icon_color)
		item.get_icon().connect('clicked',
								self.__activity_icon_clicked_cb,
								activity)

		self._items[activity.get_id()] = item

	def __activity_icon_clicked_cb(self, item, activity):
		activity.present()

class HomeGroup(goocanvas.Group):
	def __init__(self, shell):
		goocanvas.Group.__init__(self)

		tasks = TasksItem(shell)
		tasks.translate(600, 450)
		self.add_child(tasks)

		me = MyIcon(150)
		me.translate(600 - (me.get_property('size') / 2),
					 450 - (me.get_property('size') / 2))
		self.add_child(me)
