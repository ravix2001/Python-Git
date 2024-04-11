capitals= {'USA':'Washington DC',
           'India':'New Delhi',
           'China':'Beijing',
           'Russia':'Moscow'}
#print(capitals.items())

capitals.update({'Nepal':'Kathmandu'})
print(capitals['USA'])
print(capitals['India'])
#print(capitals['Nepal'])   //Error
print(capitals.get('Nepal'))
#print(capitals.keys())
#print(capitals.values())