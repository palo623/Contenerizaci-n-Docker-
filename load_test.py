import asyncio
import aiohttp
import time
import psutil
import pandas as pd

results = []

URL = "http://localhost:11434/api/generate"

PAYLOAD = {
    "model": "gemma4:e4b",
    "prompt": "Explica Docker en una frase.",
    "stream": False,
    "options": {
        "temperature": 0.2,
        "num_predict": 64
    }
}

async def make_request(session):
    start = time.time()

    try:
        async with session.post(URL, json=PAYLOAD) as response:
            data = await response.json()

            elapsed = time.time() - start

            eval_count = data.get("eval_count", 0)
            eval_duration = data.get("eval_duration", 1)

            tokens_sec = 0

            if eval_duration > 0:
                tokens_sec = eval_count / (eval_duration / 1_000_000_000)

            results.append({
                "status": response.status,
                "time": round(elapsed, 2),
                "tokens_sec": round(tokens_sec, 2)
            })

    except Exception as e:
        print("Error:", e)

        results.append({
            "status": "ERROR",
            "time": None,
            "tokens_sec": 0
        })

async def run_test(users):
    async with aiohttp.ClientSession() as session:
        tasks = [make_request(session) for _ in range(users)]
        await asyncio.gather(*tasks)

def print_results(users):
    df = pd.DataFrame(results)

    print("\n=== RESULTADOS ===")
    print(f"Usuarios concurrentes: {users}")
    print(f"CPU: {psutil.cpu_percent()}%")
    print(f"RAM: {psutil.virtual_memory().percent}%")

    print(df)

    if not df.empty:
        tiempos = df["time"].dropna()

        print(f"\nTiempo medio: {tiempos.mean():.2f}s")
        print(f"Tiempo máximo: {tiempos.max():.2f}s")
        print(f"Tiempo mínimo: {tiempos.min():.2f}s")

        errores = len(df[df["status"] == "ERROR"])
        print(f"Errores: {errores}")

if __name__ == "__main__":
    USERS = 20

    asyncio.run(run_test(USERS))

    print_results(USERS)
