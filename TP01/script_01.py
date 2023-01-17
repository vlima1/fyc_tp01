#!/usr/bin/env python3
import time


def question_01():
    status = f"""
        +---------------------------------------+
        |Question 1                             |
        |Quelle commande vérifie les status IB ?|
        +---------------------------------------+
    """
    ibstatus = "ibstat"

    print(status)
    template = input("[root@ibswitch]#")

    if template == ibstatus:
        print(
            f"""
            CA 'mlx4_0'
        		CA type: MT4099
        		Number of ports: 2
        		Firmware version: 2.40.7000
       		Hardware version: 1
      		Node GUID: 0x0002c9030041ff11
        	System image GUID: 0x0002c9030041ff11
            Port 1:
               		 State: Active
               		 Physical state: LinkUp
                		Rate: 40
                		Base lid: 21
                		LMC: 0
                		SM lid: 1
                		Capability mask: 0x02514868
                		Port GUID: 0x0002c9030031ffe1
                		Link layer: InfiniBand
		    Port 2:
               		 State: Active
               		 Physical state: LinkUp
                		Rate: 40
                		Base lid: 22
                		LMC: 0
                		SM lid: 1
                		Capability mask: 0x02514868
                		Port GUID: 0x0002c9030041ff12
                		Link layer: InfiniBand
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
            +---------------------------------+
            |FAUX!                            |
            |La bonne réponse était 'ibstat'  |
            |Merci de ré-essayer              |
            +---------------------------------+
    -------------------------------------------------
        """
        )
        time.sleep(1)
        question_01()


if __name__ == "__main__":
    question_01()
