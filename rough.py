def globe(func):
    print('this is inside globe function')
    def callone():
        func()
    return callone

@globe
def single():
    print('this is single function')

single()