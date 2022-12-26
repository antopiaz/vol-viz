import aiohttp_jinja2
from aiohttp.web import View, Response, HTTPFound
from pathlib import Path
from .roundvolumes import roundVolumes


@aiohttp_jinja2.template('input_volume.html')
async def index(request):
    return {}

@aiohttp_jinja2.template('login.html')
async def login(request):

    if request.method == 'POST':
        form = await request.post()
        voloz=form['volumeoz']
        volml=form['volumeml']
        if voloz:
            ml=round(float(voloz)*29.574,2)
            vol=float(voloz) 
        elif volml and not voloz:
            vol=round(float(volml)/29.574,2)
            ml=float(volml)
        if len(voloz) or len(volml):
            if vol == 0.0 or vol >48:
                answer_size=0
                answers=[]
            else:
                answers=roundVolumes(vol,0)
                answer_size=len(answers)
            context = {
            'vol': vol,
            'ml': ml,
            'imgname': f"{vol}oz.jpg",
            'count': answer_size,
            'answers':answers,
            }
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
'''
def roundVolumes(inputVolume, units):
    
    mlList = [30,59,89,118,148,177,207,237,296,355,473,532]
    ozList = [1,2,3,4,5,6,7,8,10,12,16,18,20,24]

    unitsArr = [ozList, mlList]
       
    answers = [0,0]           
    
    for i in range(len(ozList)):
        if inputVolume == unitsArr[units][i]:
            answers = [1,i]
            return answers
           
    
    for i in range(len(ozList)):
        
        
    
    
        if inputVolume%unitsArr[units][i] == 0:
            print("bruh")
            answers[0] = inputVolume/unitsArr[units][i]
            if answers[0]>4:
                continue                
            else:
                
                answers[1] = i
                return answers
                
                                                                                            
        elif inputVolume < unitsArr[units][i]:
                          
            answers[0] = 1
            if(i==0):
                                   
                answers[1] = i    
                return answers
                
            else:
                
                average = (unitsArr[units][i] + unitsArr[units][i-1])/2.0
                if(inputVolume >= average):
                    answers[1] = i
                else:
                    answers[1] = i-1                    
                return answers
                
                       
        elif inputVolume > 48:
            print("uh oh")
            answers[1]=12
            return answers
            
                               
    return answers
'''
