def deadlock_detection(available, allocation, request):
    n_process = len(allocation)
    n_resource = len(available)

    work = available.copy()
    finish = [False] * n_process

    while True:
        found = False
        for i in range(n_process):
            if not finish[i]:
                if all(request[i][j] <= work[j] for j in range(n_resource)):
                    # Proses bisa dieksekusi
                    for j in range(n_resource):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    found = True

        if not found:
            break

    deadlock_process = []
    for i in range(n_process):
        if not finish[i]:
            deadlock_process.append(f"P{i}")

    return deadlock_process


# ===== DATA UJI =====
available = [1, 1, 0]

allocation = [
    [0, 1, 0],  # P0
    [2, 0, 0],  # P1
    [3, 0, 3],  # P2
    [2, 1, 1]   # P3
]

request = [
    [0, 0, 0],  # P0
    [1, 0, 1],  # P1
    [0, 0, 1],  # P2
    [0, 0, 0]   # P3
]

# ===== EKSEKUSI =====
deadlock = deadlock_detection(available, allocation, request)

if deadlock:
    print("Deadlock terdeteksi pada proses:", ", ".join(deadlock))
else:
    print("Tidak terjadi deadlock, semua proses dapat diselesaikan.")
