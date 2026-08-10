---
layout: page
title: Projects
use-site-title: true
---

### [Manhattan Reasoning](https://manhattanreasoning.com/)

A hardware reasoning platform I help build, giving people — and AI agents — cloud access to real silicon. It provides a cluster of Lattice ECP5-85F FPGAs behind a Python SDK and CLI, an open toolchain built on Yosys, nextpnr, and LiteX, and sandboxed environments with verifiable reward signals for training and benchmarking hardware design agents.

### [mini-dsl-scala](https://github.com/kwadwoz/mini-dsl-scala)

A tiny language that compiles code into circuits. You write a small imperative program in a Lox-like DSL; the Scala 3 compiler lowers the AST to synthesizable Verilog with a Wishbone register interface plus a matching Python client, then proves the hardware correct by simulating it and comparing against a reference interpreter. The generated design runs on real ECP5-85F silicon.

`Source → Scanner → Parser → AST → Verilog + Python → FPGA`

### [ecp5-ethernet-soc](https://github.com/kwadwoz/ecp5-ethernet-soc)

A UDP/TCP echo SoC for the Lattice ECP5 Evaluation Board. The host sends packets over Ethernet; the FPGA writes each payload into a hardware BRAM, reads it back, and echoes it. Built from an Amaranth HDL Wishbone BRAM inside a LiteX SoC, bare-metal VexRiscv RISC-V firmware (with an lwIP TCP variant), and a host-side harness that sweeps payload sizes to measure round-trip latency and throughput. This is the prototype node for a 10-node cloud FPGA cluster.
