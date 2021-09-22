from flask_appbuilder import BaseView, expose, has_access
from . import appbuilder


class MyView(BaseView):
    default_view = 'method1'

    @expose("/method1/")
    @has_access
    def method1(self):
        return "Hello"

    @expose("/method2/<string:param1>")
    @has_access
    def method2(self, param1):
        param1 = "Goodbye %s" % (param1)
        return param1

    @expose("/method3/<string:param1>")
    @has_access
    def method3(self, param1):
        param1 = 'Method3 %s' % (param1)
        self.update_redirect()
        return self.render_template('method3.html', param1=param1)


appbuilder.add_view(MyView, "Method1", category='My View')
appbuilder.add_link("Method2", href='/myview/method2/john', category='My View')
appbuilder.add_link("Method3", href='/myview/method3/john', category='My View')