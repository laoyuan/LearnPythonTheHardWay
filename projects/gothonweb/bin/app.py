import web

urls = (
    '/', 'index',
    '/upload', 'upload',
    '/(.*)', 'hello'
)

app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")

class index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        if form.greet:
            greeting = "%s, %s" % (form.greet, form.name)
        else:
            greeting = "ERROR: greet is required."
        return render.index(greeting = greeting)


class upload(object):
    def POST(self):
        form = web.input(file={})
        target = open(form.file.filename, 'w')
        target.truncate()
        target.write(form.file.file.read())
        target.close()

        file_str = "%s saved." % (form.file.filename)

        return render.upload(file_str = file_str)


class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return render.hello(name = name)


if __name__ == "__main__":
    app.run()

