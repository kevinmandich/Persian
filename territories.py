__all__ = ['Territory','territories']

class Territory(object):
  '''
  A territory object is a node in the Map graph.
  '''

  def __init__(self, name, type_, supplies, castles, consolidation, port, \
               adjacent_port, garrison, owner, neighbors, footmen, cavalry, \
               siege, ships, portShips):

    self.name           = name          # string
    self.type           = type_         # string
    self.supplies       = supplies      # int
    self.castles        = castles       # int
    self.consolidation  = consolidation # int
    self.port           = port          # int
    self.adjacent_port  = adjacent_port  # int
    self.garrison       = garrison      # int
    self.owner          = owner         # string (None)
    self.neighbors      = neighbors     # list
    self.footmen        = footmen       # int
    self.cavalry        = cavalry       # int
    self.siege          = siege         # int
    self.ships          = ships         # int
    self.portShips      = portShips     # int

territories = [ \
Territory(name='Bay of Ice', \
          type_='sea', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=1, \
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
          adjacent_port=0, \
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
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Bay of Ice','The Stony Shore','Castle Black','Karhold','White Harbor','The Shivering Sea','Moat Cailin'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Karhold', \
          type_='land', \
          supplies=0, \
          castles=0, \
          consolidation=1, \
          port=0, \
          adjacent_portv=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Winterfell','Castle Black','The Shivering Sea'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='The Shivering Sea', \
          type_='sea', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Castle Black','Karhold','Winterfell','White Harbor','Widows Watch','The Narrow Sea'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='White Harbor', \
          type_='land', \
          supplies=0, \
          castles=1, \
          consolidation=0, \
          port=1, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Winterfell','Moat Cailin','Widows Watch','The Shivering Sea','The Narrow Sea'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Widows Watch', \
          type_='land', \
          supplies=1, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['White Harbor','The Shivering Sea','The Narrow Sea'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='The Stony Shore', \
          type_='land', \
          supplies=1, \
          castles=1, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Bay of Ice','Winterfell'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Sunset Sea', \
          type_='land', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Bay of Ice','West Summer Sea','Ironmans Bay','The Golden Sound','Flints Finger','Searoad Marches'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Flints Finger', \
          type_='land', \
          supplies=0, \
          castles=1, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Bay of Ice','Sunset Sea','Ironmans Bay','Greywater Watch'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Greywater Watch', \
          type_='land', \
          supplies=1, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Bay of Ice','Flints Finger','Ironmans Bay','Seagard','Moat Cailin'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Moat Cailin', \
          type_='land', \
          supplies=0, \
          castles=1, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Greywater Watch','Seagard','The Twins','The Narrow Sea','White Harbor','Winterfell'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Ironmans Bay', \
          type_='sea', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=1, \
          garrison=0, \
          owner=None, \
          neighbors=['Sunset Sea','The Golden Sound','Riverrun','Seagard','Greywater Watch','Flints Finger'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Pike', \
          type_='land', \
          supplies=1, \
          castles=2, \
          consolidation=1, \
          port=1, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Ironmans Bay'] \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Seagard', \
          type_='land', \
          supplies=1, \
          castles=2, \
          consolidation=1, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Ironmans Bay','Riverrun','The Twins','Moat Cailin','Greywater Watch'] \
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
          adjacent_port=0, \
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
          adjacent_port=0, \
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







