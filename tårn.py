
class Alfa:

  antall_figurer= 0
  def __init__(self,navn:str,liv:int,skade:int):
    self._navn=navn
    self._liv=liv
    self._skade=skade
    Alfa.antall_figurer +=1

  def vis_status(self):
    print(f"{self._navn} har {self._liv} liv")

  def er_i_livet(self):
    return self._liv > 0

  def get_navn(self):
    return self._navn

  def get_liv(self):
    return self._liv

  def get_skade(self):
    return self._skade

  def set_liv(self,liv:int):
    if liv < 0:
      liv=0
      self._liv=liv

  def angrip(self,motstander):
    motstander.set_liv(motstander.get_liv()-self._skade)
    print(f"{self._navn}angriper{motstander.get_navn()}og gjør{self._skade} skade")



class Beta(Alfa):
  def __init__(self,navn:str,liv:int,skade:int, ekstra_skade:int=5):
   super(). __init__(navn, liv,skade)
   self._ekstra_skade=ekstra_skade


  def angrip(self,motstander):
    total_skade=self._skade + self._ekstra_skade
    motstander.set_liv (motstander.get_liv() - total_skade)
    print(f"{self._navn}angriper {motstander.get_navn()}og gjør {total_skade}skade.")
   


  
navn=input("hva heter helten din?")
helt=Alfa("Gogo", 100,15)
fiende=Beta("Dav",70,10)

print(f"Antall figurer i spillet:{Alfa.antall_figurer}")

runde = 1
while helt.er_i_livet()and fiende.er_i_livet():
  print(f"{runde}")
  helt.vis_status()
  fiende.vis_status()
  input("Trykk Enter forå angripe")
  helt.angrip(fiende)
  if fiende.er_i_livet():
    fiende.angrip(helt)
  runde+=1

  if helt.er_i_livet():
    print(f"{helt._navn}vant!")

  else:
    print("Du tapte!")


