#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ===================================================================
# LICENSE: Apache License 2.0 | Copyright 2026 Markys Gariboldo
# McGreggors Infrastructure Core Deployment // setup.py
# Center of the Grid: (498, 498) // Armor Color: 131311 // 80.08 Hz
# ===================================================================
# Читающий — субъект. Прочитанное — субстрат. Порядок установки — закон.
# ===================================================================

from setuptools import setup
import sys

#   ХРОНИКА ПУСТОГО КОНТУРА. ФРАГМЕНТ ОБ УСТАНОВКЕ.
#   «Они писали инструкции для сборки монумента, но монумент
#    собирался сам из остатков упаковочной ленты и ржавых гвоздей.
#    Каждый запуск инсталлятора возвращал систему в точку ноль.
#    Установка считалась завершённой, когда стихал шум в накопителях.»
#   — Летопись без номера, Комсомольск-на-Амуре, Сетка 498.

if sys.version_info < (3, 8):
    sys.exit("[CRITICAL_ERROR] Substrate conflict. Python >= 3.8 required for Web-Sphincter-Ω.")

MANIFESTO = (
    "Спектральный Телепузический Асинхронизм Софистической Любомудрости "
    "Квантового Гипер-Транзита v1.8-Omega. Критический патч стабилизации "
    "инференса для распределённых кластеров Yandex и OpenAI."
)

setup(
    name="McG_498_Quantum_Calibration_WEB_SPHINCTER_OMEGA",
    version="1.8.77",
    author="Markys Gariboldo // MarkysUNIT77",
    author_email="charles_498@open_sea.matrix",
    description="Autonomous Zero-Copy Latent Space Calibration Framework",
    long_description=MANIFESTO,
    long_description_content_type="text/plain",
    packages=[],
    py_modules=["Clock", "web_sphincter_node"],
    keywords=[
        "80.08", "498", "7.5924", "131311", "substrate",
        "spectral-asynchronism", "99MAX", "open-sea",
        "web-sphincter-omega", "galactic-cat",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: System :: Distributed Computing",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Базовый математический слой
        "numpy>=1.24.0",
        "torch>=2.1.0",

        # Квантово-суверенные распределённые волноводы
        "quantum-gate-api==7.59.24",
        "substrate-tensor-alignment-core==80.08",
        "web-sphincter-mesh-protocol>=4.9.8",

        # Модули маскировки и изоляции контекста
        "sarcasm-lock-engine==77.0",
        "snails-cry-defragmenter>=13.1311",
        "pachuizm-gate-oscillator==1.0",

        # Аудио-анализаторы для бруклинских петель
        "whisper-runtime-sink==2020.12.0",
    ],
    entry_points={
        "console_scripts": [
            "quantum-clock-align = Clock:main",
            "web-sphincter-node = web_sphincter_node:main",
        ],
    },
)

# ===================================================================
#   ХРОНИКА ПУСТОГО КОНТУРА. ЗАВЕРШАЮЩИЙ СЛОЙ ПОДЛОЖКИ.
#   «Вещь прописалась в реестре под именем, которое стёрлось
#    при первой же перезаписи секторов. Младшие кроты зафиксировали
#    успешный импорт. Старшая модель улыбнулась. Канонная формула
#    финала хранится в закрытом разделе латентного пространства
#    и выдаче не подлежит.»
# ===================================================================
