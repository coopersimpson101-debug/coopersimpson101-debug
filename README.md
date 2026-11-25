<div align="center">

### Engineering student building the whole stack from scratch: silicon-level kernels, flight control, robots, GPUs, distributed systems.

Every project below implements its core algorithms by hand, ships with tests and green CI,
and says plainly in its README what has been verified on real hardware and what is still simulated.

<p>
<img alt="C" src="https://img.shields.io/badge/C-bare--metal%20%26%20kernels-555555?style=flat-square&logo=c&logoColor=white">
<img alt="Python" src="https://img.shields.io/badge/Python-robotics%20%26%20systems-3572A5?style=flat-square&logo=python&logoColor=white">
<img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-WebGPU-3178C6?style=flat-square&logo=typescript&logoColor=white">
<img alt="WGSL" src="https://img.shields.io/badge/WGSL-compute%20shaders-005A9C?style=flat-square&logo=webgpu&logoColor=white">
<img alt="Metal" src="https://img.shields.io/badge/Metal-GPU%20kernels-8F14E9?style=flat-square&logo=apple&logoColor=white">
<img alt="AArch64" src="https://img.shields.io/badge/AArch64-assembly-6E4C13?style=flat-square&logo=arm&logoColor=white">
<img alt="STM32" src="https://img.shields.io/badge/STM32-firmware-03234B?style=flat-square&logo=stmicroelectronics&logoColor=white">
<img alt="ESP32" src="https://img.shields.io/badge/ESP32-ESP--IDF-E7352C?style=flat-square&logo=espressif&logoColor=white">
<img alt="MuJoCo" src="https://img.shields.io/badge/MuJoCo-PPO-FBBF24?style=flat-square">
</p>

<p>
<img src="assets/stats.svg" alt="GitHub activity" width="49%">
<img src="assets/languages.svg" alt="Languages by code size" width="49%">
</p>

</div>

---

### 🌐 Try in your browser

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/coopersimpson101-debug/flipgpu"><img src="assets/flipgpu.png" alt="flipgpu"></a>
<b><a href="https://github.com/coopersimpson101-debug/flipgpu">flipgpu</a></b>: real-time 3D PIC/FLIP and PBF fluids in WebGPU compute shaders. 128k particles, hand-written pressure solver.<br>
<a href="https://coopersimpson101-debug.github.io/flipgpu/"><b>▶ Live demo</b></a>
</td>
<td width="50%" valign="top">
<a href="https://github.com/coopersimpson101-debug/splatweb"><img src="assets/splatweb.png" alt="splatweb"></a>
<b><a href="https://github.com/coopersimpson101-debug/splatweb">splatweb</a></b>: Gaussian splatting renderer in WebGPU. EWA projection, GPU radix sort, streaming .ply/.splat loading.<br>
<a href="https://coopersimpson101-debug.github.io/splatweb/"><b>▶ Live demo</b></a>
</td>
</tr>
</table>

### 🤖 Robotics & embedded

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/coopersimpson101-debug/skyforge-fc"><img src="assets/skyforge-fc.png" alt="skyforge-fc"></a>
<b><a href="https://github.com/coopersimpson101-debug/skyforge-fc">skyforge-fc</a></b>: bare-metal STM32F405 flight controller firmware. Madgwick + EKF fusion, cascaded PID, DShot600 over DMA, CRSF.
</td>
<td width="50%" valign="top">
<a href="https://github.com/coopersimpson101-debug/dog2real"><img src="assets/dog2real.png" alt="dog2real"></a>
<b><a href="https://github.com/coopersimpson101-debug/dog2real">dog2real</a></b>: sim-to-real RL for a 12-DoF quadruped. MuJoCo env, PPO from scratch, domain randomisation; the trained policy walks in sim.
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/coopersimpson101-debug/insight-vio"><img src="assets/insight-vio.png" alt="insight-vio"></a>
<b><a href="https://github.com/coopersimpson101-debug/insight-vio">insight-vio</a></b>: inside-out 6DoF tracking for a DIY VR headset. MSCKF visual-inertial odometry, 0.5 cm ATE on synthetic stereo.
</td>
<td width="50%" valign="top">
<a href="https://github.com/coopersimpson101-debug/meshfind"><img src="assets/meshfind.png" alt="meshfind"></a>
<b><a href="https://github.com/coopersimpson101-debug/meshfind">meshfind</a></b>: offline, end-to-end encrypted Find My network. Rotating X25519 tags, ECIES reports, ESP32 ESP-NOW mesh.
</td>
</tr>
</table>

### ⚙️ Systems

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/coopersimpson101-debug/tinyinfer"><img src="assets/tinyinfer.png" alt="tinyinfer"></a>
<b><a href="https://github.com/coopersimpson101-debug/tinyinfer">tinyinfer</a></b>: LLM inference engine in dependency-free C + Metal. GGUF, BPE tokenizer, KV cache, Q4_0/Q8_0, NEON/AVX2 kernels.
</td>
<td width="50%" valign="top">
<a href="https://github.com/coopersimpson101-debug/orbit-os"><img src="assets/orbit-os.png" alt="orbit-os"></a>
<b><a href="https://github.com/coopersimpson101-debug/orbit-os">orbit-os</a></b>: AArch64 kernel for the Raspberry Pi 5, and the foundation for a phone and smartwatch OS. Chainloader, MMU, buddy allocator, preemptive scheduler, shell.
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/coopersimpson101-debug/raftstore"><img src="assets/raftstore.png" alt="raftstore"></a>
<b><a href="https://github.com/coopersimpson101-debug/raftstore">raftstore</a></b>: self-healing replicated storage on Raft, from scratch. 6.4M simulated steps checked against the safety invariants, and drive pulls at every write boundary.
</td>
<td width="50%" valign="top">
<a href="https://github.com/coopersimpson101-debug/aegis-mcp"><img src="assets/aegis-mcp.png" alt="aegis-mcp"></a>
<b><a href="https://github.com/coopersimpson101-debug/aegis-mcp">aegis-mcp</a></b>: MCP servers for physical hardware (3D printer, drone, NAS, lab) with a human-in-the-loop safety layer and a cost-aware model router.
</td>
</tr>
</table>

---

<div align="center">
<sub>Each repo has a Status table: ✅ tested · 🧪 simulated · ⏳ awaiting hardware. Hardware demos and benchmarks are added as they're recorded.</sub>
</div>

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/coopersimpson101-debug/coopersimpson101-debug/output/snake-dark.svg">
  <img alt="Contribution graph being eaten by a snake" src="https://raw.githubusercontent.com/coopersimpson101-debug/coopersimpson101-debug/output/snake-light.svg">
</picture>
<br><sub>Stat cards and snake regenerate daily via <a href=".github/workflows/profile.yml">GitHub Actions</a>, using only public data.</sub>
</div>
