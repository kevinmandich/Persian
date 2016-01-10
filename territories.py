__all__ = ['Territory','territories']

class Territory(object):
  '''
  A territory object is a node in the Map graph.
  '''

  def __init__(self, name, type_, supplies, castles, consolidation, port, \
               adjacentPort, garrison, owner, neighbors, footmen, cavalry, \
               siege, ships, portShips):

    self.name          = name          # string
    self.type          = type_         # string
    self.supplies      = supplies      # int
    self.castles       = castles       # int
    self.consolidation = consolidation # int
    self.port          = port          # int
    self.adjacentPort  = adjacentPort  # int
    self.garrison      = garrison      # int
    self.owner         = owner         # string (None)
    self.neighbors     = neighbors     # list
    self.footmen       = footmen       # int
    self.cavalry       = cavalry       # int
    self.siege         = siege         # int
    self.ships         = ships         # int
    self.portShips     = portShips     # int

territories = [ \
Territory(name='Bay of Ice', \
          type_='sea', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacentPort=1, \
          garrison=0, \
          owner=None, \
          neighbors=['Castle Black','Winterfell','The Stony Shore','Sunset Sea','Flints Finger','Greywater Watch'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Castle Black', \
          type_='land', \
          supplies=0, \
          castles=0, \
          consolidation=1, \
          port=0, \
          adjacentPort=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Bay of Ice','Winterfell','Karhold','The Shivering Sea'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Winterfell', \
          type_='land', \
          supplies=1, \
          castles=2, \
          consolidation=1, \
          port=1, \
          adjacentPort=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Bay of Ice','The Stony Shore','Castle Black','Karhold','White Harbor','The Shivering Sea','Moat Cailin'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Winterfell', \
          type_='land', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacentPort=0, \
          garrison=0, \
          owner=None, \
          neighbors=[] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Winterfell', \
          type_='land', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacentPort=0, \
          garrison=0, \
          owner=None, \
          neighbors=[] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Winterfell', \
          type_='land', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacentPort=0, \
          garrison=0, \
          owner=None, \
          neighbors=[] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Winterfell', \
          type_='land', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacentPort=0, \
          garrison=0, \
          owner=None, \
          neighbors=[] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Winterfell', \
          type_='land', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacentPort=0, \
          garrison=0, \
          owner=None, \
          neighbors=[] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Winterfell', \
          type_='land', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacentPort=0, \
          garrison=0, \
          owner=None, \
          neighbors=[] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
]







