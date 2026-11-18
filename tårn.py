
class Alfa:
  def __init__(self,navn:str,liv:int,skade:int):
    self._navn=navn
    self._liv=liv
    self._skade=skade


    
  def __str__(self):
     return f"alfa heter{self._navn}, som har liv på {self._liv} og gjør skaden til motstanderen er {self._skade}" # her skal mann skrive hva den skal gjør 
  
  def get_navn(self):
    return self._navn

  def get_liv(self):
    return self._liv

  def get_skade(self):
    return self._skade

  def set_liv(self,liv):
    self._liv=liv

  def er_i_livet(self):
    return self._liv > 0
    
  def angrip(self,motstander):
    motstander.set_liv(motstander.get_liv()-self._skade)



class Beta(Alfa):
  def __init__(self,navn:str,liv:int,skade:int):
    super(). __init__(navn, liv,skade)
    self._skade=skade

  def __str__(self):
     return f"beta heter {self._navn}, som har liv på{self._liv}. Beta gjør en skade på motstandere n {self._skade}"
 
   
   def angrip(self,motstander):
     motstander.set_liv(motstander.get_liv()-self._skade)
  
  
  




