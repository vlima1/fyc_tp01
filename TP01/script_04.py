#!/usr/bin/env python3
import time


def question_04():
    status = f"""
        +----------------------------------------------------------+
        |Question 4                                                |
        |Quelle commande affiche tous les Switchs d'une topologie ?|
        +----------------------------------------------------------+
    """
    ibswitches = "ibswitches"

    print(status)
    template = input("[root@ibswitch]#")

    if template == ibswitches:
        print(
            f"""
            Switch  : 0x080038000235b99d ports 36 "BC 36-Port QDR IB Switch" base port 0 lid 3 lmc 0
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
            +------------------------------------+
            |FAUX!                               |
            |La bonne réponse était 'ibswitches' |
            |Merci de ré-essayer                 |
            +------------------------------------+
    -------------------------------------------------
        """
        )
        time.sleep(1)
        question_04()


if __name__ == "__main__":
    question_04()
