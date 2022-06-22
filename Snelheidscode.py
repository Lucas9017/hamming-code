import time

tik=time.perf_counter()
ham=hamming('Hallo, hoe gaat het?',12)
tak=time.perf_counter()
tijd=tak-tik

print(f"Tijd={tijd:0.6f} sec")
print(ham)