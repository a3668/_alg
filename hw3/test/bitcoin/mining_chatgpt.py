import hashlib
import json
import random
import time

def hash(text):
    m = hashlib.sha256()
    m.update(text.encode('utf-8'))
    return m.hexdigest()

record = {
  'nonce': 0,
  'data': 'john => mary $2.7',
}

def mining(record, prefix='00000', max_attempts=10**8):
    """
    使用隨機亂數方式挑選 nonce，直到找到符合 prefix 的 hash。
    回傳 dict: {'nonce': ..., 'hash': ..., 'attempts': ..., 'time': ...}
    若超過 max_attempts 還找不到，回傳 None。
    """
    attempts = 0
    start = time.time()
    while attempts < max_attempts:
        attempts += 1
        record['nonce'] = random.randint(0, 1000000000000)
        h = hash(json.dumps(record))
        if h.startswith(prefix):
            elapsed = time.time() - start
            return {'nonce': record['nonce'], 'hash': h, 'attempts': attempts, 'time': elapsed}
    return None

# ================================
#   第一組實驗：prefix = '00000'
#   找到開頭有 5 個 0 的 hash
# ================================
results_5 = []
for i in range(5):
    r = mining(record.copy(), prefix='00000')
    if r:
        results_5.append(r)
        # 輸出格式：nonce:..., hash:..., attempts:..., time:...
        print(f"nonce:{r['nonce']}, hash:{r['hash']}, attempts:{r['attempts']}, time:{r['time']:.6f}")

if results_5:
    avg_attempts_5 = sum(r['attempts'] for r in results_5) / len(results_5)
    avg_time_5 = sum(r['time'] for r in results_5) / len(results_5)
    print(f"AVERAGE_ATTEMPTS(00000):{avg_attempts_5:.2f}, AVERAGE_TIME(00000):{avg_time_5:.6f}")


print("\n--- prefix = 0000 (4 個 0) ---\n")


# ================================
#   第二組實驗：prefix = '0000'
#   找到開頭有 4 個 0 的 hash
# ================================
results_4 = []
for i in range(5):
    r = mining(record.copy(), prefix='0000')
    if r:
        results_4.append(r)
        print(f"nonce:{r['nonce']}, hash:{r['hash']}, attempts:{r['attempts']}, time:{r['time']:.6f}")

if results_4:
    avg_attempts_4 = sum(r['attempts'] for r in results_4) / len(results_4)
    avg_time_4 = sum(r['time'] for r in results_4) / len(results_4)
    print(f"AVERAGE_ATTEMPTS(0000):{avg_attempts_4:.2f}, AVERAGE_TIME(0000):{avg_time_4:.6f}")
    











'''def hash(text):
    m = hashlib.sha256()
    m.update(text.encode('utf-8'))
    return m.hexdigest()

record = {
    'nonce': 0,
    'data': 'john => mary $2.7',
}

def mining(record, prefix='000000', max_nonce=10**12):
    """
    從 0 起遞增 nonce，暴力嘗試直到 hash 開頭符合 prefix（例如 '000000'）。
    回傳 dict: {'record': record, 'hash': h, 'attempts': attempts, 'time': elapsed_seconds}
    若超過 max_nonce 則回傳 None。
    """
    attempts = 0
    start = time.time()
    for i in range(max_nonce):
        record['nonce'] = i
        attempts += 1
        # sort_keys=True 保證同一筆 record 轉成 JSON 的鍵順序一致（避免不同順序導致不同 hash）
        h = hash(json.dumps(record, sort_keys=True))
        if h.startswith(prefix):
            elapsed = time.time() - start
            # 回傳時複製 record，避免外部再被改動影響紀錄
            return {'record': record.copy(), 'hash': h, 'attempts': attempts, 'time': elapsed}
    return None

result = mining(record, prefix='000000')   # prefix 少一點 0，較容易找到
print(result)'''

