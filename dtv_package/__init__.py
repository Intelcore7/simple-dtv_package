from .core import Info, Draw           #not "getVisual" because "." means from local location; exposes "Info" and "Draw" for import

__all__ = ['Info', 'Draw']                  #look up "how __init__.py works"; basically: "from [package] import *" = from __innit__ import __all__