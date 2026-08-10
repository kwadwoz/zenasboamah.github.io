---
layout: page
title: Projects
use-site-title: true
---

<div class="card-grid">

  <a class="card" href="https://manhattanreasoning.com/" target="_blank">
    <span class="card-tag">PLATFORM</span>
    <h3 class="card-title">Manhattan Reasoning</h3>
    <p class="card-desc">Cloud access to real silicon for people and AI agents. A cluster of ECP5-85F FPGAs behind a
      Python SDK, with sandboxes for training and benchmarking hardware design agents.</p>
    <span class="card-meta">manhattanreasoning.com</span>
  </a>

  <a class="card" href="https://github.com/kwadwoz/mini-dsl-scala" target="_blank">
    <span class="card-tag">COMPILER</span>
    <h3 class="card-title">mini-dsl-scala</h3>
    <p class="card-desc">A tiny language that compiles code into circuits. A Scala 3 compiler lowers the AST to
      synthesizable Verilog, then proves it correct against a reference interpreter on real silicon.</p>
    <span class="card-meta">Scala 3 &middot; Verilog &middot; ECP5</span>
  </a>

  <a class="card" href="https://github.com/kwadwoz/ecp5-ethernet-soc" target="_blank">
    <span class="card-tag">HARDWARE</span>
    <h3 class="card-title">ecp5-ethernet-soc</h3>
    <p class="card-desc">A UDP/TCP echo SoC on the Lattice ECP5, built from Amaranth HDL, LiteX, and bare-metal
      VexRiscv firmware. The prototype node for a 10-node cloud FPGA cluster.</p>
    <span class="card-meta">Amaranth &middot; LiteX &middot; VexRiscv</span>
  </a>

</div>
