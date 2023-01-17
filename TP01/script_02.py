#!/usr/bin/env python3
import time


def question_02():
    status = f"""
        +--------------------------------------------------+
        |Question 2                                        |
        |Quelle commande est correspond à "ipconfig en IB ?|
        +--------------------------------------------------+
    """
    ibaddr = "ibaddr"

    print(status)
    template = input("[root@ibswitch]#")

    if template == ibaddr:
        print(
            f"""
            GID fe80::2:c903:3a:ff15 LID start 0x15 end 0x15
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
            |La bonne réponse était 'ibaddr'  |
            |Merci de ré-essayer              |
            +---------------------------------+
    -------------------------------------------------
        """
        )
        time.sleep(1)
        question_02()


if __name__ == "__main__":
    question_02()
