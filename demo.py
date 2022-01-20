def globe(func):
    print('this is inside globe function')
    def callone():
        func()
    return callone

@globe
def single():
    print('this is single function')

single()



#running flask app in terminal with 
    #export FLASK_APP=demo.py
    #export FLASK_ENV=development
    #export FLASK_DEBUG=1
    #flask run
    #  env/bin/activate& 
