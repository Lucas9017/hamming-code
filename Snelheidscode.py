import time

tik=time.perf_counter()
ham=hamming('"Hallo, ik wil 130 broodjes", zei Jannes',20)
tak=time.perf_counter()
tijd=tak-tik

print(f"Tijd={tijd:0.8f} sec")
print(ham)