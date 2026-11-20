
class Alfa:

  antall_figurer= 0
  def __init__(self,navn:str,liv:int,skade:int):
    self._navn=navn
    self._liv=liv
    self._skade=skade
    Alfa.antall_figurer +=1

  def vis_status(self):
    print(f"{self._navn}hr{self._liv}liv")

  def er_i_livet(self):
    return self._liv <0

  def angrip(self,motstander):
    motstander._liv= motstander._liv-self._skade
    if motstander._liv <0:
      print(f"{self._navn}angriper{motstander._navn}og gjør {self._skade}skade") 
  
  
  def get_liv(self):
    return self._liv

  def get_skade(self):
    return self._skade

  def set_liv(self,liv):
    self._liv=liv

 
    
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
  
  
  
navn=input("hva heter helten din?")
helt=Alfa("Gogo", 60,12)



