import aiohttp_jinja2
from aiohttp.web import View, Response, HTTPFound
from pathlib import Path


@aiohttp_jinja2.template('input_volume.html')
async def index(request):
    return {}

@aiohttp_jinja2.template('login.html')
async def login(request):

    if request.method == 'POST':
        form = await request.post()
        #error = validate_login(form)
        voloz=form['volumeoz']
        volml=form['volumeml']
        if voloz:
            ml=round(float(voloz)*29.574,2)
            vol=voloz 
        elif volml and not voloz:
            vol=round(float(volml)/29.574,2)
            ml=volml
        error = 1
        len=2
        context = {
        'vol': vol,
        'ml': ml,
        'imgname': f"{vol}oz.jpg",
        'count': len
        }
        if vol:
            response = aiohttp_jinja2.render_template("display.html", request, context=context)
            return response
        else:
            # login form is valid
            location = request.app.router['index'].url_for()
            raise HTTPFound(location=location)

    return {}

async def handler(request):
    location = request.app.router['login'].url_for()
    raise HTTPFound(location=location)


#@aiohttp_jinja2.template('login.html')
#async def do_login(request):
#    data = await request.post()
#    volume = data['volume']
#    return Response(text=volume)

@aiohttp_jinja2.template('index.html')
async def index(request):
    data= await request.text()
    print('hello')
    #password = data
    #return Response(text=data)
    #return {}

class AddUserView(View):
    async def post(self):
        ### here I put data to the database
        print('example')
        return Response(text='Everything is ok!')

    async def get(self):
        response = await index(self.request)
        return response


