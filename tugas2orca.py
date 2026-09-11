class MissionManager:
  def __init__(self, object, confidence, distance, status, action):
    self.object = object
    self.confidence = confidence
    self.distance = distance
    self.status = status
    self.action = action
    
  def info(self):
    print(f"Object Detected: {self.object}")
    print(f"Confidence: {self.confidence}")
    print(f"Distance: {self.distance} m")
    print()
    print(f"Mission State: {self.status}")
    print(f"Action: {self.action}")

def main():
  object = input("Object (if nothing than type '-'): ")
  confidence = float(input("Confidence: "))
  distance = float(input("Distance: "))

  if object == "tidak ada" or object == "-":
    status = "SEARCHING"
    action = "SCAN AREA"
  elif confidence >= 0.70:
    status = "DETECTED"
    action = "APPROACH TARGET"
  elif distance <= 0.5:
    status = "MISSION_COMPLETE"
    action = "STOP & HOLD"
  elif distance <= 2.0:
    status = "APPROACHING"
    action = "SLOW DOWN"
  else:
    status = "UNKNOWN"
    action = "HOVER"

  print("\n- OUTPUT -")
  misi = MissionManager(object, confidence, distance, status, action)
  misi.info()

if __name__ == "__main__": 
  main()
