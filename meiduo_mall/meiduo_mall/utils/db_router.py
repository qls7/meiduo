class MasterSlaveDBRouter(object):
    """数据库读写路由"""

    def db_for_read(self, model, **hints):
        """
        读所使用的服务器
        :param model:
        :param hints:
        :return:
        """
        return 'slave'

    def db_for_write(self, model, **hints):
        """
        写所用的服务器
        :param model:
        :param hints:
        :return:
        """
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        是否运行关联操作
        :param obj1:
        :param obj2:
        :param hints:
        :return:
        """
        return True
