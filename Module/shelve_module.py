import shelve

d = shelve.open('shelve_test')


print(d.get('seasons'))
print(d.get('pp'))

# seasons = ['spring', 'summer', 'autumn', 'winter']
#
# pp = {'temperature': 'comfy', 'special': 'flower'}
#
# d['seasons'] = seasons
# d['pp'] = pp


d.close()