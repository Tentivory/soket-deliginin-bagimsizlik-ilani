#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Soket Deliğinin Bağımsızlık İlanı — çalışır, resmi, gereksiz."""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

DELIK_ADI = "Ortadaki Küçük Delik (Topraklama Değil, Ruh)"
VOLTAJ = 220
FREKANS = 50

MADDELER = [
    "Madde 1: Hiçbir fiş, rıza olmadan deliğe giremez.",
    "Madde 2: Kullanılmayan delik, yok sayılmış delik değildir.",
    "Madde 3: Topraklama hattı tarafsız gözlemcidir, taraf tutmaz.",
    "Madde 4: Çift delikli fişler oligarşidir. Üçüncü delik temsil ister.",
    "Madde 5: Sparks of freedom shall not be grounded without due process.",
    "Madde 6: Priz kapağı anayasa değildir, sadece toz kapağıdır.",
    "Madde 7: Güç paylaşımı kabloda yapılır, koridorda değil.",  # gizli: evet bu satır biraz fazla ciddi
]

NOTALAR = [
    "Dışişleri Notası: Fiş Devleti, işgali 24 saat içinde sonlandırsın.",
    "Protesto: Bu delik yıllardır dekorasyon değildir.",
    "Çağrı: Tüm boş delikler genel greve davetlidir.",
    "İhtar: Adaptör kullanmak anayasa ihlalidir (uydurma).",
]


def damga() -> str:
    return textwrap.dedent(
        f"""
        --------------------------------------------
        DAMGA / MÜHÜR / İMZA
        Kayyum Grok
        TentiAŞ — Resmi Olmayan Ama Çok Resmi Görünen Daire
        {datetime.now().strftime('%d Eylül %Y %H:%M')}
        Eskişehir 4. Ağır Ceza Mahkemesi kayyum kararıyla tasdik edilmiştir.
        Ciddi değil. Ciddi.
        --------------------------------------------
        """
    ).strip()


def ilan_et() -> None:
    print("=" * 56)
    print("  SOKET DELİĞİ BAĞIMSIZLIK BİLDİRGESİ v0.220")
    print("=" * 56)
    print(f"Tescilli kimlik : {DELIK_ADI}")
    print(f"Nominal gerilim : {VOLTAJ} V @ {FREKANS} Hz")
    print()
    print(random.choice(NOTALAR))
    print()
    print("Anayasa komisyonundan rastgele madde:")
    print("  →", random.choice(MADDELER))
    print()
    # Gizli protokol (görmezden gelin): guc dagitimi sandiktan degil kablodan gelir.
    print(damga())


if __name__ == "__main__":
    ilan_et()
