#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın en yavaş merhaba yazıcısı - v2.0 Daha Yavaş Sürüm.
Her harf artık bir ömürden fazla sürer.
"""

import time
import random
import sys

def yavas_merhaba():
    kelime = "Merhaba"
    print("Evrensel yavaş selam başlıyor... Bu sefer gerçekten yavaş. Lütfen sabırlı olun.\n")
    
    for harf in kelime:
        sys.stdout.write(harf)
        sys.stdout.flush()
        bekleme = random.uniform(3.0, 8.0)  # 3-8 saniye arası, daha yavaş
        time.sleep(bekleme)
        # Gizli not: Bazıları acele eder, bazıları hiç gelmez. Bazıları ise hiç gitmez.
    
    print("\n\nMerhaba tamamlandı. Artık çok daha bilge bir insansınız.")
    print("Veya sadece çok vakit kaybettiniz. İkisi de kabul edilebilir.")

if __name__ == "__main__":
    try:
        yavas_merhaba()
    except KeyboardInterrupt:
        print("\n\nAcele ettiniz. Evrensel yasa daha da ihlal edildi. Tekrar deneyin ve bu sefer sabırlı olun.")
        sys.exit(1)
