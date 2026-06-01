import time
from weather_api import get_weather


# First call - should be slow
start = time.time()
result1 = get_weather("Jakarta")
time1 = time.time() - start

print("First call result:", result1)
print(f"First call: {time1:.2f}s")


# Second call - should be fast because cached
start = time.time()
result2 = get_weather("Jakarta")
time2 = time.time() - start

print("Second call result:", result2)
print(f"Second call (cached): {time2:.2f}s")


print("\nPenjelasan:")
print("First call lambat karena data belum ada di cache, sehingga harus call API.")
print("Second call cepat karena data sudah disimpan di Redis cache.")
print("Cache akan expired otomatis setelah 300 detik atau 5 menit.")