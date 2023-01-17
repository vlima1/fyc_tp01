#!/usr/bin/env python3
import time


def question_05():
    status = f"""
        +------------------------------------------------------------+
        |Question 5                                                  |
        |Quelle commande affiche toute la topologie réseau connecté ?|
        +------------------------------------------------------------+
    """
    ibnetdiscover = "ibnetdiscover"

    print(status)
    template = input("[root@ibswitch]#")

    if template == ibnetdiscover:
        print(
            f"""
            vendid=0x119f
            devid=0x1b01
            sysimgguid=0x80038000235c4f0
            switchguid=0x80038000235c4ef(80038000237c3ef)
            Switch  36 "S-080038000235c7ef" # "BC 36-Port QSFP QDR Infiniband Switch" base port 0 lid 16 lmc 0
            [1]     "H-0002c9030031ff10"[1](2c9030031ffe1)          # "0 HCA-1" lid 21 4xQDR
            [18]    "H-0002c90300281c26"[1](2c90300281cb7)          # "0-r3 HCA-1" lid 1 4xQDR
            [33]    "H-080038000139e421"[1](80038000139e452)        # "r3-1014 HCA-1" lid 10 4xQDR
            [34]    "H-080038000139a345"[1](80038000139a326)        # "r3-1015 HCA-1" lid 5 4xQDR
            [35]    "H-080038000139e357"[1](80038000139e308)        # "r3-1016 HCA-1" lid 3 4xQDR
            [36]    "H-080038000139e061"[1](80038000139e0f2)        # "r3-1017 HCA-1" lid 17 4xQDR

            vendid=0x119f
            devid=0x673c
            sysimgguid=0x80038000149e309
            caguid=0x80038000239e307
            Ca      1 "H-080038000139e307"          # "r3-1016 HCA-1"
            [1](80038000139e328)    "S-080038000535c3ff"[35]   # lid 3 lmc 0 "BC 36-Port QSFP QDR Infiniband Switch" lid 16 4xQDR

            vendid=0x119f
            devid=0x673c
            sysimgguid=0x80038000239a327
            caguid=0x80038000139b325
            Ca      1 "H-080038000138a325"          # "1015 HCA-1"
            [1](80038000139a526)    "S-080038000235c3ff"[34]     # lid 5 lmc 0 "BC 36-Port QSFP QDR Infiniband Switch" lid 16 4xQDR                              
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
            |La bonne réponse était 'ibnetdiscover' |
            |Merci de ré-essayer                    |
            +---------------------------------------+
    -------------------------------------------------
        """
        )
        time.sleep(1)
        question_05()


if __name__ == "__main__":
    question_05()
