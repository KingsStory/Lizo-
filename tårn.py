
class Alfa:
  def __init__(self,navn:str,liv:int,skade:int):
    self._navn=navn
    self._liv=liv
    self._skade=skade


    
  def __str__(self):
     return f"alfa heter{self._navn}, som har liv på {self._liv} og gjør skaden til motstanderen er {self._skade}" # her skal mann skrive hva den skal gjør 
  

  def angrip(self,motstander):
    motstander._hp-=self._skade



class Beta(Alfa):
  def __init__(self,navn:str,liv:int,skade:int):
    super(). __init__(navn, liv,skade)







