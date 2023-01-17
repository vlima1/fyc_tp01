#!/usr/bin/env python3
import time


def question_06():
    status = f"""
        +-----------------------------------------------------------+
        |Question 6                                                 |
        |Quelle commande vérifie la connectivité de tout le réseau ?|
        +-----------------------------------------------------------+
    """
    ibqueryerrors = "ibqueryerrors"

    print(status)
    template = input("[root@ibswitch]#")

    if template == ibqueryerrors:
        print(
            f"""
            Errors for "c015 HCA-1"
   		            GUID 0x800380001389e62 port 1: [PortRcvErrors == 52]
            Errors for 0x80038000235b96d "BC36-Port QDR IB Switch"
            GUID 0x80038000235b9 port ALL: [PortRcvSwitchRelayErrors == 31] [PortXmitDiscards == 5]
            GUID 0x80038000235b96d port 17: [PortRcvSwitchRelayErrors == 29]
            GUID 0x80038000235b96d port 29: [PortXmitDiscards == 1]
            GUID 0x80038000235b96d port 31: [PortRcvSwitchRelayErrors == 2] [PortXmitDiscards == 1]
            
        ## Summary: 5 nodes checked, 2 bad nodes found
        ##          42 ports checked, 6 ports have errors beyond threshold               
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
            |La bonne réponse était 'ibqueryerrors' |
            |Merci de ré-essayer                    |
            +---------------------------------------+
    -------------------------------------------------
        """
        )
        time.sleep(1)
        question_06()


if __name__ == "__main__":
    question_06()
