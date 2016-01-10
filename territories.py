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

base = [ \
Territory(name='Bay of Ice', \
          type_='sea', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=1, \
          garrison=0, \
          owner=None, \
          neighbors=['Castle Black','Winterfell','The Stony Shore','Sunset Sea','Flints Finger','Greywater Watch'], \
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
          neighbors=['Bay of Ice','Winterfell','Karhold','The Shivering Sea'], \
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
          neighbors=['Bay of Ice','The Stony Shore','Castle Black','Karhold','White Harbor','The Shivering Sea','Moat Cailin'], \
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
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Winterfell','Castle Black','The Shivering Sea'], \
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
          neighbors=['Castle Black','Karhold','Winterfell','White Harbor','Widows Watch','The Narrow Sea'], \
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
          neighbors=['Winterfell','Moat Cailin','Widows Watch','The Shivering Sea','The Narrow Sea'], \
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
          neighbors=['White Harbor','The Shivering Sea','The Narrow Sea'], \
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
          neighbors=['Bay of Ice','Winterfell'], \
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
          neighbors=['Bay of Ice','West Summer Sea','Ironmans Bay','The Golden Sound','Flints Finger','Searoad Marches'], \
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
          neighbors=['Bay of Ice','Sunset Sea','Ironmans Bay','Greywater Watch'], \
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
          neighbors=['Bay of Ice','Flints Finger','Ironmans Bay','Seagard','Moat Cailin'], \
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
          neighbors=['Greywater Watch','Seagard','The Twins','The Narrow Sea','White Harbor','Winterfell'], \
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
          neighbors=['Pike','Sunset Sea','The Golden Sound','Riverrun','Seagard','Greywater Watch','Flints Finger'], \
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
          neighbors=['Ironmans Bay'], \
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
          neighbors=['Ironmans Bay','Riverrun','The Twins','Moat Cailin','Greywater Watch'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='The Twins', \
          type_='land', \
          supplies=0, \
          castles=0, \
          consolidation=1, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Moat Cailin','Seagard','The Mountains of the Moon','The Fingers','The Narrow Sea'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='The Fingers', \
          type_='land', \
          supplies=1, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['The Twins','The Mountains of the Moon','The Narrow Sea'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='The Narrow Sea', \
          type_='sea', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=1, \
          garrison=0, \
          owner=None, \
          neighbors=['The Shivering Sea','Widows Watch','White Harbor','Moat Cailin','The Twins','The Fingers','The Mountains of the Moon','The Eyrie','Crackclaw Point','Shipbreaker Bay'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='The Mountains of the Moon', \
          type_='land', \
          supplies=1, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Crackclaw Point','The Narrow Sea','The Eyrie','The Fingers','The Twins'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='The Eyrie', \
          type_='land', \
          supplies=1, \
          castles=1, \
          consolidation=1, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['The Mountains of the Moon','The Narrow Sea'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='The Golden Sound', \
          type_='sea', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=1, \
          garrison=0, \
          owner=None, \
          neighbors=['Ironmans Bay','Sunset Sea','Searoad Marches','Lannisport','Riverrun'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Lannisport', \
          type_='land', \
          supplies=2, \
          castles=2, \
          consolidation=0, \
          port=1, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['The Golden Sound','Searoad Marches','Stoney Sept','Riverrun'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Stoney Sept', \
          type_='land', \
          supplies=0, \
          castles=0, \
          consolidation=1, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Lannisport','Searoad Marches','Blackwater','Harrenhal','Riverrun'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Riverrun', \
          type_='land', \
          supplies=1, \
          castles=2, \
          consolidation=1, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Ironmans Bay','The Golden Sound','Lannisport','Stoney Sept','Harrenhal','Seagard'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Harrenhal', \
          type_='land', \
          supplies=0, \
          castles=1, \
          consolidation=1, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Riverrun','Stoney Sept','Blackwater','Crackclaw Point'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Crackclaw Point', \
          type_='land', \
          supplies=0, \
          castles=1, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['The Mountains of the Moon','Harrenhal','Blackwater','Kings Landing','Blackwater Bay','Shipbreaker Bay','The Narrow Sea'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Blackwater Bay', \
          type_='sea', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Crackclaw Point','Kings Landing','Kingswood','Shipbreaker Bay'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Shipbreaker Bay', \
          type_='sea', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=1, \
          garrison=0, \
          owner=None, \
          neighbors=['Crackclaw Point','Blackwater Bay','Kingswood','Storms End','East Summer Sea','Dragonstone','The Narrow Sea'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Dragonstone', \
          type_='land', \
          supplies=1, \
          castles=2, \
          consolidation=1, \
          port=1, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Shipbreaker Bay'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Searoad Marches', \
          type_='land', \
          supplies=1, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['The Golden Sound','Sunset Sea','West Summer Sea','Highgarden','The Reach','Blackwater','Stoney Sept','Lannisport'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Blackwater', \
          type_='land', \
          supplies=2, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Searoad Marches','The Reach','Kings Landing','Crackclaw Point','Harrenhal','Stoney Sept'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Kings Landing', \
          type_='land', \
          supplies=0, \
          castles=2, \
          consolidation=2, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Crackclaw Point','Blackwater','The Reach','Kingswood','Blackwater Bay'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='West Summer Sea', \
          type_='sea', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Sunset Sea','Redwyne Straights','The Arbor','East Summer Sea','Starfall','Three Towers','Highgarden','Searoad Marches'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Redwyne Straights', \
          type_='sea', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=1, \
          garrison=0, \
          owner=None, \
          neighbors=['West Summer Sea','The Arbor','Highgarden','Oldtown','Three Towers'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='The Arbor', \
          type_='land', \
          supplies=0, \
          castles=0, \
          consolidation=1, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Redwyne Straights','West Summer Sea'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Highgarden', \
          type_='land', \
          supplies=2, \
          castles=2, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['West Summer Sea','Redwyne Straights','Oldtown','Dornish Marches','The Reach','Searoad Marches'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='The Reach', \
          type_='land', \
          supplies=0, \
          castles=1, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Searoad Marches','Highgarden','Dornish Marches','The Boneway','Kingswood','Kings Landing','Blackwater'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Kingswood', \
          type_='land', \
          supplies=1, \
          castles=0, \
          consolidation=1, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Kings Landing','The Reach','The Boneway','Storms End','Shipbreaker Bay','Blackwater Bay'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Storms End', \
          type_='land', \
          supplies=0, \
          castles=1, \
          consolidation=0, \
          port=1, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Kingswood','The Boneway','Sea of Dorne','East Summer Sea','Shipbreaker Bay'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Oldtown', \
          type_='land', \
          supplies=0, \
          castles=2, \
          consolidation=0, \
          port=1, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Redwyne Straights','Three Towers','Dornish Marches','Highgarden'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Dornish Marches', \
          type_='land', \
          supplies=0, \
          castles=0, \
          consolidation=1, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Highgarden','Oldtown','Three Towers','Princes Pass','The Boneway','The Reach'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='The Boneway', \
          type_='land', \
          supplies=0, \
          castles=0, \
          consolidation=1, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Sea of Dorne','Storms End','Kingswood','The Reach','Dornish Marches','Princes Pass','Yronwood'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Sea of Dorne', \
          type_='sea', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['East Summer Sea','Storms End','The Boneway','Yronwood','Sunspear'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Three Towers', \
          type_='land', \
          supplies=1, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Redwyne Straights','Princes Pass','Dornish Marches','Oldtown'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Princes Pass', \
          type_='land', \
          supplies=1, \
          castles=0, \
          consolidation=1, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Dornish Marches','Three Towers','Starfall','Yronwood','The Boneway'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Starfall', \
          type_='land', \
          supplies=1, \
          castles=1, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['West Summer Sea','East Summer Sea','Salt Shore','Yronwood','Princes Pass'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Yronwood', \
          type_='land', \
          supplies=0, \
          castles=1, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['The Boneway','Princes Pass','Starfall','Salt Shore','Sunspear','Sea of Dorne'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Salt Shore', \
          type_='land', \
          supplies=1, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Sunspear','Yronwood','Starfall','East Summer Sea'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='Sunspear', \
          type_='land', \
          supplies=1, \
          castles=2, \
          consolidation=1, \
          port=1, \
          adjacent_port=0, \
          garrison=0, \
          owner=None, \
          neighbors=['Yronwood','Salt Shore','East Summer Sea','Sea of Dorne'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
Territory(name='East Summer Sea', \
          type_='sea', \
          supplies=0, \
          castles=0, \
          consolidation=0, \
          port=0, \
          adjacent_port=1, \
          garrison=0, \
          owner=None, \
          neighbors=['Shipbreaker Bay','Storms End','Sea of Dorne','Sunspear','Salt Shore','Starfall','West Summer Sea'], \
          footmen=0, \
          cavalry=0, \
          siege=0, \
          ships=0, \
          portShips=0, \
          ), \
]

territories = { t.name: t for t in base }
