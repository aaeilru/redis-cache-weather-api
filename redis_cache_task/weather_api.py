import json
import time
import redis


# Koneksi ke Redis
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)


def call_weather_api(city):
    """
    Simulasi API call yang lambat.
    Dalam tugas, bagian ini mewakili request ke API eksternal.
    """
    time.sleep(2)

    # Karena https://api.example.com/weather/{city} hanya contoh,
    # response dibuat simulasi agar testing bisa berjalan.
    return {
        "city": city,
        "temperature": 30,
        "condition": "Sunny",
        "source": "api"
    }


def get_weather(city):
    """
    Mengambil data cuaca dengan caching Redis.

    Alur:
    1. Cek cache Redis dengan key weather:{city}
    2. Kalau data ada, return dari cache
    3. Kalau data tidak ada, call API lambat
    4. Simpan hasil API ke Redis
    5. Set expire 300 detik
    6. Return hasil API
    """

    cache_key = f"weather:{city.lower()}"

    # 1. GET dari Redis
    cached_data = redis_client.get(cache_key)

    # 2. Kalau cache ada, return cepat
    if cached_data:
        data = json.loads(cached_data)
        data["source"] = "cache"
        return data

    # 3. Kalau cache tidak ada, panggil API lambat
    data = call_weather_api(city)

    # 4. SET ke Redis
    redis_client.set(cache_key, json.dumps(data))

    # 5. EXPIRE 5 menit
    redis_client.expire(cache_key, 300)

    return data