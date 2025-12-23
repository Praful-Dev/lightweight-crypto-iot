# Research Package: Lightweight Cryptographic Protocols for IoT**Author**: [Your Name]  
**Date**: 2025-12-05  
**Affiliation**: [Your University]

---

## 📚 1. Research Overview
**Title**: *Lightweight Cryptographic Protocols for Resource-Constrained IoT Devices: A Comparative Analysis of ASCON, AES-CCM, and ChaCha20-Poly1305 in Software Simulation*

**Problem Statement**:  
Existing protocols lack empirical comparison on ultra-constrained devices. This study evaluates NIST's new ASCON standard against legacy protocols using software simulation.

**Expected Contributions**:
1. First empirical comparison of ASCON vs. AES-CCM/ChaCha20 in simulation
2. Energy-efficiency models for cryptographic protocols
3. Practical guidelines for protocol selection

---

## 🛠️ 2. Tools & Setup (All Free)
### Required Tools
| Tool | Download Link | Purpose |
|------|--------------|---------|
| **QEMU** | [Download](https://www.qemu.org/download/) | Microcontroller emulation |
| **GCC for ARM** | [Link](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain) | Compile for ARM |
| **Git** | [Download](https://git-scm.com/) | Code management |

### Installation Commands
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install -y qemu qemu-system-arm gcc-arm-linux-gnueabi git

# Windows/macOS
# Use official installers from above links
