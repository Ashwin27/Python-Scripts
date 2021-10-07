class Config:
  def __init__(self):
    self.test_prop_1 = "dep"
    self.test_prop_2 = "dep"
  
  def printValue(self):
    msg = f"""
    {self.test_prop_1}
    {self.test_prop_2}
    """
    print(msg)

CONFIG = Config()