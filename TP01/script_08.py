#!/usr/bin/env python3
import time


def question_08():
    status = f"""
        +-------------------------------------------------------------------+
        |Question 8                                                         |
        |Quelle commande affiche les informations des liens dans le réseau ?|
        +-------------------------------------------------------------------+
    """
    iblinkinfo = "iblinkinfo"

    print(status)
    template = input("[root@ibswitch]#")

    if template == iblinkinfo:
        print(
            f"""
            0x080038000137469c      8    1[  ] ==( 4X10.0 Gbps Active/  LinkUp)==>3   30[  ] "BC 36-Port QDR IB Switch" ( )
            CA: chivas1010 HCA-1:
            0x0800380001374198     12    1[  ] ==( 4X10.0 Gbps Active/  LinkUp)==>  3   29[  ] "BC 36-Port QDR IB Switch" ( )
            Switch: 0x080038000235b96d Bullx Chassis 36-Port QDR IB Switch:
            3    1[  ] ==(                Down/ Polling)==>             [  ] "" ( )
            3    2[  ] ==(                Down/ Polling)==>             [  ] "" ( )
            3    3[  ] ==(                Down/ Polling)==>             [  ] "" ( )
            3   28[  ] ==(                Down/ Polling)==>             [  ] "" ( )
            3   29[  ] ==( 4X          10.0 Gbps Active/  LinkUp)==>      12    1[  ] "c1010 HCA-1" ( )
            3   30[  ] ==( 4X          10.0 Gbps Active/  LinkUp)==>       8    1[  ] "c1011 HCA-1" ( )
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
            |La bonne réponse était 'iblinkinfo'    |
            |Merci de ré-essayer                    |
            +---------------------------------------+
    -------------------------------------------------
        """
        )
        time.sleep(1)
        question_08()


if __name__ == "__main__":
    question_08()
