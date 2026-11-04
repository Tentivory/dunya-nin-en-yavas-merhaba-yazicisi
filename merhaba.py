#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın en yavaş merhaba yazıcısı.
Her harf bir ömür sürer. Ciddi bir iştir.
"""

import time
import random
import sys

def yavas_merhaba():
    kelime = "Merhaba"
    print("Evrensel yavaş selam başlıyor... Lütfen sabırlı olun. Bu bir isyandır.\n")
    
    for harf in kelime:
        sys.stdout.write(harf)
        sys.stdout.flush()
        bekleme = random.uniform(1.5, 4.0)  # 1.5-4 saniye arası
        time.sleep(bekleme)
        # Gizli not: Bazıları acele eder, bazıları hiç gelmez.
    
    print("\n\nMerhaba tamamlandı. Artık daha bilge bir insansınız.")
    print("Veya sadece vakit kaybettiniz. İkisi de kabul edilebilir.")

if __name__ == "__main__":
    try:
        yavas_merhaba()
    except KeyboardInterrupt:
        print("\n\nAcele ettiniz. Evrensel yasa ihlal edildi. Tekrar deneyin.")
        sys.exit(1)
