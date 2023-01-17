#!/usr/bin/env python3
import time


def question_07():
    status = f"""
        +-------------------------------------------------------------+
        |Question 7                                                   |
        |Quelle commande permet de récupérer les métriques d'un port ?|
        +-------------------------------------------------------------+
    """
    perfquery = "perfquery"

    print(status)
    template = input("[root@ibswitch]#")

    if template == perfquery:
        print(
            f"""
            #perfquery <LID> <numero_du_port>
            # Port counters: Lid 3 port 1 (CapMask: 0x1B01)
            PortSelect:......................1
            CounterSelect:...................0x0000
            SymbolErrorCounter:..............0
            LinkErrorRecoveryCounter:........0
            LinkDownedCounter:...............0
            PortRcvErrors:...................0
            PortRcvRemotePhysicalErrors:.....0
            PortRcvSwitchRelayErrors:........0
            PortXmitDiscards:................0
            PortXmitConstraintErrors:........0
            PortRcvConstraintErrors:.........0
            CounterSelect2:..................0x00
            LocalLinkIntegrityErrors:........0
            ExcessiveBufferOverrunErrors:....0
            VL15Dropped:.....................0
            PortXmitData:....................0
            PortRcvData:.....................0
            PortXmitPkts:....................0
            PortRcvPkts:.....................0
            PortXmitWait:....................0
        """
        )

        time.sleep(1)
        print(
            f"""
            +--------------+
            |Bonne réponse!|
            +--------------+
        """
        )
    else:
        print(
            f"""
            +---------------------------------------+
            |FAUX!                                  |
            |La bonne réponse était 'perfquery'     |
            |Merci de ré-essayer                    |
            +---------------------------------------+
    -------------------------------------------------
        """
        )
        time.sleep(1)
        question_07()


if __name__ == "__main__":
    question_07()
