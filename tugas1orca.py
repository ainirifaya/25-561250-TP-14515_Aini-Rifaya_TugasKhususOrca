class komponenROV:

  def __init__(self, nama, status):
    self.nama = nama
    self.status = status

  def info(self):
    print(f"Nama: {self.nama}, Status: {self.status}")

class Thruster(komponenROV):

  def __init__(self, nama, status, power):
    super().__init__(nama, status)
    self.power = power

  def info(self):
    print(f"Thruster, Nama: {self.nama}, Status: {self.status}, Power: {self.power}")

class Sensor(komponenROV):

  def __init__(self, nama, status, nilai):
    super().__init__(nama, status)
    self.nilai = nilai

  def info(self):
    print(f"Sensor, Nama: {self.nama}, Status: {self.status}, Nilai: {self.nilai}")

def main():
  jumlah = int(input("Masukkan jumlah komponen: "))
  komponen_list = []
  
  for i in range(jumlah):
    input_data = input("Masukkan jenis, nama, status, nilai: ")
    data = input_data.split()
    jenis = data[0]
    nama = data[1]
    status = data[2]
    angka = data[3]

    if jenis == "Thruster" or jenis == "thruster":
      komponen = Thruster(nama, status, angka)
    elif jenis == "Sensor" or jenis == "sensor":
      komponen = Sensor(nama, status, angka)

    komponen_list.append(komponen)

  print("- Output Informasi Komponen -")
  for k in komponen_list:
    k.info()

if __name__ == "__main__":
  main()
