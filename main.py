# =============================================================================
# MAIN.PY
# SIM Card Cloner — Information
# =============================================================================

import os
import time

# =============================================================================
# BANNER
# =============================================================================

BANNER = r"""
 ███████╗██╗███╗   ███╗     ██████╗██╗      ██████╗ ███╗   ██╗███████╗██████╗
 ██╔════╝██║████╗ ████║    ██╔════╝██║     ██╔═══██╗████╗  ██║██╔════╝██╔══██╗
 ███████╗██║██╔████╔██║    ██║     ██║     ██║   ██║██╔██╗ ██║█████╗  ██████╔╝
 ╚════██║██║██║╚██╔╝██║    ██║     ██║     ██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗
 ███████║██║██║ ╚═╝ ██║    ╚██████╗███████╗╚██████╔╝██║ ╚████║███████╗██║  ██║
 ╚══════╝╚═╝╚═╝     ╚═╝     ╚═════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

                Telecom Security • Mobile Fraud • SIM Research
"""

# =============================================================================
# INTRO
# =============================================================================

INTRO = """
[+] SIM Card Cloner Information Console
[+] Telecom Authentication & Mobile Security Overview
[+] IMSI • Ki Authentication Key • LTE/5G Security
"""

# =============================================================================
# INFORMATION
# =============================================================================

DESCRIPTION = """
A SIM card cloner is a hardware and software tool used to duplicate
the identifying information of a Subscriber Identity Module (SIM)
onto another programmable SIM card.

Modern mobile networks use advanced encryption systems that make
true SIM cloning significantly more difficult than older GSM/2G systems.
"""

HOW_IT_WORKS = [
    "Hardware setup using smart-card reader/writer",
    "Extraction of IMSI and Ki authentication data",
    "Programming data onto a blank SIM card",
    "Authentication attempt on the mobile network"
]

# =============================================================================
# START
# =============================================================================

if __name__ == "__main__":
    main()
