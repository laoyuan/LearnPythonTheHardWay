import web

urls = (
    '/', 'index',
    '/(.*)', 'hello'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class index(object):
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)


class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return render.hello(name = name)


if __name__ == "__main__":
    app.run()

